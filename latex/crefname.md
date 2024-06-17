# LaTeX 自定义 Lemma 引用及计数器使用指南

在 LaTeX 中，如果希望引用 `lemma` 环境并且使用计数器，同时确保在引用时显示为“Lemma”而不是“Theorem”，可以按照以下步骤操作：

## 步骤 1：定义定理环境

首先，定义定理环境，并确保 `lemma` 环境继承 `theorem` 的计数器：

```latex
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma} % 继承 theorem 的计数器
\newtheorem{definition}[theorem]{Definition}
\newtheorem{assumption}[theorem]{Assumption}
```

**注意**: `\newtheorem{lemma}[theorem]{Lemma}` 中的 `[theorem]` 是导致 `crefname` 没有更新的元凶。这意味着 `lemma` 使用了 `theorem` 的计数器，这会让 `cleveref` 误认为 `lemma` 是 `theorem`。

## 步骤 2：加载所需包

加载 `hyperref` 和 `cleveref` 包，并自定义引用名称：

```latex
% 先加载 hyperref
\usepackage{hyperref}

% 然后加载 cleveref 包
\usepackage{cleveref}

% 自定义引用名称
\crefname{theorem}{Theorem}{Theorems}
\Crefname{theorem}{Theorem}{Theorems}

\crefname{lemma}{Lemma}{Lemmas}
\Crefname{lemma}{Lemma}{Lemmas}

\crefname{definition}{Definition}{Definitions}
\Crefname{definition}{Definition}{Definitions}

\crefname{assumption}{Assumption}{Assumptions}
\Crefname{assumption}{Assumption}{Assumptions}
```

## 步骤 3：自定义引用命令

为了确保引用 `lemma` 时显示为“Lemma”而不是“Theorem”，可以创建一个自定义的引用命令：

```latex
% 自定义 Lemma 引用命令
\newcommand{\lemmaref}[1]{Lemma~\ref{#1}}
```

## 步骤 4：修复 crefname 问题

如果希望继续使用 `theorem` 的计数器但引用名称正确，可以通过以下步骤操作：

```latex
\usepackage{aliascnt}

% 定理环境的定义
\newtheorem{theorem}{Theorem}

% 通过 aliascnt 包创建新的 lemma 环境，并继承 theorem 的计数器
\newaliascnt{lemma}{theorem}
\newtheorem{lemma}[lemma]{Lemma}
\aliascntresetthe{lemma}

% 定义 cleveref 的引用名称
\crefname{theorem}{Theorem}{Theorems}
\Crefname{theorem}{Theorem}{Theorems}
\crefname{lemma}{Lemma}{Lemmas}
\Crefname{lemma}{Lemma}{Lemmas}
```

## 步骤 5：示例代码

以下是一个完整的示例代码，演示如何实现这一目标：

```latex
\documentclass{article}

% 其他需要的包
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{hyperref}
\usepackage{cleveref}
\usepackage{aliascnt}

% 定理环境的定义
\newtheorem{theorem}{Theorem}

% 通过 aliascnt 包创建新的 lemma 环境，并继承 theorem 的计数器
\newaliascnt{lemma}{theorem}
\newtheorem{lemma}[lemma]{Lemma}
\aliascntresetthe{lemma}

% 定义 cleveref 的引用名称
\crefname{theorem}{Theorem}{Theorems}
\Crefname{theorem}{Theorem}{Theorems}
\crefname{lemma}{Lemma}{Lemmas}
\Crefname{lemma}{Lemma}{Lemmas}

% 自定义 Lemma 引用命令
\newcommand{\lemmaref}[1]{Lemma~\ref{#1}}

\begin{document}

\begin{lemma}[Joint Probability of Co-cluster Size]
  \label{lem:joint_probability}
  Let $C_k$ be a co-cluster and $B_{(i,j)}$ be a block in the partitioned matrix. The probability that the size of the co-cluster $C_k$ within block $B_{(i,j)}$ is less than $T_m$ rows and $T_n$ columns is given by:
  \begin{aligned*}
    P(M_{(i,j)}^{(k)} < T_m, N_{(i,j)}^{(k)} < T_n) & \le \exp[-2 (s_i^{(k)})^2 \phi_i -2 (t_j^{(k)})^2 \psi_j]
  \end{aligned*}
  where $s_i^{(k)} = \cfrac{M^{(k)}}{M}-\cfrac{T_m-1}{\phi_i}$ and $t_j^{(k)} = \cfrac{N^{(k)}}{N}-\cfrac{T_n-1}{\psi_j}$.
\end{lemma}

In the scenario where the matrix $A$ is partitioned into $m \times n$ blocks, each block has size $\phi_i \times $\psi_j$, that is, $M=\sum_{i=1}^m \phi_i$ and $N=\sum_{j=1}^n \psi_j$, the joint probability of $M_{(i,j)}^{(k)}$ and $N_{(i,j)}^{(k)}$ is given by \lemmaref{lem:joint_probability}.

\end{document}
```

通过以上步骤，您可以确保在引用 `lemma` 时显示为“Lemma”而不是“Theorem”，同时保持计数器的一致性。
