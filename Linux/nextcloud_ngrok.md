# 使用 ngrok 在 Nextcloud 上创建公共访问

### 步骤 1：安装 Nextcloud

1. 安装 Nextcloud：

```bash
sudo snap install nextcloud
```

1. 检查 Nextcloud 服务状态：

```bash
sudo snap services nextcloud
```

1. 查看 Nextcloud 的状态：

```bash
sudo nextcloud.occ status
```

### 步骤 2：安装 ngrok

1. 下载并解压 ngrok：

```bash
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
tar -xvzf ngrok-v3-stable-linux-amd64.tgz
```

1. 添加 ngrok 的身份验证令牌：

```bash
ngrok config add-authtoken 2hT0Pc3KdiXLhRhm4ecsFBX0ZVr_7ENPcnYJA6fj377HS4sA5
```

### 步骤 3：配置 ngrok 作为 HTTP 隧道

1. 运行 ngrok HTTP 隧道：

```bash
ngrok http --domain=endlessly-social-joey.ngrok-free.app 80
```

### 步骤 4：配置 Nextcloud 信任的域

1. 将 ngrok 域名添加到 Nextcloud 的信任域：

```bash
sudo nextcloud.occ config:system:set trusted_domains 2 --value="endlessly-social-joey.ngrok-free.app"
```

### 步骤 5：访问 Nextcloud

1. 现在你可以通过 `https://endlessly-social-joey.ngrok-free.app` 访问你的 Nextcloud 实例。

### 注意事项

- 确保 ngrok 正常运行，并且你的域名已经正确配置。
- 通过 `tmux` 或其他会话管理工具保持 ngrok 进程持续运行。

### 挂载硬盘到 Nextcloud webdav

由于 Nextcloud 的 webdav 文件系统要求权限，因此将硬盘挂载到 Nextcloud 比较简单

```bash
sudo mkdir /var/snap/nextcloud/common/nextcloud/data/username/files/mnt
sudo mount /dev/sda1 /var/snap/nextcloud/common/nextcloud/data/username/files/mnt
sudo nextcloud.occ files:scan --all
```
