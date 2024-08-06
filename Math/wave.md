---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---

# Wave

- Stand wave: $y(x,t) = \phi(t) \psi(x)$, 波形不随时间移动(波腹和波谷不移动)
- Traveling wave: $y(x,t) = \phi(x \pm vt)$, 波形随时间移动(波腹和波谷移动)

## Wave Equation

### 一维波动方程

$$\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}$$

基于的假设: 受到的是两侧的力, 且满足胡克定律

### d’Alembert’s formula (行波解)

边界条件:

$$
\begin{split}
  y(x,0) = f(x) \\ \frac{\partial y}{\partial t}(x,0) = g(x)
\end{split}
$$

解:

$$
y(x,t) = \frac{1}{2}[f(x+vt) + f(x-vt)] + \frac{1}{2v} \int_{x-vt}^{x+vt} g(\xi) d\xi
$$

### 驻波解

$$
\begin{split}
  \phi(x)'' = -k^2 \phi(x) \\
  \psi(t)'' = -k^2 \psi(t) \\
  y_k(x,t) = (A_k \cos kt + B_k \sin kt)\sin kx
\end{split}
$$

### 引出问题

**Question:** Given any reasonable function \( F \) on \([- \pi, \pi]\), with Fourier coefficients defined above, is it true that

$$
F(x) = \sum_{m = - \infty}^{\infty} a_m e^{imx}?
$$
