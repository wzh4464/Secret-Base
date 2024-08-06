---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---

# Comments from IJMLC

## Reviewer 1

This paper proposes a method based on co-clustering to detect elliptic features efficiently, which is quite different from the existing methods based on arc matching. The thesis has the following problems:

1. The ellipse occlusion of the Datasets selected in the paper is small, so it was suggested to test the performance of the algorithm in Dataset #1. Dataset #1 was collected from Fornaciari et al. and consists of 400 real images;
2. Compare some recent detection algorithms, for example, Arc-support line segments revisited: an efficient high-quality ellipse detection ", etc.
3. The detection speed of the algorithm is not clearly stated;
4. Suggest a list of important intermediate process quantities for the algorithm.

## Reviewer 2

This paper presents a novel ellipse detection method based on global co-clustering. It groups the arcs according to the JS divergence of the probability distribution of ellipses. Experiments show that their method has higher F-measure and fewer invalid or redundant ellipses. The experiment is adequate to prove their statements. Overall, this is an interesting manuscript with novelty.

However, their manuscript has several flaws in terms of logic, rigor, language accuracy, and so on, which need to be addressed through revisions before considering acceptance.

Following are some questions and advice:

1. There is a lack of analysis and statistical data on the actual efficiency of the algorithm in the experiment. From Alg.1, this method requires repeated SVD decomposition, k-means clustering, and PFA calculations, which seem to have high computational complexity. It is best for the author to provide an analysis of time efficiency so that readers can better determine the usage scenarios of this method.
2. The captions of the figures should describe the contents in detail for easier understanding. Fig. 3 should refer to Fig. 2 for the colored arcs. Moreover, the result matrix in Fig. 3 is not explained. What is its relevance and difference to the compatibility matrix? What do the circles/u_1/u_2 mean in Fig. 4?
3. Incomplete sentence in 3.4.2: "...represents the grayscale gradient at pixel p for."
4. In 3.4.1, "...maintaining a data structure Q," what kind of data structure?
5. In 3.5, "We can visualize this as estimating an ellipse distribution for each arc." Give an example of the visualization.
6. In 3.5.1, Eq. 3 needs more explanation. How to get this equation?
7. In 3.5.2, how to calculate the divergence in Eq. 4 in practice? Is it by sampling in the parameter space to get discrete values? What's the computational complexity?
8. Images may contain multiple ellipses. How to determine k in k-means and why?
9. It will be better to add precision and recall values to Table 1 and more visualizations on real-world datasets.
10. The format of the reference is poor. Please carefully check the completeness of the information.

## Reviewer 3

1. The authors may give more clearly the innovation of this work and to explain better why the proposed method outperforms other methods from literature.
2. Computational complexity analysis is missing
3. The authors can measure the performance of the proposed method also using the U2OS cells and NIH3T3 dataset [1,2,3], applying the proposed method on cell segmentation problem. Additionally, you can see the datasets from papers [1-5] that may be compared with the proposed method, if it possible to include more datasets.

> [1] A. Gharipour, A.W.-C. Liew, Segmentation of cell nuclei in fluorescence microscopy images: an integrated framework using level set segmentation and touching-cell splitting, Pattern Recog. 58 (2016) 1–11.
> [2] S. Zafari, T. Eerola, J. Sampo, H. Kälviäinen, H. Haario, Segmentation of overlapping elliptical objects in silhouette images, IEEE Trans. Image Process. 24 (12) (2015) 5942–5952.
> [3] C. Panagiotakis and A. Argyros, “Region-based fitting of overlapping ellipses and its application to cells segmentation,” Image and Vision Computing, vol. 93, p. 103810, 2020.
> [4] C. Panagiotakis and A. Argyros, Parameter-free Modelling of 2D Shapes with Ellipses, Pattern Recognition, vol. 53, pp. 259-275, 2016.
> [5]  Zou, T., Pan, T., Taylor, M., & Stern, H. (2021). Recognition of overlapping elliptical objects in a binary image. Pattern Analysis and Applications, 24(3), 1193-1206.

4. In the Evaluation metrics of experimental results, you can also include interaction over union (IoU) metric or F1-measure that can be measured in the segmentation image without using thresholds.

## Reviewer 4

### Strengths  of the paper

- The author proposes a novel method for detecting ellipses based on co-clustering, using a global approach to address challenges related to occlusion, overlap, and noise.
- The method framework is described clearly.
- Remarked the Prasad+dataset and created a new dataset, Prasad++.

### Weaknesses  of the paper

- There are only three experimental comparison methods, and two are relatively old. It is recommended to compare the method with methods from recent years.
- There are four quantitative indicators in the synthetic dataset, but only one of the quantitative indicators in the real-world dataset is provided.

## Reviewer 5

In this paper, the problem of ellipse detection in images is investigated. The aim of the proposed methodology is to incorporate both local geometric properties and global arc relationships in order to address problems such as the presence of noise, occlusions, overlaps, gaps, etc. More specifically, effective ellipse detection is pursued by employing a co-clustering algorithm to  successfully address the problem of occlusions and overlaps between ellipses, while a PFA (Probability of False Alarm) procedure is proposed to minimize false positive detections due to noise and other image imperfections. The proposed methodology is general, as it is applicable to both synthetic and real-world images.

The first two Sections of the paper are quite well-written and informative for the reader regarding the various sub-problems that exist in the general problem of ellipse detection. However, Section 3 is quite difficult to read. Specifically:

- It includes extensive references to theory known from the literature. Indicatively, a large part of Section 3.2, mainly on page 8, refers to extensive details about the SVD method, which is a well-known method.
Sections 3.5.2 and 3.5.3 also refer to known facts about Kullback-Leibler Divergence and Jensen-Shannon Divergence. Section 3.7, where extensive interpretation of Algorithm 1 on page 15 is given, is also unnecessary.
- Sections 3.4.1 and 3.4.2 present a very detailed part of [10], which is part of the proposed methodology. In the second paragraph of Section 3.4 it is stated: "We adopt the arc extraction technique presented in [10] ...", but immediately below it states "The candidate generation step in our arc extraction procedure..." and "Our arc detection procedure can be broken down into two main steps:...". In my opinion, the word "our" in these two sentences is confusing and should be omitted.
- There are multiple definitions of the same thing. For example, in Section 3.3, Section 3.4.1, and Section 3.5.1, the image I is defined in exactly the same way.
- Confusion is created with the use of terminology and the same symbol is used for different things. For example, Table A is referred to on page 6 as feature matrix, on page 8 as data matrix, and on page 13 as compatibility matrix.

Another concern is related to the novelty of the work. The core of the co-clustering algorithm presented in the 4 steps on page 14, where a matrix is factorized using the SVD method and an attempt is made to extract the clusters in the transformed space, is not an unknown idea in Pattern Recognition problems where segmentation, subspace clustering, etc. are required. Also, the methodology of [10], which is also part of the proposed methodology, is quite strong and it should be highlighted how difficult the problem of ellipse detection is after the extraction of the arc candidates, using [10]. In this direction, some helpful diagrams would be useful where the arc candidates would be visualized, as they are extracted from [10].
Additional Observations:

1) It would be helpful to number all of the equations in the paper. This would make it easier for readers to refer to specific equations when discussing the paper.
2) The minimization constraints in the equations for S_row and S_col on page 8 should be updated to explicitly indicate that the minimization should be performed with respect to i_1 and j_1.
3) The phrase "to enhance ellipse detection, including using the Hough transform..." in Section 2.3 on page 4 could be corrected.
4) Please, create a detailed technical pipeline to further clarify the methodology. This pipeline could be presented alongside the more general pipeline shown in Figure 5.
The suggested format for the technical pipeline is:
Arc Candidates extraction using [10] → Probability extraction for each arc to belong to an ellipse → Compatibility matrix extraction, with elements representing Jensen-Shannon Divergence between ellipses → Co-clustering of compatibility matrix elements.

Overall, I believe that the paper needs many changes and is not ready for publication in such a high-impact journal.

## 翻译

# 国际机器学习与计算学报 (IJMLC) 审稿意见

## 审稿人1

本文提出了一种基于共聚类的方法，用于高效地检测椭圆特征，这与现有的基于弧匹配的方法有很大不同。论文存在以下问题：

1. 论文中选择的数据集椭圆遮挡较少，建议在数据集#1中测试算法性能。数据集#1来自Fornaciari等人，包含400张真实图像；
2. 需要比较一些最新的检测算法，例如“Arc-support line segments revisited: an efficient high-quality ellipse detection”等；
3. 未明确说明算法的检测速度；
4. 建议列出算法的重要中间过程量。

## 审稿人2

本文提出了一种基于全局共聚类的新颖椭圆检测方法。该方法根据椭圆概率分布的JS散度对弧进行分组。实验表明，该方法具有较高的F值，并且无效或冗余的椭圆较少。实验充分证明了他们的论点。总体而言，这是一个具有新颖性的有趣手稿。

然而，手稿在逻辑性、严谨性和语言准确性等方面存在几个缺陷，需要通过修改解决后再考虑接受。

以下是一些问题和建议：

1. 缺乏对实验中算法实际效率的分析和统计数据。从算法1来看，该方法需要重复进行SVD分解、k均值聚类和PFA计算，似乎计算复杂度很高。最好提供时间效率分析，以便读者更好地确定该方法的使用场景。
2. 图的标题应详细描述内容以便于理解。图3应参考图2中的彩色弧。此外，图3中的结果矩阵没有解释。它与兼容矩阵的相关性和区别是什么？图4中的圆圈/u_1/u_2是什么意思？
3. 3.4.2节中的不完整句子：“...表示像素p的灰度梯度”。
4. 在3.4.1节中，“...维护数据结构Q”，这是什么样的数据结构？
5. 在3.5节中，“我们可以将其可视化为每个弧的椭圆分布估计。”给出一个可视化的例子。
6. 在3.5.1节中，方程3需要更多解释。这个方程是如何得到的？
7. 在3.5.2节中，如何实际计算方程4中的散度？是通过在参数空间中取样以获得离散值吗？计算复杂度是多少？
8. 图像可能包含多个椭圆。如何在k均值中确定k值，为什么？
9. 最好在表1中添加精度和召回值，并在真实数据集上添加更多可视化内容。
10. 参考文献格式较差。请仔细检查信息的完整性。

## 审稿人3

1. 作者可以更清晰地说明这项工作的创新之处，并更好地解释为什么所提出的方法优于文献中的其他方法。
2. 缺乏计算复杂度分析。
3. 作者可以使用U2OS细胞和NIH3T3数据集[1,2,3]测量所提出方法的性能，并将其应用于细胞分割问题。此外，可以查看文献[1-5]中的数据集，若可能，可将更多数据集纳入比较。

> [1] A. Gharipour, A.W.-C. Liew, Segmentation of cell nuclei in fluorescence microscopy images: an integrated framework using level set segmentation and touching-cell splitting, Pattern Recog. 58 (2016) 1–11.
> [2] S. Zafari, T. Eerola, J. Sampo, H. Kälviäinen, H. Haario, Segmentation of overlapping elliptical objects in silhouette images, IEEE Trans. Image Process. 24 (12) (2015) 5942–5952.
> [3] C. Panagiotakis and A. Argyros, “Region-based fitting of overlapping ellipses and its application to cells segmentation,” Image and Vision Computing, vol. 93, p. 103810, 2020.
> [4] C. Panagiotakis and A. Argyros, Parameter-free Modelling of 2D Shapes with Ellipses, Pattern Recognition, vol. 53, pp. 259-275, 2016.
> [5]  Zou, T., Pan, T., Taylor, M., & Stern, H. (2021). Recognition of overlapping elliptical objects in a binary image. Pattern Analysis and Applications, 24(3), 1193-1206.

4. 在实验结果的评价指标中，您还可以包含交互比（IoU）或F1度量，该度量可以在分割图像中不使用阈值进行测量。

## 审稿人4

### 论文的优点

- 作者提出了一种基于共聚类的新颖方法，用于检测椭圆，采用全局方法解决了遮挡、重叠和噪声相关的挑战。
- 方法框架描述清晰。
- 强调了Prasad+数据集并创建了新数据集Prasad++。

### 论文的缺点

- 仅有三个实验对比方法，其中两个相对较旧。建议将该方法与近年来的方法进行比较。
- 在合成数据集中有四个定量指标，但在真实数据集中只提供了一个定量指标。

## 审稿人5

本文研究了图像中椭圆检测的问题。所提出的方法旨在结合局部几何属性和全局弧关系，以解决噪声、遮挡、重叠、间隙等问题。具体来说，通过采用共聚类算法，成功解决了椭圆间的遮挡和重叠问题，同时提出了PFA（错误警报概率）程序，以尽量减少由于噪声和其他图像缺陷引起的误报。所提出的方法是通用的，适用于合成图像和真实图像。

本文的前两部分写得很好，能为读者提供有关椭圆检测问题各个子问题的详细信息。然而，第3部分比较难以阅读。具体来说：

- 包含大量已知理论的参考文献。例如，第3.2节的大部分内容，主要在第8页，详细介绍了众所周知的SVD方法。第3.5.2和3.5.3节也提到了关于KL散度和JS散度的已知事实。第3.7节对算法1第15页的详细解释也是不必要的。
- 第3.4.1和3.4.2节介绍了[10]的详细部分，这是所提出方法的一部分。在第3.4节的第二段中写道：“我们采用了[10]中提出的弧提取技术……”，但紧接着写道“我们的方法中的候选生成步骤……”和“我们的弧检测过程可以分为两个主要步骤：……”。我认为这两句话中的“我们”一词是混淆的，应该去掉。
- 同一事物有多个定义。例如，在第3.3节、第3.4.1节和第3.5.1节中，图像I的定义完全相同。
- 使用术语时产生混淆，相同的符号用于不同的事物。例如，第6页的表A被称为特征矩阵，第8页称为数据矩阵，第13页称为兼容矩阵。

另一个问题与工作的创新性有关。在第14页的4个步骤中提出的共聚类算法的核心，其中使用SVD方法分解矩阵并尝试在变换空间中提取聚类，在需要分割、子空间聚类等模式识别问题中并不是未知的想法。此外，[10]的方法也是所提出方法的一部分，需要强调使用[10]提取弧候选后椭圆检测问题的困难程度。在这方面，一些有帮助的图表会很有用，其中弧候选被可视化，显示它们是如何从[10]中提取出来的。
其他意见：

1) 给论文中的所有方程编号，这会使读者在讨论论文时更容易引用具体的方程。
2) 第8页S_row和S_col方程中的最小化约束应更新，明确表示最小化应针对i_1和j_1进行。
3) 第4页第2.3节中的短语“to enhance ellipse detection, including using the Hough transform…”可以进行修正。
4) 请创建一个详细的技术流程图以进一步澄清方法。这个流程图可以与图5中显示的一般流程图一起展示。
建议的技术流程图格式为：
使用[10]进行弧候选提取 → 提取每个弧属于椭圆的概率 → 提取兼容矩阵，元素表示椭圆之间的Jensen-Shannon散度 → 兼容矩阵元素的共聚类。

总体来说，我认为本文需要进行很多修改，目前还不适合在如此高影响力的期刊上发表。
