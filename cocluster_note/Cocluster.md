# Cocluster

## Cocluster History

1. 首次出现: 运用于基因表达数据的聚类算法，Cheng & Church (2000) [^cheng2000BiclusteringExpressionData], 使用方均 residuals 作为度量，找到所有 mannually selected 的 thereshold 以下的子矩阵.

2. Spectral Co-clustering: 该算法使用了一种基于谱聚类的方法，SCC [^dhillon2001CoclusteringDocumentsWordsa]. 该算法 coclusters on word-document matrix, 使用了一个基于谱聚类的方法，它将数据矩阵转换为一个二分图, 最小化边权重来 partition.

于是有了三种：

- Graph theory
- Statistical model
- Matrix factorization

应用有：

- Text mining
- Bioinformatics
- Recommendation system [^vizinepereira2015SimultaneousCoclusteringLearninga]

## 优点

<!-- often clusters are embedded in subspaces comprised of a subset of features, and different features may be relevant for different clusters. Algorithms that operate globally in the feature space fail to discover such local patterns -->

- 与传统聚类算法相比，coclustering 能够发现数据中的子空间，即子矩阵，这些子矩阵可能在不同的特征子集中嵌入，不同的特征可能对不同的聚类有意义。在特征空间中全局操作的算法无法发现这种局部模式。

## Evaluation Score

- variance
- maximum interaction criterion [^bock2016ProbabilisticTwowayClustering]
- mean-square residue [^cheng2000BiclusteringExpressionData]
- scaling mean-square residue [^mukhopadhyay2009NovelCoherenceMeasurec]
- average correlation value [^teng2008DiscoveringBiclustersIterativelyc]

[^cheng2000BiclusteringExpressionData]: Cheng, Y., & Church, G. (2000). Biclustering of Expression Data. Proceedings. International Conference on Intelligent Systems for Molecular Biology. <https://www.cs.princeton.edu/courses/archive/fall03/cs597F/Articles/biclustering_of_expression_data.pdf>
[^dhillon2001CoclusteringDocumentsWordsa]: Dhillon, I. S. (2001). Co-clustering documents and words using bipartite spectral graph partitioning. ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 269–274. <https://doi.org/10.1145/502512.502550>
[^vizinepereira2015SimultaneousCoclusteringLearninga]: Vizine Pereira, A. L., & Hruschka, E. R. (2015). Simultaneous co-clustering and learning to address the cold start problem in recommender systems. Knowledge-Based Systems, 82, 11–19. <https://doi.org/10.1016/j.knosys.2015.02.016>
[^bock2016ProbabilisticTwowayClustering]: Bock, H.-H. (2016). Probabilistic two-way clustering approaches with emphasis on the maximum interaction criterion. <https://doi.org/10.5445/KSP/1000058747/01>
[^mukhopadhyay2009NovelCoherenceMeasurec]: Mukhopadhyay, A., Maulik, U., & Bandyopadhyay, S. (2009). A novel coherence measure for discovering scaling biclusters from gene expression data. Journal of Bioinformatics and Computational Biology, 07(05), 853–868. <https://doi.org/10.1142/S0219720009004370>
[^teng2008DiscoveringBiclustersIterativelyc]: Teng, L., & Chan, L. (2008). Discovering biclusters by iteratively sorting with weighted correlation coefficient in gene expression data. Journal of Signal Processing Systems, 50(3), 267–280. <https://doi.org/10.1007/s11265-007-0121-2>
