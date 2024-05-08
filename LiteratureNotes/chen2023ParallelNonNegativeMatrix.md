---
zotero-key: QZHFCPF4
zt-attachments:
  - "6068"
title: Parallel non-negative matrix tri-factorization for text data co-clustering
citekey: chen2023ParallelNonnegativeMatrix
---
# Parallel non-negative matrix tri-factorization for text data co-clustering

[Zotero](zotero://select/library/items/QZHFCPF4) [attachment](<file:///Users/zihanwu/Zotero/storage/SRL3WQQ7/Chen%20et%20al.%20-%202023%20-%20Parallel%20non-negative%20matrix%20tri-factorization%20for%20text%20data%20co-clustering.pdf>)

> [!note] Page 5132
> 
> incorporates the non-negative constraint to the decomposed low-rank factors
> 
> ---
> 🔤将非负约束纳入分解的低秩因子中🔤
> ^GLXBVS3YaSRL3WQQ7p1

> [!note] Page 5132
> 
> only allows the additive combination for the representation of the original data matrix.
> 
> ---
> 🔤只允许对原始数据矩阵的表示进行加法组合。🔤
> ^7QFLPHSMaSRL3WQQ7p1

> [!note] Page 5132
> 
> leverage the inherent duality between the other two decomposed factors
> 
> ---
> 🔤利用其他两个分解因素之间固有的二元性🔤
> ^GNMXNCHDaSRL3WQQ7p1

> [!note] Page 5132
> 
> intensive matrix multiplications
> ^TZJI7M3VaSRL3WQQ7p1

> [!note] Page 5133
> 
> KKT
> 
> ---
> KKT（Karush-Kuhn-Tucker）条件是一种在数学优化领域广泛使用的方法，特别是在解决带约束条件的非线性优化问题时。它是拉格朗日乘数法的一种推广，用于找到满足某些约束条件的最优解。KKT条件包括了一组必须满足的方程和不等式，它们定义了一个最优解必须符合的条件。
> ^8ELHW2AAaSRL3WQQ7p2

> [!note] Page 5133
> 
> NI
> 
> ---
> 牛顿迭代
> ^MXKN66Q2aSRL3WQQ7p2

> [!note] Page 5132
> 
> 
> 
> ---
> NMTF 作为数据降维的工具，做ML的预处理步骤
> ^PNQSXE6LaSRL3WQQ7p1

> [!note] Page 5132
> 
> 
> 
> ---
> NMTF 的好处和应用
> ^DD2E5HVBaSRL3WQQ7p1

> [!note] Page 5132
> 
> 
> 
> ---
> 现在的不足：速度和 memory和收敛性问题
> ^AWPBFK8NaSRL3WQQ7p1

> [!note] Page 3
> 
> Non-negative Block Value Decomposition proposed by Long et al. [4],
> 
> ---
> First NMF
> ^6VUXSMHMaSRL3WQQ7p3

> [!note] Page 3
> 
> block value matrix
> ^98F5TAMMaSRL3WQQ7p3

> [!note] Page 3
> 
> For the sake of facilitation
> 
> ---
> 为了便利
> ^APY86YYVaSRL3WQQ7p3

> [!note] Page 4
> 
> The factor ZZ denotes the document cluster indicator matrix, where Zij corresponds to the degree of the ith document belonging to the jth document cluster. Similarly, the factor WW denotes the word cluster indicator matrix. The factor SS provides additional degrees of freedom such that the low-rank matrix representation remains accurate, and it also represents the association between word clusters and document clusters.
> 
> ---
> meaning of ZSW (svd can use)
> ^XUEE4HBBaSRL3WQQ7p4

> [!note] Page 7
> 
> comparison of the text data co-clustering results obtained by different models on several real-world datasets
> ^YV7KRTE8aSRL3WQQ7p7

> [!note] Page 7
> 
> evaluate the computational performance of our
> ^DTSTCJ2NaSRL3WQQ7p7

> [!note] Page 8
> 
> PNMTF, including
> ^S52HVC2NaSRL3WQQ7p8

> [!note] Page 8
> 
> convergence trend
> ^5748R48KaSRL3WQQ7p8

> [!note] Page 8
> 
> average running time
> ^8CE5BI2KaSRL3WQQ7p8

> [!note] Page 8
> 
> scalability
> ^XLHZWBAQaSRL3WQQ7p8

> [!note] Page 8
> 
> FNMTF and BKM were developed for large-scale data co-clustering by constraining the factor matrices as binary-valued cluster indicator matrices
> ^67CEU3T3aSRL3WQQ7p8

> [!note] Page 8
> 
> one-sided clustering method, Spherical k-means (Skmeans)
> ^ZC736HJMaSRL3WQQ7p8

> [!note] Page 8
> 
> DeepCC, we use the ofﬁcial open-sourced implementation in [41]
> ^2HWDFUU8aSRL3WQQ7p8

> [!note] Page 8
> 
> For all methods, the number of document clusters J1 is set to the real number of clusters corresponding to each dataset.
> 
> ---
> Use number from ground-truth as super parameter
> ^Y8F46URDaSRL3WQQ7p8

> [!note] Page 9
> 
> document clusters
> ^X8TKM8G8aSRL3WQQ7p9

> [!note] Page 9
> 
> word clustering evaluation
> ^HLWK7Z4QaSRL3WQQ7p9

> [!note] Page 9
> 
> coherence scores
> ^NNG76KS7aSRL3WQQ7p9

> [!note] Page 9
> 
> Clustering Performance Analysis
> 
> ---
> <b>实验设计</b>：所有方法均进行了10次独立运行，以记录不同随机初始化下的收敛结果。在文档聚类结果分析中，使用NMI（归一化互信息）和ARI（调整兰德指数）来评估各方法与真实标签的匹配度。某些方法由于数据集规模或计算资源限制无法进行评估（如DeepCC方法在某些数据集上耗时过长或内存不足）。<b>文档聚类结果分析</b>：Skmeans方法在小数据集上的文档聚类效果较好，但在大数据集上表现不佳。NMTF（非负矩阵三分解）基方法在大数据集上更健壮。PNMTF在不同数据集上表现各异，但在某些数据集上（如Amazon和RCV1-Small）的文档聚类方面表现出色。<b>词聚类结果分析</b>：由于缺乏词的真实标签，评估词聚类质量具有挑战性。评估词聚类的解释性，通过计算一致性得分（如CUMass、CV、CUCI和CNPMI）来实现。特定方法（如FNMTF、BKM和CoclustInfo）无法计算词聚类的一致性得分。<b>性能比较</b>：通过t检验统计评估了PNMTF与每个基线模型之间的性能差异。在较大的数据集（如NG20、Amazon和RCV1-Small）上，PNMTF在文档聚类方面相较于其他基线模型表现出显著优势。<b>方法间权衡</b>：观察到文档聚类和词聚类之间存在一定的性能权衡。例如，WCNMTF和PenNMTF在文档聚类方面表现一般，但在词聚类方面表现更好。<b>PNMTF和NMTF的比较</b>：在大多数情况下，PNMTF与NMTF的共聚类性能差异不显著。PNMTF在特定情况下（如Amazon数据集上的CUMass）表现不佳，但在其他方面（如NG20和Amazon数据集上的CNPMI）表现出色。总的来说，这部分内容展示了PNMTF方法在不同数据集上的文档聚类和词聚类性能，并与其他方法进行了比较。结果显示，PNMTF在大规模文本数据的文档聚类方面具有高度适应性，并在大多数情况下与NMTF的性能一致。
> ^S6TVXF3RaSRL3WQQ7p9

> [!note] Page 9
> 
> Since the document-word matrix of the RCV1-Large dataset is too large to be stored and processed by all baselines which are not scalable and required to be run in a single machine, we only present the results of our PNMTF on this dataset to show its scalability.
> 
> ---
> 由于RCV1-Large数据集的文档-词矩阵太大,无法存储和处理所有基线,这些基线不可扩展并且需要在单台机器上运行,我们只在这个数据集上呈现我们的PNMTF的结果,以展示其可扩展性。
> ^N6VEELL6aSRL3WQQ7p9

> [!note] Page 10
> 
> It is also noteworthy that FNMTF, BKM, and CoclustInfo perform hard clustering with the word cluster indicator taking a binary value, thus the coherence scores in word clustering can not be computed for these methods.
> 
> ---
> 特定方法（如FNMTF、BKM和CoclustInfo）无法计算词聚类的一致性得分。
> ^KZTJ77U2aSRL3WQQ7p10

> [!note] Page 10
> 
> t-tests
> ^EKPIBFJ3aSRL3WQQ7p10

> [!note] Page 10
> 
> 
> 
> ---
> 分析实验结果部分，各结果优缺点
> ^L5BLZL8WaSRL3WQQ7p10

> [!note] Page 10
> 
> 
> 
> ---
> 我可以说一点sparsity
> ^D56L3FULaSRL3WQQ7p10

> [!note] Page 11
> 
> The above results indicate that all of those constrained baseline methods show their weaknesses in various aspects. Besides, it appears that there is a performance trade-off between document clustering and word clustering to some extent.
> ^UTPYXYMCaSRL3WQQ7p11

> [!note] Page 11
> 
> asymptotic
> 
> ---
> 漸進
> ^YT596YRBaSRL3WQQ7p11
