---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---
# 矩阵的trace

## Preliminary

### 行列式求导 (Jacobi's formula)
<!--$$\frac{d}{dt} \det(A) = \det(A) \text{tr}(A^{-1} \frac{dA}{dt})$$-->
$$
\frac{\mathrm{d}}{\mathrm{d}t} \det(A) = \det(A) \text{tr}(A^{-1} \frac{\mathrm{d}A}{\mathrm{d}t})
$$
<!-- Note box -->
> **Note:** 证明：
>$$\frac{\partial \det(A)}{\partial a_{ij} } = A_{ij}$$
>$A_{ij}$是$A$的代数余子式
>$$
> \begin{aligned}
> \frac{\mathrm{d}}{\mathrm{d}t} \det(A)&= \sum_{i,j} \frac{\partial}{\partial a_{ij}}  \det(A)\frac{\mathrm{d}a_{ij}}{\mathrm{d}t} \\
> &= \sum_{i,j} A_{ij} \frac{\mathrm{d}a_{ij}}{\mathrm{d}t} = \det(A) \sum_{i,j} A_{ij}/\det(A) \frac{\mathrm{d}a_{ij}}{\mathrm{d}t} \\
> &= \det(A) \text{tr}(A^{-1} \frac{\mathrm{d}A}{\mathrm{d}t})
> \end{aligned}
>$$
>
### 行列式和trace的关系

$$
\det(e^A) = e^{\text{tr}(A)}
$$
<!-- Note box -->
> **Note:** 证明：
> 考虑$e^{tA}$，则
>$$
> \begin{aligned}
> \frac{\mathrm{d}}{\mathrm{d}t} \det(e^{tA}) &= \det(e^{tA}) \text{tr}(e^{-tA} e^{tA} A) \\
> &= \det(e^{tA}) \text{tr}(A) \\
> \end{aligned}
>$$
> 两边积分得到
>$$
> \det(e^{tA}) = Ce^{t\text{tr}(A)}
>$$
> 代入$t=0$得到$C=I$
> 代入$t=1$得到$\det(e^{A}) = e^{\text{tr}(A)}$
>
## 矩阵的trace是面积的变化率(一阶近似)

考虑一个矩阵$A \in \mathbb{R}^{n}$和一个运动
$$
\vec{d}^{i}_t =\vec{d}^{i}_0 + t A \vec{d}^{i}_0
$$
$$
\det(\vec{d}^{1}_t, \vec{d}^{2}_t, \cdots, \vec{d}^{n}_t) = S_t \\
\det(\vec{d}^{1}_0, \vec{d}^{2}_0, \cdots, \vec{d}^{n}_0) = S_0
$$
记$(\vec{d}^{1}_t, \vec{d}^{2}_t, \cdots, \vec{d}^{n}_t)$为$D_t$，$(\vec{d}^{1}_0, \vec{d}^{2}_0, \cdots, \vec{d}^{n}_0)$为$D_0$，则
$$
\begin{aligned}
S_t &= \det(D_0 + t A D_0) \\
&=S_{0} + t \det(D_0) \text{tr}(D_0^{-1} A D_0) + O(t^2) \\
&=S_{0} + t S_{0} \text{tr}(A) + O(t^2)
\end{aligned}
$$

## 对trace求导

$$
\frac{\mathrm{d} \mathbf{tr}(AB)}{\mathrm{d}B} = A^T
$$
<!-- Note box -->
> **Note:** 证明：
>$$
> \begin{aligned}
> \frac{\mathrm{d} \mathbf{tr}(AB)}{\mathrm{d}B} &= \frac{\mathrm{d} a_{ij} b_{ji}}{\mathrm{d}b_{kl}} \\
> &= a_{ij} \delta_{il} \delta_{jk} \\
> &= a_{lk} \\
> &= A^T
> \end{aligned}
>$$
