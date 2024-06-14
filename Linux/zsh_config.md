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

# And then add them to "~/.zshrc" file
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
```

## powerlevel10k

```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

And then add `ZSH_THEME="powerlevel10k/powerlevel10k"` to `~/.zshrc`.
