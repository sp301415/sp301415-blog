---
title: LLL 알고리즘으로 정수 문제 풀기
tag: [수학]
summary: 격자 이론의 아이디어를 이용하면 정수 문제를 색다른 각도에서 접근해서 풀 수 있습니다.
---

## Integer Problems

정수 문제는 일반적으로 **아주 어렵다**. 그렇기 때문에 수학자들은 아주 오래 전부터 정수 문제를 풀기 위한 방법을 고안해냈다. 예를 들어서, 다음의 아주 일반적인 문제를 살펴보자.

**Problem.** (Integer Relation).  $a_1,  \cdots, a_n \in \R$에 대해서, 다음을 만족하는 non-trivial solution $x_1, \cdots, x_n \in \Z$를 찾으시오.

$$
a_1x_1 + \cdots + a_nx_n = 0
$$

만약 이것이 실수에 관한 문제였다면, 풀기가 아주 쉬웠을 것이다. 그냥 $a_1, \cdots, a_{n-1}$에 아무 수나 넣은 다음 일차방정식을 풀면 되기 때문이다. 그렇지만 해가 정수여야 한다는 조건이 붙어 있으므로, 가능한 해가 상당히 빡빡하다는 사실을 직관적으로 알 수 있다. 이렇게 실수들 사이의 정수 관계를 찾는 문제를 Integer Relation Problem이라고 하며, 다른 정수 문제들 또한 Integer Relation Problem의 일부분으로 생각할 수 있다. 예를 들어서, 아주 유명한 Subset Sum Problem을 살펴보자.

**Problem.** (Subset Sum Problem). 집합 $A \in \Z$와 자연수 $M$이 주어져 있다고 하자. 이 때, $\sum S = M$을 만족하는 $A$의 부분집합 $S$를 찾으시오.

이 문제는 다음과 같이 변형할 수 있다. 먼저, $A = \{a_1, \cdots, a_n\}$이라고 써 보자. 그렇다면, 다음과 같은 방정식을 생각할 수 있다.

$$
a_1x_1 + \cdots + a_nx_n - M = 0, \quad x_i = 1 \text{ or } 0
$$

이제 $S = \{a_i \mid x_i = 1\}$가 Subset Sum Problem의 해가 된다. 따라서, Subset Sum Problem은 조건이 더 빡빡한 Integer Relation Problem이라고 볼 수 있다. 

오늘 이 글에서는, 이러한 정수 문제들을 기하학적으로 접근하는 방법에 대해 다룰 것이다.

## Lattices

Lattice는 우리말로는 격자라고 번역할 수 있다. 마치 체스판처럼, 평면을 같은 크기의 칸들로 나눈 것을 격자라고 한다. 조금 더 수학적으로 써 보면...

**Definition.** (Lattice). **기저**(Basis) $\mathbf{B} = \{\mathbf b_1, \cdots, \mathbf b_n \}$에 대해서, 격자 $\mathcal L(\mathbf B)$는 다음과 같이 정의된다.

$$
\mathcal L = \left\{\sum_i a_i \mathbf b_i \mid a_i \in \Z\right\}
$$

### Lattice Problems and Integer Problems

격자 위의 오래된 문제로는 다음 두 가지가 있다.

- SVP(Shortest Vector Problem): $\mathcal L$ 위의 가장 짧은 벡터 $\lambda_1$을 구하시오.
- CVP(Closest Vector Problem): 주어진 벡터 $\mathbf w \in \R^n$와 가장 가까운 $\mathcal L$ 위의 벡터 $\mathbf v$를 구하시오.

참고로, 두 문제 모두 NP-Hard임이 알려져 있다. 그렇지만, 특수한 조건 하에서의 SVP와 CVP는 쉽게 풀 수 있음 또한 알려져 있다. 따라서, 우리는 먼저 Integer Problem을 SVP로 바꾼 뒤(!) SVP를 풀 것이다. (CVP는 이 글에서는 자세히 다루지 않겠다.)

먼저, 위의 Integer Relation Problem에 집중하자. 이 정의에서, 주어진 $a_i$ 들에 비해서 정수 해 $x_i$들은 매우 작다고 해도 아무 상관이 없다. 왜냐하면, 주어진 식이 선형이므로, 적당한 factor를 $a_i$들에 곱해서 크기를 마음대로 조절할 수 있기 때문이다. 이제, 다음 행렬의 row들이 생성하는 격자를 생각해보자.

$$
\mathcal L = \begin{bmatrix}
1 & 0 & \cdots & 0 & a_1 \\
0 & 1 & \cdots & 0 & a_2 \\
 & & \ddots & &\vdots \\
0 & 0 & \cdots & 1 & a_n
\end{bmatrix}
$$

각 row를 $\mathbf b_i$라고 하면, 다음 벡터는 $\mathcal L$ 안에 들어있다.

$$
\begin{align*}
\mathbf v &= x_1 \mathbf b_1 + \cdots x_n \mathbf b_n \\
&= (x_1, \cdots, x_n, a_1x_1 + \cdots + a_nx_n) \\
&\approx (x_1, \cdots, x_n, 0)
\end{align*}
$$

위에서 각 $x_i$들은 충분히 작다고 했으므로, $\mathbf v$는 $\mathcal L$ 위의 짧은 벡터가 된다. 따라서, 우리는 $\mathcal L$에서의 SVP를 풀 수 있다면, Integer Relation Problem도 높은 확률로 풀 수 있게 된 것이다. 언뜻 보면 약팔이 같지만, 이 글에서 우리는 이 방법이 진짜로 먹힌다는 것을 증명할 것이다. 심지어는, NP-Complete라고 알려진 Subset Sum Problem 중 일부를 다항 시간 안에 풀 수 있다는 사실(!)도 알아볼 것이다.

## Lattice Reduction
SVP를 푸는 가장 직관적인 답은 기저의 수직성(Orthogonality)를 생각하는 것이다. 왜냐하면, 다음이 성립하기 때문이다.

**Claim.** 기저 $\mathbf B$가 orthogonal하다고 하자. 그렇다면, $\lambda_1 = \min \mathbf b_i $이다.

**pf.** 직관적으로 당연하다. $\lambda_1 = \sum a_i\mathbf b_i$라고 하자. 이 때 일반성을 잃지 않고 $a_i \neq 0$이라고 하자. (즉, coefficient가 nonzero인 기저만 생각하자). 그렇다면, 

$$
\begin{align*}
\lVert \lambda_1 \rVert^2 &= \lVert a_1 \mathbf b_1 + \cdots + a_k \mathbf b_k \rVert^2 \\
&= a_1^2\lVert \mathbf b_1 \rVert ^2 + \cdots + a_k^2\lVert \mathbf b_k \rVert ^2 \\
&\ge a_i^2 \min \lVert \mathbf b_i \rVert ^2  \\
&\ge \min \lVert \mathbf b_i \rVert ^2
\end{align*}
$$

이것을 조금만 더 확장한다면, 굳이 수직일 필요 없이, *적당히* 수직이기만 해도 위의 Claim은 여전히 성립한다고 생각할 수 있다. 따라서, 만약 이 격자의 수직에 가까운 기저를 찾는다면, SVP를 풀 수 있을 것이다. 이 문제를 격자 축소 (Lattice Reduction) 문제라고 하며, 이것 또한 가우스 시대 때부터 연구된 유서 깊은 문제이다. (실제로, 2차원에서의 SVP 문제는 가우스가 가장 먼저 풀어냈다.)

그런데, 우리는 이미 일반적인 벡터 공간에서 수직인 기저를 아주 효율적으로 찾는 방법을 이미 알고 있다. 바로 Gram-Schmidt Orthogonalization이다. 까먹은 사람들을 위해 다시 써 보면,

**Definition.** (Gram-Schmidt Orthogonalization.) 벡터 공간 $V$의 기저 $\mathbf B$가 주어져 있을 때, 다음 과정을 통해 orthogonal한 기저 $\mathbf B^\ast$를 얻을 수 있다.

$$
\mathbf b^\ast_i = \mathbf b_i - \sum_{j=1}^{i-1} \mu_{i, j}\mathbf b^\ast_j
$$

여기에서, Gram-Schmidt 계수 $\mu_{i, j} = \dfrac{\langle \mathbf b_i, \mathbf b^\ast_j \rangle}{\lVert \mathbf b_j \rVert^2}$이다.

물론, 이것을 그대로 우리의 문제에 가져다 쓸 수는 없다. 격자는 기본적으로 이산적이기 때문에, 이렇게 얻은 기저가 원래 격자를 span할 이유는 전혀 없기 때문이다. 하지만, Gram-Schmidt를 *근사*한다면 가능하지 않을까? 이것이 바로 LLL Algorithm의 아이디어이다.

## LLL Algorithm

LLL(Lenstra-Lenstra-Lovasz) Algorithm은 1982년에 Arjen Lenstra, Hendrik Lenstra, 그리고 Laszlo Lovasz가 고안한 알고리즘이다.

**Definition.** (LLL-Reduced Basis) $\mathcal L$의 기저 $\mathbf B$와, 그것을 Gram-Schmidt한 기저 $\mathbf B^\ast$을 생각하자. (이 때, 물론 $\mathbf B^\ast \subset \R^n$이다.) $\mathbf B$와 $\mathbf B^\ast$가 다음 조건을 만족한다면, $\mathbf B$를 $\mathcal L$의 **LLL-Reduced Basis**라고 한다.

1. (Size Condition.) $\displaystyle \lvert \mu_{i, j} \rvert = \left\lvert {\langle \mathbf b_i, \mathbf b^\ast_j \rangle \over \lVert \mathbf b_j \rVert^2} \right\rvert \le {1 \over 2} $
2. (Lovasz Condition.) $\displaystyle \lVert \mathbf b_{i+1}^\ast + \mu_{i+1, i}\mathbf b^\ast_i \rVert \ge {3 \over 4}\lVert \mathbf b^\ast_i \rVert^2$

Lovasz Condition의 $3/4$는 다른 값 $1/4 < \delta < 1$로 대체될 수 있다. 첫 번째 조건을 이해하는 것은 크게 어렵지 않을 것이다. Gram-Schmidt Orthogonalization에서 $\mu$ 대신 $\lceil \mu \rfloor$를 써서 근사하는 것과 동치이기 때문이다. 두 번째 조건은 살짝 이해하기 까다로운데, 접근하는 두 가지 방법이 있다.

첫째는 반례를 생각해보는 것이다. 만약 Size Condition만 주어졌다고 하자. 그렇다면, 만약 $\mathbf b_i$가 $\mathbf b_j$에 비해 매우 길다면, $\mu_{i, j}$의 크기는 둘 사이의 각도와는 관계없이 $1/2$보다 작아질 수 있다. 그렇다면, $\mathbf b_i^\ast$의 길이는 $\mathbf b_j^\ast$의 길이보다 아주 작거나 클 것이다. 하지만, Lovasz Condition이 주어진다면,

$$
\begin{align*}
\lVert \mathbf b_{i+1}^\ast + \mu_{i+1, i}\mathbf b^\ast_i \rVert &= \lVert \mathbf b_{i+1}^\ast \rVert^2  + \mu_{i+1, i}^2 \lVert \mathbf b_i^\ast \rVert ^2 \\
&\ge {3 \over 4}\lVert \mathbf b_i^\ast \rVert^2 \\
\lVert \mathbf b_{i+1}^\ast \rVert^2 &\ge \left({3 \over 4} - \mu_{i+1, i}^2 \right)\lVert \mathbf b_i^\ast \rVert^2 \\
&\ge {1 \over 2} \lVert \mathbf b_i^\ast \rVert^2
\end{align*}
$$

이므로, $\mathbf b_{i+1}^\ast$의 길이가 $\mathbf b_i^\ast$의 길이보다 아주 짧을 수는 없다. 즉, Orthogonal한 벡터들의 순서를 어느 정도 강제한다. 그리고, $\delta > 1/4$여야 한다는 사실도 알 수 있다.

두 번째 접근은 조금 더 엄밀하다. Gram-Schmidt를 거칠게 요약하자면, $\mathbf b_i$를 $\operatorname{span} (\mathbf b_1, \cdots, \mathbf b_{i-1})^{\perp}$로 사영(projection) 시키는 것이다. 이 정의에서 Lovasz condition을 바라본다면, 우변은 $\mathbf b_{i+1}$을 $\operatorname{span} (\mathbf b_1, \cdots, \mathbf b_{i-1})^{\perp}$에 사영시킨 것이고, 좌변은 $\mathbf b_i$를 이 평면에 사영시킨 것이다. 따라서, 비슷하게 이 조건은 벡터들의 순서를 강제하는 것이라고 이해할 수 있다. 만약 $\delta = 1$이라면, 이 순서를 엄밀하게 지킨다는 뜻이 될 것이다. 

LLL Algorithm은 LLL-Reduced Basis의 정의에서 자연스럽게 따라나온다.

**Definition.** (LLL Algorithm.) 다음 알고리즘은 임의의 기저 $\mathbf B$를 LLL-Reduced Basis로 변환한다.

1. Gram-Schmidt Orthogonalization을 근사한다. ($\mu_{i, j}$ 대신 $\lceil \mu_{i, j} \rfloor$을 사용해서.)
2. 모든 $i$에 대해서 Lovasz Condition을 확인한다. 이 때,
    - 조건을 만족한다면 종료한다.
    - $\mathbf b_i^\ast$와 $\mathbf b_{i+1}^\ast$가 조건을 만족하지 않는다면, $\mathbf b_i$와 $\mathbf b_{i+1}$의 순서를 바꾼 뒤, 1번으로 돌아간다.

이 알고리즘의 Correctness는 거의 자명하다. Step 1을 거치면 Size Condition이 만족되고, Step 2를 거치면 Lovasz Condition이 만족된다. 다만 신기한 사실은, 이 알고리즘이 다항 시간 안에 종료된다는 것이다.

**Theorem.** (Runtime of LLL.) LLL은 다항 시간 안에 종료된다.

**pf.** 증명은 조금 테크니컬하다. 먼저 다음 두 값을 생각하자.

$$
d_l = \prod_{i = 1}^l \lVert \mathbf b_i^\ast \rVert ^2, \quad D = \prod_{l=1}^n d_l = \lVert \mathbf b_1^\ast \rVert^{2n} \cdots \lVert \mathbf b_n^\ast \rVert^2
$$

우리는 다음 두 보조정리를 통해 원래 정리를 증명할 것이다.

**Lemma 1.** $D$는 bounded되어 있다. 특히, $D \in \Z^+$이다.

**pf.** Upper Bound는 자명하다. 가장 긴 기저 $\mathbf b_{\text{max}}^\ast$를 대입하면:

$$
D \le \lVert \mathbf b_{\text{max}}^\ast \rVert^{2n} \cdots \lVert \mathbf b_{\text{max}}^\ast \rVert^2 = \lVert \mathbf b_{\text{max}}^\ast \rVert^{n(n+1)}
$$

Lower Bound는 조금 까다롭다. 먼저, $d_l = (\det \mathbf B_l^\ast)^2$임을 관찰하자. 여기에서 $\mathbf B_l^\ast$는 $\mathbf B^\ast$를 $l$ 차원으로 restrict 시킨 것이다. Gram-Schmidt Orthogonalization의 정의에 따라, $\mathbf B_l$과 $\mathbf B_l^\ast$의 transition matrix는 다음과 같이 정의된다.

$$
\mathbf B_l = \begin{bmatrix}
1 & 0 \\
\mu & 1 
\end{bmatrix} \mathbf B_l^\ast
$$

따라서, $\det \mathbf B_l^\ast = \det \mathbf B_l \in \Z$이고 $d_l \in \Z^+$이므로, $D \in \Z^+$이다. Lower Bound는 자연스럽게 따라온다.

**Lemma 2**. $D$는 항상 감소한다.

**pf.** Step 1에서 $\mathbf B^\ast$가 바뀌지 않음은 쉽게 확인할 수 있다. Step 2에서, $\mathbf b_i$와 $\mathbf b_{i+1}$를 swap했다고 가정하자. 그 뜻은, Lovasz Condition이 만족되지 않았다는 뜻이므로,

$$
\lVert \mathbf b_{i+1}^\ast + \mu_{i+1, i}\mathbf b^\ast_i \rVert < {3 \over 4}\lVert \mathbf b^\ast_i \rVert^2
$$

이다. 이제, swap한 뒤의 벡터들을 $\tilde {\mathbf b}$라고 하자. 특히, $\tilde {\mathbf b}\_i = \mathbf b_{i+1}$, $\tilde{\mathbf b}\_{i+1} = \mathbf b_i$이다. 그러면 $\tilde d_l$은 어떻게 될까? 만약 $l < i$라면, $\tilde{\mathbf b}\_k = \mathbf b_k$이므로, $d_l = \tilde d_l$일 것이다. 만약 $l \ge i+1$이라면, $d_l$과 $\tilde d_l$ 모두 $\mathbf b_1, \cdots, \mathbf b_i, \mathbf b_{i+1}$을 포함하므로, 역시 $d_l = \tilde d_l$일 것이다. 따라서, 다음이 성립한다.

$$
{\tilde d_i \over d_i} = {\lVert \tilde{\mathbf b}_i^\ast \rVert^2 \over \lVert \mathbf b_i^\ast \rVert^2}
$$

그런데, 정의에 따르면

$$
\lVert \tilde{\mathbf b}_i^\ast \rVert ^2 = \lVert \mathbf b_{i+1}^\ast + \mu_{i+1, i}\mathbf b_i^\ast \rVert^2 < {3 \over 4} \rVert \mathbf b_i^\ast \rVert^2
$$

따라서, 우리는 $D$가 매 루프마다 적어도 $3/4$만큼 감소한다는 사실을 알 수 있다.

이제 Lemma 1과 Lemma 2에 따르면, LLL 알고리즘은 적어도 $\log_{3/4} \lVert \mathbf b_{\text{max}}^\ast \rVert^{n(n+1)} = O(n^2 \log \lVert b_{\text{max}} \rVert)$ 시간 안에 종료된다. Step 1, Step 2 또한 다항 시간 안에 종료되므로, LLL Algorithm 전체는 다항 시간 안에 종료된다. (실제로는 $O(d^5 n \log^3 \lVert b_{\text{max}} \rVert)$에 종료된다고 알려져 있다.)

이 증명 과정을 유심히 읽어본다면 $\delta < 1$이어야 하는 이유를 알게 될 것이다. 위에서 언급했듯이, $\delta = 1$이라면 $\mathbf b_i^\ast$들의 순서가 더 엄밀해지므로, LLL 알고리즘의 결과가 개선된다. 그렇지만, 우리의 증명 과정에서 사용한 $D$가 감소한다는 사실을 더 이상 쓸 수 없게 되므로, 다항 시간 안에 종료된다는 보장이 없어진다. 실제로도 이 경우에 LLL 알고리즘이 다항 시간 안에 종료되는지의 여부는 아직 open이다.

드디어 이 글의 종착지인 다음 정리에 도착했다.

**Theorem.** $\mathcal L$의 LLL-Reduced Basis를 $\mathbf B$라고 하자. 그렇다면 다음이 성립한다.

$$
\lambda_1 \le {\sqrt 2}^{n-1} \lVert \mathbf b_1 \rVert 
$$

즉, LLL은 SVP를 $\sqrt 2^{n-1}$의 factor로 푼다.

**pf.** 먼저 다음 보조정리를 증명하자.

**Lemma 1.** $\lambda_1 \ge \lVert \mathbf b_{\text{min}}^\ast \rVert$

**pf.** 정의를 쓰면 간단하게 보일 수 있다. 위에서처럼, 일반성을 잃지 않고 $a_i \neq 0$이라고 하자.

$$
\begin{align*}
\lambda_1^2 &= \left\lVert \sum a_i \mathbf b_i \right\rVert^2 \\
&= \left\lVert \sum a_i \sum \mu_{i, j} \mathbf b_i^\ast \right\rVert^2 \quad (\mu_{i, i} = 1) \\
&= \lVert a_1 \mathbf b_1^\ast + a_2(\mathbf b_2^\ast + \mu_{2, 1}\mathbf b_1^\ast) + \cdots \rVert^2 \\
&\ge a_n^2 \lVert \mathbf b_n^\ast \rVert^2 \\
&\ge \lVert \mathbf b_{\text{min}}^\ast \rVert^2 
\end{align*}
$$

이제 $\mathbf b_{\text{min}} = \mathbf b_m$이라고 하자. 위에서 보았듯이, Lovasz Condition에 의해 $\lVert \mathbf b_1^\ast \rVert^2 \le 2\lVert \mathbf b_2^\ast \rVert^2 \le \cdots \le 2^{k-1}\lVert \mathbf b_k^\ast \rVert^2$이 성립한다. 따라서,

$$
\begin{align*}
\lVert \mathbf b_1 \rVert^2 &= \lVert \mathbf b_1^\ast \rVert^2 \\
&\le 2^{m-1} \lVert \mathbf b_m^\ast \rVert ^2 \\
&\le 2^{n-1} \lambda_1^2
\end{align*}
$$

양변에 루트를 씌우면 원하는 결과를 얻는다.

## Solving Integer Problems using Lattices

지금까지 Integer Problem을 SVP로 바꾼 뒤, LLL을 통해 풀 수 있다는 것을 살펴보았다. 꼭 여기에 있는 문제가 아니더라도, 좋은 조건만 있으면 LLL 알고리즘은 좋은 해결책이 될 수 있다. 일반적으로는 다음과 같은 사고방식을 따르면 좋다.

1. 문제에서 어떻게든 크기가 작고 선형인 해를 뽑아낸다.
2. 적당한 Lattice를 만들어서 1. 에서 구한 작은 해가 SVP의 정답이 되도록 만든다. 
    - 이 글에서 자세히 다루지 않았지만, 여기서 target vector의 크기의 좋은 가늠은 $\sqrt n (\det \mathcal L)^{1/n}$ 정도이다. 이 값보다 작다면, SVP를 통해 찾을 수 있을 가능성이 높다.
3. LLL을 통해 SVP를 푼다.
4. PROFIT!

### Subset Sum Problem using LLL

위에서, 특수한 종류의 Subset Sum Problem을 다항 시간 안에 풀 수 있다고 했다. 이 특수한 조건이란 $a_i = O(2^{2n})$ 정도로, 개수에 비해 크기가 아주 큰 조건을 말한다. 이 경우 LO-Attack을 통해 Subset Sum Problem을 풀 수 있다. (후에 CJLOSS 알고리즘을 통해 이 bound는 $O(2^n)$ 정도까지 개선되었다.) 

여기에서는 $n = 5$인 다음의 경우를 풀어보도록 하자.
```python
arr = [1562, 1283, 1381, 1272, 1540]
target = 4483
```
LLL 알고리즘을 직접 코딩하기엔 시간이 너무 많이 걸리므로, [SageMath](https://www.sagemath.org/)를 이용해서 위의 풀이 과정을 따라가보자.

*1. 문제에서 어떻게든 크기가 작고 선형인 해를 뽑아낸다.*

이것은 이 문제에서 자연스럽게 주어져 있다. 위에서 보았듯이,

$$
a_1x_1 + \cdots + a_nx_n - M = 0, \quad x_i = 1 \text{ or } 0
$$

을 푸는 것과 동치이며, $x_1, \cdots, x_n$이 선형이고 작은 해이다.

{:start="2"}
*2. 적당한 Lattice를 만들어서 1. 에서 구한 작은 해가 SVP의 정답이 되도록 만든다.*

다음과 같은 Lattice를 생각하자.

$$
\mathcal L = \begin{bmatrix}
1 & 0 & \cdots & 0 & -a_1 \\
0 & 1 & \cdots & 0 & -a_2 \\
 & & \ddots & &\vdots \\
0 & 0 & \cdots & 1 & -a_n\\
0 & 0 & \cdots & 0 & M
\end{bmatrix}
$$

각 row들을 $\mathbf b_i$라고 하면, 

$$
\begin{align*}
x_1 \mathbf b_1 + \cdots + x_n \mathbf b_n &= (x_1, \cdots, x_n, M - \sum x_ia_i) \\
&= (x_1, \cdots, x_n, 0)
\end{align*}
$$

은 $\mathcal L$ 위의 작은 벡터이고, 따라서 SVP의 답이 될 가능성이 크다. 직접 코딩해보면:

```python
L = []
N = len(arr)

for i, a in enumerate(arr):
    row = [0] * (N+1)
    row[i] = 1
    row[-1] = -a
    L.append(row)
L.append([0] * N + [target])

L = Matrix(L)
print(L)
"""
[    1     0     0     0     0 -1562]
[    0     1     0     0     0 -1283]
[    0     0     1     0     0 -1381]
[    0     0     0     1     0 -1272]
[    0     0     0     0     1 -1540]
[    0     0     0     0     0  4483]
"""
```

{:start="3"}
*3. LLL을 통해 SVP를 푼다.*

```python
L = L.LLL()
print(L)
"""
[ 1  0  1  0  1  0]
[-1  2  0 -2  1  0]
[-3 -1  2 -1  0 -4]
[ 2 -2 -2 -3  1 -3]
[ 1  1 -4  2  3 -2]
[-4 -2  1  1  4  1]
"""
```

여기에서, `L[0]`이 우리가 정확히 원하는 형식으로 나왔음을 알 수 있다. (맨 끝의 값은 0이고, 나머지 값은 0 또는 1이다.) 따라서, 우리는 $x_i$를 전부 찾았고, 이 문제를 풀었다! 직접 확인해보자:

```python
sol = []
for i, x in enumerate(L[0]):
    if x == 1:
        sol.append(arr[i])

print(sol)
"""
[1562, 1381, 1540]
"""
print(sum(sol), target)
"""
4483 4483
"""
```

## 맺음말 

이 글에서는 정수에 관련된 문제를 격자로 옮긴 뒤, LLL 알고리즘을 통해 푸는 방법을 알아보았다. 꼭 Integer Relation Problem과 관련된 문제가 아니라도, LLL은 초월수 판별, 정수계수 다항식 인수분해 등 다양한 문제에 폭넓게 쓰일 수 있는 강력한 알고리즘이다. 특히, 암호학계에서는 RSA의 가장 강력한 공격 중 하나인 Coppersmith Theorem에 응용된다. (언젠간 이에 대해서 다뤄볼 생각이다.) 꼭 응용이 아니더라도, 한 분야의 문제를 다른 분야로 옮겨서 푼다는 아이디어 자체가 수학적으로도 매력적이라고 생각한다. 
