---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---

# Hessian in DIT: Derivation Steps

1) Starting from equation (10):

$$\theta_{-j}^{[t+1]} - \theta^{[t+1]} = (\theta_{-j}^{[t]} - \theta^{[t]}) - \frac{\eta_t}{|S_t|}(\sum_{i\in S_t\backslash\{j\}} g(z_i; \theta_{-j}^{[t]}) - \sum_{i\in S_t} g(z_i; \theta^{[t]}))
\\ = (\theta_{-j}^{[t]} - \theta^{[t]}) + \frac{\eta_t}{|S_t|}(\mathbf{1}_{j\in S_t}g(z_j; \theta^{[t]}) - \left[\sum_{i\in S_t\backslash\{j\}} g(z_i; \theta^{[t]}) - \sum_{i\in S_t\backslash\{j\}} g(z_i; \theta_{-j}^{[t]})\right])$$

2) Using first-order Taylor expansion from equation (11):

$$g(z_i; \theta_{-j}^{[t]}) - g(z_i; \theta^{[t]}) \approx \nabla_\theta g(z_i; \theta^{[t]})^T(\theta_{-j}^{[t]} - \theta^{[t]})$$

3) Summing all terms:

$$\sum_{i\in S_t\backslash\{j\}} \nabla_\theta g(z_i; \theta^{[t]})^T(\theta_{-j}^{[t]} - \theta^{[t]}) \approx \sum_{i\in S_t\backslash\{j\}} (g(z_i; \theta_{-j}^{[t]}) - g(z_i; \theta^{[t]}))$$

4) Using the Hessian matrix defined in equation (12) and (A4):

$$H^{[t]}(\theta_{-j}^{[t]} - \theta^{[t]}) \approx H_{-j}^{[t]}(\theta_{-j}^{[t]} - \theta^{[t]}) = \frac{1}{|S_t|}\sum_{i\in S_t\backslash\{j\}} \nabla_\theta g(z_i; \theta^{[t]})^T(\theta_{-j}^{[t]} - \theta^{[t]})$$

5) Substituting results from equations (12) and (A4) into equation (10):

$$-\eta_tH^{[t]}(\theta_{-j}^{[t]} - \theta^{[t]}) \approx \frac{\eta_t}{|S_t|} \left[\sum_{i\in S_t\backslash\{j\}} (g(z_i; \theta^{[t]}) - g(z_i; \theta_{-j}^{[t]}))\right]$$

6) Finally, obtaining equation (14):

$$\theta_{-j}^{[t+1]} - \theta^{[t+1]} \approx (I - \eta_t H^{[t]})(\theta_{-j}^{[t]} - \theta^{[t]}) + \mathbf{1}_{j\in S_t}\frac{\eta_t}{|S_t|}g(z_j; \theta^{[t]})$$

Where $$\mathbf{1}_{j\in S_t}$$ is an indicator function that equals 1 when j is in set St and 0 otherwise. This term comes from the separate j term isolated in step 3.
