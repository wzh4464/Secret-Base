# Runpod setup

## Change HOME

```bash
export HOME=/workspace/
```

## ssh key

```bash
mkdir .ssh
ssh-keygen -t ed25519 -C "32484940+wzh4464@users.noreply.github.com"
```

And add the public key to github.

## git config

```bash
git config --global user.email "32484940+wzh4464@users.noreply.github.com"
git config --global user.name "wzh4464"
```

## zsh

```bash
apt-get update
apt-get install zsh
# chsh -s /bin/usr/zsh not work, need password
```

## oh-my-zsh

```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

## Webdav

```bash
cadaver http://dav.jianguoyun.com/dav
```

```bash
zihanwu7@icloud.com
```

```bash
get filename
```

## two git account

```config
# GitHub account1
Host github.com-user1
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_github1
    IdentitiesOnly yes

# GitHub account2
Host github.com-user2
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_github2
    IdentitiesOnly yes
```
