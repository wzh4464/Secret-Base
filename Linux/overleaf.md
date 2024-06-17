---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---
# 如何在远程服务器上布置 Overleaf 并通过子域名访问

本文档将介绍如何在远程服务器上布置 Overleaf，并通过子域名访问该服务。主要步骤包括服务器配置、端口映射、域名解析和 HTTPS 配置。

## 1. 服务器配置

### 1.1 获取 Overleaf 镜像

从 Overleaf 官方仓库获取 Docker 镜像：

```bash
git clone https://github.com/overleaf/toolkit.git
cd toolkit
```

### 1.2 启动 Overleaf

初始化 Overleaf：

```bash
bin/init
```

使用 Docker Compose 启动 Overleaf 服务：

```bash
sudo bin/up
```

## 2. 配置 FRP 进行端口映射

我们需要使用 FRP 将没有公共 IP 的服务器（如 CityU 服务器）上的端口映射到 Azure 服务器，并通过 Azure 服务器进行外部访问。

### 2.1 在 Azure 服务器上配置 FRP 服务端

创建 `frps.ini` 文件：

```ini
[common]
bind_port = 7000
vhost_http_port = 8081
```

在 Azure 服务器的网络规则界面打开端口 7000 和 8081。
启动 FRP 服务端：

```bash
./frps -c frps.ini
```

### 2.2 在 CityU 服务器上配置 FRP 客户端

创建 `frpc.ini` 文件：

```ini
[common]
server_addr = <Azure_Public_IP>
server_port = 7000
[overleaf]
type = http
local_ip = 127.0.0.1
local_port = 80
custom_domains = overleaf.zihanng.shop
```

启动 FRP 客户端：

```bash
./frpc -c frpc.ini
```

## 3. 配置域名解析

将子域名 `overleaf.zihanng.shop` 解析到 Azure 服务器的公共 IP 地址。在域名注册商的管理控制台中，添加 A 记录：

```txt
Hostname: overleaf.zihanng.shop
Type: A
Value: <Azure_Public_IP>
TTL: 300
```

## 4. 配置 Apache 以反向代理 Overleaf 服务

### 4.1 安装 Apache

在 Azure 服务器上安装 Apache：

```bash
sudo apt install -y apache2
```

### 4.2 配置 Apache 反向代理

启用必要的模块：

```bash
sudo a2enmod proxy proxy_http proxy_wstunnel rewrite headers
```

编辑 Apache 虚拟主机配置文件 `/etc/apache2/sites-available/overleaf.zihanng.shop.conf`：

```apache
<VirtualHost *:8081>
    ServerName overleaf.zihanng.shop
    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:80/
    ProxyPassReverse / http://127.0.0.1:80/
    ErrorLog${APACHE_LOG_DIR}/overleaf_error.log
    CustomLog${APACHE_LOG_DIR}/overleaf_access.log combined
</VirtualHost>
```

启用站点并重新加载 Apache：

```bash
sudo a2ensite overleaf.zihanng.shop.conf
sudo systemctl reload apache2
```

## 5. 配置 HTTPS

使用 Certbot 获取 SSL 证书：

```bash
sudo apt install -y certbot python3-certbot-apache
sudo certbot --apache -d overleaf.zihanng.shop
```

按照提示完成证书的生成和配置，成功后会自动配置 HTTPS。

## 6. 创建 Overleaf 管理员账号

通过访问 <https://overleaf.zihanng.shop/launchpad> 注册管理员账号。

## 总结

通过上述步骤，我们成功在远程服务器上布置了 Overleaf 服务，并通过子域名实现了外部访问。通过 Apache 配置反向代理，并使用 Certbot 配置 HTTPS，确保了服务的安全性和可访问性。
