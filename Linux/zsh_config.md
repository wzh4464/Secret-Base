---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---
# zsh config

## Install zsh

```bash
sudo apt install zsh
```

## oh-my-zsh

```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

## plugins

```bash
# Assuming you have git installed
# If not, simply do "sudo yum install git -y"
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/matthiasha/zsh-uv-env ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-uv-env
# And then add them to "~/.zshrc" file
plugins=(git zsh-autosuggestions zsh-syntax-highlighting zsh-uv-env)
```

## powerlevel10k

```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

And then add `ZSH_THEME="powerlevel10k/powerlevel10k"` to `~/.zshrc`.

## 优化 Powerlevel10k Python 虚拟环境显示

在使用 Powerlevel10k 主题时，默认的 Python 虚拟环境（pyenv）显示方式有时不够灵活，特别是在不同目录下切换虚拟环境时，显示内容可能不如预期。为此，可以通过自定义 `POWERLEVEL9K_PYENV_CONTENT_EXPANSION` 变量，优化虚拟环境的显示效果。

### 推荐配置

在你的 zsh 配置文件（如 `.zshrc`）中加入如下内容：

```zsh
typeset -g POWERLEVEL9K_PYENV_CONTENT_EXPANSION='${${VIRTUAL_ENV:#$PWD/*}:-${VIRTUAL_ENV:t}}${${VIRTUAL_ENV:#$PWD/*}:+${VIRTUAL_ENV}} ${P9K_CONTENT:+($P9K_CONTENT)}'
```

### 配置详解

- `${VIRTUAL_ENV}`：当前激活的 Python 虚拟环境路径。
- `${VIRTUAL_ENV:t}`：取虚拟环境路径的最后一段（即虚拟环境名）。
- `${VIRTUAL_ENV:#$PWD/*}`：判断虚拟环境路径是否在当前目录下。
- `${P9K_CONTENT}`：Powerlevel10k 主题的内容变量。

这条配置的作用是：
- 如果虚拟环境在当前目录下，只显示虚拟环境名；
- 如果虚拟环境不在当前目录下，显示完整路径；
- 如果有额外内容（如 pyenv 版本），则在后面加括号显示。

### 效果展示

- 当前目录下的虚拟环境：  
  `(.venv)`
- 全局虚拟环境或其他路径：  
  `/Users/xxx/.pyenv/versions/xxx`
- 带有额外内容时：  
  `(.venv) (3.10.12)`

### 总结

通过自定义 `POWERLEVEL9K_PYENV_CONTENT_EXPANSION`，可以让 Powerlevel10k 更智能地显示 Python 虚拟环境信息，提升命令行体验。建议所有经常切换 Python 虚拟环境的用户都进行此项配置。
