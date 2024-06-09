# Use virtual X server to use xclip (CentOS)

## Install Xvfb

```bash
sudo yum install xorg-x11-server-Xvfb
sudo mkdir -p /tmp/.X11-unix && sudo chmod 1777 /tmp/.X11-unix # Create X11 socket directory
Xvfb :99 -screen 0 1024x768x16 &
export DISPLAY=:99
```

## Install xclip

```bash
sudo yum install xclip
```

## Use xclip

```bash
echo "Hello, world" | xclip -selection clipboard
```

## ImageMagick to take screenshot

```bash
sudo yum install ImageMagick
sudo yum install xdotool
import -window "$(xdotool search --onlyvisible --name xterm | head -n 1)" screenshot.png
```
