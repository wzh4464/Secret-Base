---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---
# ssh 端口转发
目标是从设备 A（本地，无公共 IP）通过设备 C（Azure，有公共 IP）转发 SSH 连接到设备 B（zihanwu@xxx，无公共 IP）。以下是具体步骤：
1. **在设备 B 上启动 SSH 隧道**：
   在设备 B 上使用 SSH 建立一个到设备 C 的反向隧道：
   ```bash
   ssh -R 2000:localhost:22 zihan@4.216.86.63
   ```
   这个命令的含义是：将设备 C 的 2000 端口转发到设备 B 的 22 端口。确保这个命令持续运行，或者可以使用 `tmux` 或 `screen` 来保持会话。
2. **在设备 C 上配置 SSH 允许网关端口转发**：
   确保设备 C 上的 SSH 配置允许网关端口转发。编辑 `/etc/ssh/sshd_config` 并确保以下行存在且未被注释：
   ```plaintext
   GatewayPorts yes
   ```
   然后重新启动 SSH 服务：
   ```bash
   sudo systemctl restart sshd
   ```
3. **在设备 A 上连接到设备 B**：
   在设备 A 上，使用 SSH 通过设备 C 转发连接到设备 B：
   ```bash
   ssh -p 2000 zihanwu@4.216.86.63
   ```
   这个命令的含义是：从设备 A 通过设备 C 的 2000 端口连接到设备 B 的 SSH 服务。
通过这些步骤，你应该能够从设备 A 通过设备 C 成功地 SSH 连接到设备 B。如果连接过程中遇到任何问题，请检查防火墙设置和端口开放情况，确保所有相关端口（如设备 C 的 22 和 2000 端口）都是开放和可访问的。
你可以使用 `rsync` 命令来指定目标为使用端口 2000 的 SSH 连接。下面是如何将 `rsync` 与特定端口一起使用的示例：
```bash
rsync -avz -e 'ssh -p 2000' /path/to/local/directory/ zihanwu@4.216.86.63:/path/to/remote/directory/
```
解释：
- `-avz` 是常用的 `rsync` 选项：
  - `-a` 表示归档模式，递归传输目录并保持文件属性。
  - `-v` 表示详细模式，显示传输过程中的详细信息。
  - `-z` 表示压缩数据在传输过程中。
- `-e 'ssh -p 2000'` 指定使用 SSH 并设置端口为 2000。
- `/path/to/local/directory/` 是本地源目录路径。
- `zihanwu@4.216.86.63:/path/to/remote/directory/` 是远程目标路径。
确保所有路径正确，并且你有权限访问和修改这些目录。
例如，要将本地目录 `/home/user/data/` 同步到远程主机的目录 `/home/zihanwu/data/`，可以使用以下命令：
```bash
rsync -avz -e 'ssh -p 2000' /home/user/data/ zihanwu@4.216.86.63:/home/zihanwu/data/
```
运行此命令后，`rsync` 将通过 SSH 在指定端口 2000 上进行连接，并将本地目录同步到远程主机。
