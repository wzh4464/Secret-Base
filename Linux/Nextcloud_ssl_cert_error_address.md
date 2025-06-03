# Nextcloud 通过 Cloudflare + FRP 实现安全公网访问配置指南

✅ 总体目标

通过 Cloudflare → Azure (frps) → frpc → Apache + PHP-FPM (Nextcloud) 架构，使公网用户能够安全访问私有服务器中的 Nextcloud 服务。

⸻

🧱 技术组件
 • 域名：nc.zihanng.shop
 • CDN/反向代理：Cloudflare（“橙色云”开启）
 • 公网服务器：Azure VM（运行 frps）
 • 内网服务器：家庭或本地服务器（运行 frpc，连接 Nextcloud）
 • Web服务：Apache + PHP-FPM 8.3
 • HTTPS 证书：Let’s Encrypt 通配符证书

⸻

🪜 步骤总结

🔐 1. 获取并部署通配符 SSL 证书（在 Azure）

sudo certbot certonly \
  --dns-cloudflare \
  --dns-cloudflare-credentials /root/.secrets/certbot/cloudflare.ini \
  -d zihanng.shop -d "*.zihanng.shop"

然后将生成的证书用于 frps.ini：

[common]
vhost_https_port = 443
tls_cert_file = /etc/letsencrypt/live/zihanng.shop/fullchain.pem
tls_key_file  = /etc/letsencrypt/live/zihanng.shop/privkey.pem

🔁 若证书更新需重启 frps：

sudo systemctl restart frps

⸻

🌐 2. 配置 Cloudflare
 • DNS 设置中 nc.zihanng.shop 指向 Azure IP
 • 开启"橙色云"代理（Proxy）
 • SSL 模式设为 Full

⸻

🚇 3. 配置 frpc（本地）

[nextcloud]
type = https
local_ip = 127.0.0.1
local_port = 8443
custom_domains = nc.zihanng.shop
tls_verify = false

⸻

📦 4. Apache 配置（本地）

nextcloud.conf：

<VirtualHost *:8443>
    ServerName nc.zihanng.shop
    DocumentRoot /var/www/nextcloud

    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/zihanng.shop/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/zihanng.shop/privkey.pem

    <Directory /var/www/nextcloud>
        Require all granted
        AllowOverride All
        Options FollowSymLinks MultiViews
    </Directory>

    <FilesMatch \.php$>
        SetHandler "proxy:unix:/run/php/php8.3-fpm.sock|fcgi://localhost/"
        SSLOptions +StdEnvVars
    </FilesMatch>

    ErrorLog ${APACHE_LOG_DIR}/nextcloud_error.log
    CustomLog ${APACHE_LOG_DIR}/nextcloud_access.log combined
</VirtualHost>

⸻

🧑‍🔧 5. PHP-FPM 用户匹配配置

确保 /etc/php/8.3/fpm/pool.d/www.conf：

user = zihan
group = zihan
listen = /run/php/php8.3-fpm.sock
listen.owner = zihan
listen.group = zihan
listen.mode = 0660

⚠️ 否则 Apache 无法访问 socket，连接会“超时无响应”。

⸻

🔄 6. 重启服务并测试

sudo systemctl restart php8.3-fpm
sudo systemctl restart apache2

测试：

curl -vk <https://127.0.0.1:8443>
curl -vk <https://nc.zihanng.shop>

返回 HTTP/1.1 302 Found 并跳转到 /index.php/login 即为成功。

⸻

🧠 总结要点经验

问题 解决方式
curl 请求无响应 Apache 与 PHP-FPM 没连通
proxy_fcgi:error 没设置 SetHandler 或 socket 权限错误
TLS handshake 成功但页面不加载 本地服务器未返回有效响应，通常为 PHP 问题
Cloudflare TLS 校验失败 证书未包含 *.zihanng.shop
Apache 以自定义用户运行 PHP-FPM socket 权限需同步调整

⸻

✅ 最终结果

你的 Nextcloud 服务现已通过：

🔒 Cloudflare + HTTPS
🌐 自定义子域名
🌍 公网访问
🚇 FRP 加密穿透
✔️ 成功上线！
