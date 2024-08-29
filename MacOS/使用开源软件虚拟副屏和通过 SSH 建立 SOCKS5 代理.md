---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---

# 使用开源软件虚拟副屏和通过 SSH 建立 SOCKS5 代理

## 虚拟副屏连接 iPad

在本地设备上，你可以使用以下两个开源软件轻松地虚拟出副屏，并连接到 iPad：

1. **Deskreen**
   - 通过浏览器将 Mac 屏幕的内容共享到任何支持浏览器的设备上（如 iPad）。
   - 支持局域网内的有线或无线连接。
   - 开源、免费，易于使用。

2. **BetterDummy**
   - 在 macOS 上创建虚拟显示器，将其映射为虚拟屏幕。
   - 与 Deskreen 结合使用，可以将虚拟屏幕内容传输到 iPad 等外部设备上。
   - 开源、简单设置，不需要额外的硬件支持。

### 使用步骤

1. 使用 BetterDummy 在 macOS 上创建一个虚拟显示器。
2. 通过 Deskreen 将虚拟显示器内容共享到 iPad。

## 通过 SSH 建立 SOCKS5 代理

由于本地已经有了端口转发，可以轻松通过 SSH 建立 SOCKS5 代理。

### 简单命令

```bash
ssh -D 1080 zihan_gpu
```
