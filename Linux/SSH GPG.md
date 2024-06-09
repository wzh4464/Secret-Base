# 在本地为 macOS 时，通过 SSH 连接到远程 Ubuntu 服务器并在 VSCode 中使用 GPG 签名进行 Git 提交的配置步骤如下

### 1. 本地配置

#### 1.1 配置 GPG 代理

在本地 macOS 机器上，确保 GPG 代理支持 SSH：

```bash
echo "enable-ssh-support" >> ~/.gnupg/gpg-agent.conf
echo "extra-socket /Users/$(whoami)/.gnupg/S.gpg-agent.extra" >> ~/.gnupg/gpg-agent.conf
```

重启 GPG 代理以应用更改：

```bash
gpgconf --kill gpg-agent
gpgconf --launch gpg-agent
```

#### 1.2 设置环境变量

确保 GPG 代理和 SSH 代理正确设置：

```bash
echo "export GPG_TTY=$(tty)" >> ~/.bash_profile
echo "export SSH_AUTH_SOCK=$(gpgconf --list-dirs agent-extra-socket)" >> ~/.bash_profile
source ~/.bash_profile
```

### 2. 远程配置

#### 2.1 在远程服务器上安装 GPG 和相关工具

在远程 Ubuntu 服务器上，确保安装了 GPG 和 `pinentry`：

```bash
sudo apt update
sudo apt install gnupg2 pinentry-curses
```

#### 2.2 配置 SSH 代理转发

在本地 macOS 机器上编辑或创建 `~/.ssh/config` 文件，添加以下内容：

```plaintext
Host yourserver
  HostName yourserver.com
  User yourusername
  ForwardAgent yes
  RemoteForward /home/yourusername/.gnupg/S.gpg-agent /Users/yourusername/.gnupg/S.gpg-agent.extra
```

将 `yourserver.com` 和 `yourusername` 替换为你的服务器域名和用户名。

### 3. VSCode 配置

#### 3.1 配置 SSH 插件

确保 VSCode 的 SSH 插件配置支持代理转发。编辑 SSH 插件的设置，确保 `ForwardAgent` 设置为 `yes`。

### 4. 在远程服务器上配置 GPG

在远程 Ubuntu 服务器上，确保 GPG 代理配置正确：

```bash
echo "pinentry-program /usr/bin/pinentry-curses" >> ~/.gnupg/gpg-agent.conf
echo "default-cache-ttl 600" >> ~/.gnupg/gpg-agent.conf
echo "max-cache-ttl 7200" >> ~/.gnupg/gpg-agent.conf
```

重启 GPG 代理：

```bash
gpgconf --kill gpg-agent
gpgconf --launch gpg-agent
```

### 5. 验证配置

#### 5.1 在远程服务器上测试 GPG 签名

在远程服务器上，测试 GPG 签名是否正常工作：

```bash
echo "test" | gpg --clearsign
```

#### 5.2 配置 Git 使用 GPG 签名

在远程服务器上，确保 Git 配置正确使用 GPG 签名：

```bash
git config --global user.signingkey ABCDEF1234567890
git config --global commit.gpgSign true
```

将 `ABCDEF1234567890` 替换为你的 GPG 密钥 ID。

### 6. 在 VSCode 中进行 GPG 签名的 Git 提交

通过 VSCode 连接到远程服务器，进行 GPG 签名的 Git 提交：

```bash
git commit -m "Your commit message" -S
```

### 验证

在 VSCode 中尝试进行 GPG 签名的 Git 提交：

```bash
git commit -m "Your commit message" -S
```

如果一切配置正确，GPG 代理和 SSH 代理转发应能正常工作，你将能够在 VSCode 中通过 SSH 连接的远程 Ubuntu 服务器上进行 GPG 签名的 Git 提交。
