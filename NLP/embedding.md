---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---
# Text Embedding
## Contrastive Learning
对比学习（Contrastive Learning）用于生成文本嵌入。在文本聚类的背景下，对比学习主要是通过在相似和不相似的样本之间建立对比来训练模型，使得相似样本在嵌入空间中靠近，不相似样本远离。
1. BERT (Bidirectional Encoder Representations from Transformers)
方法和架构：BERT使用Transformer架构，特别是其编码器部分。BERT通过双向训练深度Transformer模型来生成文本的上下文嵌入。它在大规模的文本数据上进行预训练，使用两种主要任务：掩码语言模型（Masked Language Model, MLM）和下一个句子预测（Next Sentence Prediction, NSP）。
特点：BERT的双向编码使得它能够捕捉到更丰富的上下文信息，对多种自然语言处理任务有很好的表现。
2. GPT (Generative Pre-trained Transformer)
方法和架构：GPT使用Transformer的解码器部分进行自回归语言建模。它在大规模文本数据上进行预训练，通过预测序列中的下一个词来学习语言模型。
特点：GPT在生成任务上表现出色，能够生成流畅且连贯的文本，同时也能用于文本嵌入生成。
3. RoBERTa (Robustly optimized BERT approach)
方法和架构：RoBERTa是BERT的改进版，它通过更大的数据集、更长时间的训练以及去除了NSP任务来优化BERT的性能。它依然使用Transformer编码器架构。
特点：RoBERTa在许多基准测试上超越了BERT，提供了更强的文本理解和嵌入生成能力。
4. T5 (Text-To-Text Transfer Transformer)
方法和架构：T5将所有文本处理任务都转换为文本生成任务。它使用标准的Transformer架构，并在大规模文本数据上进行预训练。
特点：T5的统一框架使得它在多种任务上都有出色的表现，能够生成高质量的文本嵌入。
5. DistilBERT
方法和架构：DistilBERT是BERT的精简版，通过知识蒸馏的方法减少了模型的参数数量和计算量，同时保持了大部分的性能。它也使用Transformer编码器架构。
特点：DistilBERT更轻量级，适合资源受限的应用，同时提供了接近BERT的性能。
6. Sentence-BERT (SBERT)
方法和架构：SBERT在BERT的基础上添加了一个Siamese网络结构，以生成固定长度的句子嵌入。它通过对比学习优化嵌入，使相似句子的嵌入靠近，不相似的句子嵌入远离。
特点：SBERT特别适合句子级别的相似性任务，如语义搜索、文本聚类等。
7. Universal Sentence Encoder (USE)
方法和架构：USE使用Transformer或深度平均网络（DAN）架构，通过在大规模的对话和网络文本数据上进行预训练来生成通用的句子嵌入。
特点：USE提供了高效且高质量的句子嵌入，适用于多种下游任务。
