---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---
---
zotero-key: RJAJK78V
zt-attachments:
  - "791"
title: Co-clustering by block value decomposition
citekey: long2005CoclusteringBlockValue
---
# Co-clustering by block value decomposition
[Zotero](zotero://select/library/items/RJAJK78V) [attachment](<file:///Users/zihanwu/Zotero/storage/U95TA7PH/Long%20et%20al.%20-%202005%20-%20Co-clustering%20by%20block%20value%20decomposition.pdf>)
> [!note] Page 635
> 
> Dyadic
> 
> ---
> 🔤二元🔤
> ^9I337M8UaU95TA7PHp1
> [!note] Page 635
> 
> intertwining
> 
> ---
> 🔤交织在一起🔤
> ^XGFPA7LYaU95TA7PHp1
> [!note] Page 636
> 
> We are interested in simultaneously clustering X into k disjoint clusters and Y into l disjoint clusters. This is equiv- alent to ﬁnding block structure of the matrix Z, i.e., ﬁnding k × l submatrices of Z such that the elements within each submatrix are similar to each other and elements from different submatrices are dissimilar to each other.
> ^LER3K477aU95TA7PHp2
> [!note] Page 636
> 
> In the traditional one-way clustering, given the cluster centers and the weights that denote degrees of observations associated with their clusters, one can approximate the original data by linear combinations of the cluster centers. Similarly, we should be able to ”reconstruct” the original data matrix by the linear combinations of the block centers.
> 
> ---
> 和传统聚类类似，可以这么理解。
> 传统：每个element可以表示为聚类中心的线性表示
> co-clustering: $Z \sim RBC$, B就像聚类中心
> ^66H3G3EHaU95TA7PHp2
> [!note] Page 637
> 
> Under the BVD framework, the combinations of the components also have an intuitive interpretation. RB is the matrix containing the basis for the column space of Z and BC contains the basis for the row space of Z. For example, for a word-by-document matrix Z, each column of RB captures a base topic of a particular document cluster and each row of BC captures a base topic of a word cluster.
> 
> ---
> 在文本数据集中，矩阵分解的意义。
> ^5G5X7V89aU95TA7PHp3
> [!note] Page 637
> 
> Comparing with SVD-based approaches, there are two main diﬀerences between BVD and SVD.
> 
> ---
> 🔤与基于 SVD 的方法相比，BVD 和 SVD 之间有两个主要区别。🔤
> 1. 求和更有意义
> 2. 基向量方向和cluster联系更紧密
> 都是可解释性上的区别
> ^NRPLVT7IaU95TA7PHp3
> [!note] Page 637
> 
> The objective function in (2) is convex in R, B and C respectively. However, it is not convex in all of them simultaneously. Thus, it is unrealistic to expect an algorithm to ﬁnd the global minimum. We derive an EM [1] style algorithm that converges to a local minimum by iteratively updating the decomposition using a set of multiplicative updating rules.
> 
> ---
> 使用iterative方法的原因
> ^8G9ZT6VCaU95TA7PHp3
> [!note] Page 638
> 
> Deﬁnition 3.
> 
> ---
> 对称情况
> ^XHQ8JH3YaU95TA7PHp4
> [!note] Page 638
> 
> Data Sets and Parameter Settings
> 
> ---
> 我们使用20新闻组数据集(NG20)和CLASSIC3数据集的各种子集来进行性能评估。NG20数据集包含来自20个不同新闻组的大约20,000篇新闻组文章。我们完全复制了也被\ [8, 10\]用于文档共聚类的数据集,以确保评估中的可直接比较性。许多新闻组共享相似的主题,大约4.5%的文档被交叉发布,使得某些新闻组之间的界限相当模糊。为了使我们的比较与现有算法一致,我们重建了\ [8, 10\]中使用的NG20的各种子集,即删除停用词,忽略文件头并根据互信息选择前2000个词。与\ [10\]中一样,我们在文章中包含主题行。子集的具体细节如表1所示。由于每个词-文档矩阵的文档向量被归一化为单位L2范数,在NBVD的实现中,我们归一化了RB的每一列以获得单位L2范数。假设RB被归一化为RBV。文档的聚类标签由V−1C给出,而不是C。我们使用混淆矩阵的准确度来衡量聚类性能,混淆矩阵由获得的聚类和“真实”类给出。混淆矩阵中的每个条目(i,j)表示聚类i中属于真实类j的文档数量。具体而言,我们使用微平均精度。
> 
> 
> 主要思路为:
> - 使用 20 新闻组数据集等进行评估
> - 对数据集进行预处理(移除停用词等)以保证可比性
> - 使用混淆矩阵和微平均精度评测聚类性能
> ^LDN4ETKJaU95TA7PHp4
> [!note] Page 638
> 
> Experiment on Word-Document Data
> 
> ---
> 这一部分提供了实证证据，以展示作为一种通用的共聚类算法，NBVD如何在与NMF[6]以及另外两种共聚类算法——信息论共聚类（ICC）[8]和迭代双重聚类算法（IDC）[10]相比较时，提高了文档聚类的准确性。在实验中，初始矩阵按以下方式生成：R和C的所有元素都是从0到1的均匀分布中生成的，而B的所有元素则简单地赋值为数据矩阵的平均值。由于NBVD算法无法保证找到全局最小值，因此多次运行该算法并使用不同的初始值，选择目标值最小的一次试验是有益的。实际上，通常几次试验就足够了。在本文报道的实验中，每个测试运行中进行了三次NBVD试验，最终结果是二十次测试运行的平均值。NMF的实验也以同样的方式进行。表2记录了在CLASSIC3数据集上使用NMF和NBVD分别获得的两个混淆矩阵，其中包含3个单词簇，即真实单词簇的数量。观察到NBVD以0.9879的微平均精度提取了原始簇，而NMF的微平均精度为0.9866。NBVD和NMF在CLASSIC3数据集上表现几乎相同并不令人惊讶。这是因为当行簇和列簇之间存在完美的一对一对应时，块值矩阵B接近于单位矩阵，NMF等同于NBVD。表3显示了数据集CLASSIC3的一个块值矩阵。表3的完美对角结构表明了CLASSIC3的文档簇和单词簇之间的一对一对应结构。表4显示了在Multi5数据集上NBVD和NMF分别获得的两个混淆矩阵。NBVD和NMF分别产生了0.944和0.884的微平均精度。这个实验表明，在Multi5数据集上，NBVD的性能优于NMF。与CLASSIC3相比，Multi5具有更复杂的隐藏块结构，文档簇和单词簇之间没有简单的一对一关系。这表明，通过利用行聚类和列聚类的双重性，NBVD比NMF更有能力发现数据的复杂隐藏块结构。表5显示了在所有NG20数据集上的微平均精度测量结果。所有NBVD的精度值都是通过在真实文档簇的数量和通过额外实验找到的相应最佳单词簇数量上运行NBVD获得的，这些额外实验评估了在不同数量的单词簇下的精度（由于空间限制，细节省略）。引用自[8]和[10]的ITC和IDC的峰值精度值。在所有数据集上，NBVD的表现都优于其单边对应的NMF。这个结果证明了需要利用单词聚类和文档聚类之间的双重性。与另外两种最新的共聚类算法相比，NBVD在几乎所有数据集上的精度都有明显的提高。特别是在具有更多簇的复杂数据集上观察到了更大的改进，这是实践中的典型场景。
> ^3NHK2PAJaU95TA7PHp4
# Basic Information:
- Title: Co-clustering by Block Value Decomposition (块值分解的共聚类)
- Authors: Bo Long, Zhongfei (Mark) Zhang, Philip S. Yu
- Affiliation: Computer Science Dept., SUNY Binghamton (纽约州立大学宾汉姆顿分校计算机科学系)
- Keywords: Co-clustering, Clustering, Matrix Decomposition, Dyadic Data, Hidden Block Structure, Block Value Decomposition (BVD)
- URLs: [Paper](https://chatwithpaper.org/link_to_paper), [GitHub: None]
# 论文简要 :
- 本文提出了一种新的共聚类框架，即块值分解（BVD），用于处理二维数据矩阵的隐藏块结构，提出了一种特定的共聚类算法，针对非负二元数据，通过迭代计算三个分解矩阵，证明了算法的收敛性，并进行了广泛的实验评估，展示了该框架及算法的有效性和潜力。
# 背景信息:
- 论文背景: 共聚类在许多领域中都有广泛的应用，而对于二维数据矩阵，共聚类通常比传统的单向聚类更加理想。
- 过去方案: 大多数聚类文献侧重于单边聚类算法，但最近共聚类因其在基因表达数据分析和文本挖掘等问题中的应用而受到广泛关注。
- 论文的Motivation: 共聚类能够更有效地处理高维稀疏数据，并且能够同时提供行聚类和列聚类，因此在许多应用中更为理想。作者提出了块值分解（BVD）框架，旨在探索二维二元数据矩阵中的潜在块结构，通过三个分解矩阵来实现对原始数据矩阵的重构。
# 方法:
- a. 理论背景:
    - 本文介绍了一种新的用于二元数据的共聚类框架，称为块值分解（Block Value Decomposition，BVD）。该框架将二元数据矩阵分解为三个部分：行系数矩阵R，块值矩阵B和列系数矩阵C。提出的共聚类算法基于乘法更新规则迭代计算这三个分解矩阵。算法通过在每次迭代中交织行聚类和列聚类来进行隐式自适应降维。通过广泛的实验评估，证明了该框架和算法的有效性。
- b. 技术路线:
    - 本文描述了非负块值分解（Non-negative Block Value Decomposition，NBVD）算法及其特殊情况下的对称非负块值分解。NBVD算法旨在最小化目标函数，同时对矩阵R、B和C施加非负约束。算法涉及对R、B和C的迭代更新规则，时间复杂度为O(t(k + l)nm)，其中t是迭代次数。文本还介绍了局部最小值的必要条件以及对称NBVD特殊情况下的更新规则。
# 结果:
- a. 详细的实验设置:
    - 使用20-Newsgroup数据集（NG20）和CLASSIC3数据集进行性能评估。
    - NG20数据集包含约20,000篇从20个不同的Usenet新闻组收集的新闻文章。
    - 为了与现有算法进行比较，使用各种NG20的子集进行重构。
    - 子集是通过去除停用词、忽略文件头部，并基于互信息选择前2000个词语来创建的。
    - 文章的主题行包含在内。
    - 文档向量被归一化为单位L2范数。
    - 使用混淆矩阵给出的准确率来衡量聚类性能，并使用微平均精度作为度量指标。
    - 使用NBVD算法以及NMF、ICC和IDC算法进行比较，对单词-文档数据进行聚类。
    - 使用均匀分布在0到1之间生成初始矩阵。
    - NBVD算法在不同的初始值下运行多次，找到目标值最小的试验。
    - 每次测试运行中进行三次NBVD试验，最终结果取二十次测试运行的平均值。
    - 实验结果显示，与NMF、ICC和IDC算法相比，NBVD提高了文档聚类的准确性。
    - 实验还表明，NBVD在具有更多聚类的数据集上表现更好。
    - 还进行了接近度数据的实验，以展示对称NBVD算法在图分区上的潜力。
    - 与平均关联（AA）和归一化割（NC）方法相比，对称NBVD算法表现出更好的性能。
    - 实验使用与之前相同的预处理步骤的NG20数据集。
    - 文档的接近度矩阵确定为W = ZT Z，其中Z是单词-文档共现矩阵。
    - 使用余弦相似度衡量文档之间的相似性。
    - 使用微平均精度作为度量指标。
    - 对称NBVD算法在每次测试运行中进行3次试验。
    - 性能结果显示，对称NBVD算法在图分区问题上优于AA和NC方法。
# Note:
- 本总结源自于LLM的总结，请注意数据判别. Power by ChatPaper. End.
