---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---
# Fine-tuning
## Problem
Original problem notation:
- $D = \{ (x_i, y_i) \}_{i=1}^n$ is a dataset of $n$ samples
- $f_{\theta}(x)$ is a model with parameters $\theta$
- $L(f_{\theta}(x), y)$ is a loss function
- $\theta^*$ is the optimal parameter
- $\mathcal{L}(\theta) = \frac{1}{|D|} \sum_{(x, y) \in D} L(f_{\theta}(x), y)$ is the empirical risk
- $\theta^* = \arg \min_{\theta} \mathcal{L}(\theta) = \arg \min_{\theta} |D| \mathcal{L}(\theta) = \arg \min_{\theta} \sum_{(x, y) \in D} L(f_{\theta}(x), y)$
Fine-tuning problem:
- $D_f = \{ (x_i, y_i) \}_{i=1}^m$ is a dataset of $m$ samples, where $m \ll n$
- Fine-tuning loss function: $\mathcal{L}_f(\theta) = \frac{1}{|D_f|} \sum_{(x, y) \in D_f} L(f_{\theta}(x), y)$
原来的loss function: $\mathcal{L}(\theta) = \frac{1}{|D|} \sum_{(x, y) \in D} L(f_{\theta}(x), y)$, 新的loss function: $\mathcal{L}_f(\theta) = \frac{1}{|D_f| + |D|} \sum_{(x, y) \in D_f \cup D} L(f_{\theta}(x), y)$
