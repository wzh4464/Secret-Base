---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---
# Git 中文乱码
`git config --global core.quotepath false`
这个命令告诉 Git 不要对非 ASCII 文件名进行编码，而是直接显示它们。这通常可以解决中文文件名显示为乱码的问题。
