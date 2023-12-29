通过SSH输入GPG密码通常需要在远程会话中处理GPG命令的密码提示。由于SSH会话可能不会提供标准的密码输入界面，所以需要一些特殊的设置或工具来实现这一点。以下是几种常见方法：

### 1. 使用`gpg-agent`和`pinentry`

`gpg-agent` 是一个用于管理私钥和密码的守护程序，而 `pinentry` 程序用于安全地输入密码。设置它们以在SSH会话中工作：

1. 确保您的GPG配置正在使用 `gpg-agent`。
2. 在您的本地机器上运行 `gpg-agent`，并确保它配置了一个 `pinentry` 程序，该程序能够在SSH会话中弹出密码提示。
3. 在您的 `.bashrc` 或 `.bash_profile` 中添加以下行，以确保远程会话知道如何找到 `gpg-agent`：

   ```bash
   export GPG_TTY=$(tty)
   ```

4. 通过SSH连接到远程机器时，可能需要使用 `-A` 选项来转发代理连接。

### 2. 使用SSH密钥转发

如果您的GPG密钥存储在一个YubiKey或其他硬件令牌上，您可以使用SSH密钥转发功能。这允许您在远程机器上使用连接到本地机器的GPG卡：

1. 确保您的GPG配置正确设置，以使用硬件令牌。
2. 在本地机器上启动 `gpg-agent` 并确保它配置了正确的 `pinentry` 程序。
3. 将以下行添加到您的 `~/.ssh/config` 中：

   ```
   Host remote-host
       ForwardAgent yes
   ```

   其中 `remote-host` 是您想要连接的远程机器的名称。

4. 使用SSH连接到远程机器。

### 3. 使用`expect`脚本

对于不支持`pinentry`的情况，可以使用 `expect` 脚本自动化密码输入。`expect` 是一个程序，用于自动化与其他命令行程序的交互。但请注意，这种方法可能存在安全风险，因为它涉及以明文形式在脚本中存储密码。

```bash
#!/usr/bin/expect

spawn gpg --decrypt yourfile.gpg
expect "Enter passphrase:"
send "yourpassword\r"
interact
```

在使用任何这些方法之前，请考虑您的安全需求和环境。特别是在处理敏感的GPG密钥和密码时，最好选择最安全的方法。通常，使用 `gpg-agent` 和 `pinentry` 提供了一个既方便又相对安全的解决方案。