---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---
# Graph Laplacian
## Definition
The graph Laplacian is a matrix representation of a graph. It is defined as the difference between the degree matrix and the adjacency matrix of the graph.
## Formula
The graph Laplacian of a graph $G$ with $n$ vertices is defined as:
$$
L = D - A
$$
where $D$ is the degree matrix and $A$ is the adjacency matrix of the graph.
## Properties
1. The graph Laplacian is symmetric and positive semi-definite.
2. The smallest eigenvalue of the graph Laplacian is 0, and the corresponding eigenvector is the all-ones vector.
3. $x^TLx = \frac{1}{2} \sum_{i,j} w_{ij} (x_i - x_j)^2$, where $w_{ij}$ is the weight of the edge between vertices $i$ and $j$.
4. L has $n$ non-negative, real-valued eigenvalues $0 = \lambda_1 \leq \lambda_2 \leq \ldots \leq \lambda_n$.
