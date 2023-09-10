# Construction of Ito Intergration

## 1. Idea

Just like the construction of Lebesgue integral, we first define the integral for *elementary* (simple functions), then extend it to the class of where the integral is well-defined.

### Elementary Functions

For a given partition $P = \{t_0, t_1, \cdots, t_n\}$ of $[0, T]$, we define the elementary function $\phi$ as

$$
\phi = \sum_{i=0}^{n-1} e_i(\omega) \chi_{[t_{i}, t_{i+1})}(\omega)
$$

where $e_i$ is a $\mathcal{F}_{t_{i}}$-measurable random variable.

## 2. Ito Isometry

For $\phi$ is an elementary function, we define the Ito integral of $\phi$ as

$$
\int_{S}^{T} \phi(\omega, t) dB_t = \sum_{i=0}^{n-1} e_i(\omega) (B_{t_{i+1}} - B_{t_{i}})
$$

The Ito isometry states that

$$
\mathbb{E} \left[ \left( \int_{S}^{T} \phi(\omega, t) dB_t \right)^2 \right] = \mathbb{E} \left[ \int_{S}^{T} \phi^2(\omega, t) dt \right]
$$

## 3. Ito Integral

### Assesment

Denote the class we want to define the integral as $\mathcal{V}$. Let $\mathcal{V} = \mathcal{V}(S, T)$ be the class of all elementary functions $f(\omega, t): [0, \infty) \times \Omega \rightarrow \mathbb{R}$ such that

1. $f(\omega, t)$ is $\mathcal{B} \times \mathcal{F}$-measurable, where $\mathcal{B}$ is the Borel $\sigma$-algebra on $[0, \infty)$.

2. $f(\omega, t): \omega \mapsto f(\omega, t)$ is $\mathcal{F}_t$-measurable for each $t \geq 0$.

3. $\mathbb{E} \left[ \int_{0}^{\infty} f^2(\omega, t) dt \right] < \infty$.

### Step 1

Handle the bounded and continuous case.

**Lemma 1.** If $f \in \mathcal{V}$ is bounded and continuous, then there exists a sequence of elementary functions $\phi_n \in \mathcal{V}$ such that

$$
\mathbb{E} \left[ \int_{S}^{T} (f(\omega, t) - \phi_n(\omega, t))^2 dt \right] \rightarrow 0
$$

as $n \rightarrow \infty$.

### Step 2

