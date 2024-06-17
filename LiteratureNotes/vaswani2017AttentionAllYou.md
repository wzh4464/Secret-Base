---
toc: true
documentclass: "ctexart"
classoption: "UTF8"

zotero-key: ALANNG29
zt-attachments:
  - 1291
citekey: vaswani2017AttentionAllYou
title:
  - Attention Is All You Need
---
# Attention Is All You Need

[Zotero](zotero://select/library/items/ALANNG29) [attachment](file:///C:/Users/wuzihan/Zotero/storage/FIB7NQGV/Attention_Is_All_You_Need_Vaswani_et_al_2017.pdf)

> [!note] Page 1
> transduction
> ---
>
> 转换
> ^GXRSYXN3aFIB7NQGVp1
> [!note] Page 1
> dispensing
> ---
>
> 分配
> ^KCEPWU5NaFIB7NQGVp1
> [!note] Page 2
> Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence
> ---
>
> 在自注意力机制中，输入序列中的每个位置都会与其他位置计算相似度得分，表示这两个位置的相关性或重要性。这些得分将被用来加权计算每个位置的特征向量，这个特征向量被认为是该位置对序列的表示。与传统的注意力机制不同，自注意力机制不需要外部信息来帮助计算注意力，而是仅仅利用序列内部的信息。举个例子，如果我们有一个输入序列：“I like to eat pizza”，自注意力机制将会计算每个位置之间的相关性或重要性，比如“like”和“pizza”的相关性，或“like”和“eat”的相关性。然后，通过加权计算每个位置的特征向量，得到整个序列的表示。这个表示可以被用来完成各种序列处理任务，比如语言翻译、文本摘要、情感分析等。
> ^HQY2JYLAaFIB7NQGVp2
> [!note] Page 2
> At each step the model is auto-regressive [9], consuming the previously generated symbols as additional input when generating the next
> ---
>
> 自回归：上一步的输出也作为输入
> ^H9GUMZIVaFIB7NQGVp2
> [!note] Page 3
> residual connection
> ^VU5LA7TVaFIB7NQGVp3
> [!note] Page 5
> 3.2.3 Applications of Attention in our Model
> ---
>
> Transformer在三种不同的方式下使用多头注意力：在"编码器-解码器注意力"层中，查询来自前一个解码器层，而内存的键和值来自编码器的输出。这使得解码器中的每个位置都可以关注输入序列中的所有位置。这类似于序列到序列模型（如[31, 2, 8]）中的典型编码器-解码器注意力机制。编码器中包含自注意力层。在自注意力层中，所有的键、值和查询都来自同一个位置，即编码器中前一层的输出。编码器中的每个位置都可以关注编码器前一层的所有位置。类似地，解码器中的自注意力层允许解码器中的每个位置关注解码器中包括该位置在内的所有位置。为了保持自回归属性，我们需要防止解码器中的左向信息流。我们通过在缩放点积注意力中屏蔽（设置为-∞）与非法连接对应的softmax输入中的所有值来实现这一点。通过这种方式，Transformer能够在不同层和不同部分之间进行全局的注意力计算，从而捕捉到更丰富的上下文信息，并实现有效的序列建模。注意力头的数量决定了模型可以关注输入序列的不同方面和细节，从而提升模型的表达能力和泛化性能。
> ^F9K75GA4aFIB7NQGVp5
