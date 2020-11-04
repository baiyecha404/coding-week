# coding-week problem3 notes

[toc]

## function

$￢(A ∧ B) ↔ (￢A ∨ ￢B)$
```python
BinaryOp(
    left=UnaryOp(
        op=not,
        operand=BinaryOp(
            left=Variable(name='A'),
            op=and,
            right=Variable(name='B'))),
    op=eq,
    right=BinaryOp(
        left=UnaryOp(
            op=not,
            operand=Variable(name='A')),
        op=or,
        right=UnaryOp(
            op=not,
```

1. 真值表

基本功能：
- eg.
- $(A ∧ ￢B )$
- $(A  → B )$
- $1 ↔ (P ∨ 1)$
- $(A ∧ ￢B ) ∨ (A ∧ B) ∨ (￢A ∧ (￢C ∨ ￢D)) ∨ (￢A ∧ B)$

2. 主析取/主合取
   同上.可直接根据真值表生成。    

3. 判断
- eg.
- $A  → B$
- $ ￢B ∨ C$ 
- ......


## problems

 一对夫妻带着他们的一个孩子在路上碰到一个朋友。朋友问孩子：“你是男孩还是女孩？”朋友没听清孩子的回答。孩子的父母中某一个说，我孩子回答的是"我是男孩"，另一个接着说："这孩子撒谎，她是女孩。"这家人中男性从不说谎，而女性从来不连续说两句真话，也不连续说两句假话。试问这小孩性别，以及谁是其父亲，谁是其母亲？



## solution

提出假设：
```
A ： 第一个是男的
B ： 第一个说的话是真的
C ： 第二个说的第一句是真的
D ： 第二个说的第二句是真的
```

进行假言推理：
1. $A ∧ ￢B$  (第一个说的是男的且他说谎)
2. $A ∧ B$   第一个说话的是父亲,父亲没说谎。此时母亲两句话都真或都假，会与题设相矛盾
3. $￢A ∧ (￢C ∨ ￢D)$ 第二个是父亲，父亲说的两句话有谎话。
4. $￢A ∧ B$   第二个是父亲，此时第一个为母亲且她说的是真的。此时父亲的话全假，与题设矛盾

得到
$$
(A ∧ ￢B ) ∨ (A ∧ B) ∨ (￢A ∧ (￢C ∨ ￢D)) ∨ (￢A ∧ B)
$$
input:
`(A ∧ ￢B ) ∨ (A ∧ B) ∨ (￢A ∧ (￢C ∨ ￢D)) ∨ (￢A ∧ B)`
计算其真值表结果为假的情况

![](https://hackmd.summershrimp.com/uploads/upload_dc587f0255722a773531b0334231faac.png)

`A = 0 ,B = 0  C = 1,D = 1` 
即：
第一个是女的，第二个是男的。
第一个说的是假的。第二个说的两句话都真
从而可知孩子是女孩


