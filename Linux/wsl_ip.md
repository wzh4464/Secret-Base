---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---

# WSL2 静态 IP 配置和 SSH 自启动设置

## 问题概述

1. WSL2 默认使用动态 IP 地址，每次启动时 IP 可能会变化。
2. 需要在 WSL2 启动时自动启动 SSH 服务。
3. 需要为 WSL2 设置静态 IP 地址。

## 解决方案

### 1. 配置 .wslconfig 文件

在 Windows 用户目录下创建或编辑 `.wslconfig` 文件：

```ini
[wsl2]
networkingMode=static
ipv4Address=172.17.155.206/20
```

### 2. 配置 WSL 内部设置

在 WSL 中编辑 `/etc/wsl.conf` 文件：

```ini
[boot]
systemd=true
command="service ssh start && /usr/local/bin/set-static-ip.sh"

[network]
generateResolvConf = false
```

### 3. 创建静态 IP 设置脚本

在 WSL 中创建文件 `/usr/local/bin/set-static-ip.sh`：

```bash
#!/bin/bash
ip addr add 172.17.155.206/20 dev eth0
ip route add default via 172.17.144.1
```

使脚本可执行：

```bash
sudo chmod +x /usr/local/bin/set-static-ip.sh
```

## 实施步骤

1. 在 Windows 中创建/编辑 `.wslconfig` 文件。
2. 在 WSL 中编辑 `/etc/wsl.conf` 文件。
3. 在 WSL 中创建并设置 `set-static-ip.sh` 脚本。
4. 在 Windows PowerShell 中运行 `wsl --shutdown` 关闭 WSL。
5. 重新启动 WSL 并验证设置。

## 验证

重启 WSL 后，运行以下命令检查 IP 地址：

```bash
ip addr show eth0
```

IP 地址应该是设置的静态 IP（172.17.155.206）。

## 注意事项

- 确保选择的静态 IP 地址不会与网络中的其他设备冲突。
- 如果遇到 DNS 解析问题，可以考虑删除 `generateResolvConf = false` 行。
- 定期检查 WSL 更新，因为未来的更新可能会改变网络配置方式。

这个笔记总结了我们讨论的主要问题、解决方案和实施步骤。它提供了一个快速参考，以便将来需要时可以轻松地重新配置或排障。
