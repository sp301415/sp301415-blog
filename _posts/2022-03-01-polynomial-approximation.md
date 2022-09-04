---
title: 다항 근사, 체비셰프 정리와 레메즈 알고리즘
tag: [수학]
---

이 글에서 다룰 문제는 아주 간단하다. 임의의 연속 함수를 어떻게 하면 다항식으로 "잘" 근사할 수 있을까? 애초에, "잘" 근사한다는 것은 무엇일까? 문제를 조금 더 엄밀하게 써 보자.
<!--more-->

**Problem.** $[a, b]$에서 연속인 함수 $f$에 가장 가까운 다항식 $p$는 무엇일까?

여기서 "가깝"다는 것은 보통 다음과 같은 Supreme Norm의 관점에서 말하는 것이다.

$$
\lVert f \rVert_\infty = \sup_{x \in [a, b]} \lvert f(x) \rvert
$$

만약 우리가 두 함수의 차의 최댓값을 $\varepsilon$ 아래로 줄일 수 있다면, 즉 $p$가 $f$에 대해서 $\lVert f-p \rVert < \varepsilon$을 만족시킨다면, 우리는 $p$를 $f$의 $\varepsilon$-근사라고 한다. 만약 그러한 $\varepsilon$이 최소라면, 우리는 $p$를 $f$의 최적 근사(best approximation)이라고 한다.

## Weierstrass Approximation Theorem

해석학을 배워 본 사람이라면, 어떤 연속함수 $f$를 가져오더라도 항상 다항식으로 근사할 수 있다는 사실을 이미 알고 있을 것이다. 이것이 그 유명한 바이어슈트라우스 근사 정리(Weierstrass Approximation Theorem) 혹은 스톤-바이어슈트라우스 정리(Stone-Weierstrass Theorem)이다.

**Theorem.** (Weierstrass.) $[a, b]$에서 연속인 임의의 $f$에 대해서, $f$로 균등 수렴(uniformly converge)하는 적당한 다항식 함수열 $p_n$이 항상 존재한다.

다른 말로 써보자면, 임의의 $f$에 대해서 어떤 $\varepsilon$을 가져오더라도 $f$를 $\varepsilon$-근사하는 다항식을 찾을 수 있다는 것이다. 심지어 이 정리의 증명은 구성적이다. [Bernstein Polynomial](https://en.wikipedia.org/wiki/Bernstein_polynomial)이라는 것을 이용하면 항상 주어진 조건을 만족하는 함수열을 직접 만들어낼 수 있다. 이런! 문제가 너무 싱겁게 풀려버린 것 같다.

하지만 아직 안심(...?)하기엔 이르다. 왜냐하면, 많은 경우에 우리는 근사하는 다항식의 차수를 제한하고 싶기 때문이다. Weierstrass Approximation Theorem은 다항식의 차수에 대해서 말해주지도 않고, Bernstein Polynomial도 주어진 차수에 대해서 최적의 근사인지에 대한 보장은 없다. 문제는 아직도 굳건하다.

## Minimax Approximation

차수까지 고려해서 문제를 다시 적어보자면, 아래와 같다.

**Problem.** $[a, b]$에서 연속인 $f$에 대해서, $\lVert f - p \rVert = \max_{x \in [a, b]} \lvert f(x) - p(x) \rvert$를 최소화하는 $n$차 (혹은 그 이하의) 다항식 $p$를 구하시오.

이 문제는 최댓값(maximum)을 최소화(minimize)하는 것이므로, 보통 미니맥스 근사(Minimax Approximation) 문제라고 부른다. 이 글에서 살펴볼 문제도 바로 이것이다. (그리고, 앞으로 항상 $f$는 $[a, b]$에서 연속인 함수, 그리고 $p$는 $n$차 이하의 다항식이라고 가정하겠다.)

**Theorem.** 미니맥스 근사 문제의 해답은 존재한다.

**pf.** 구간 $[a, b]$에서 연속인 함수를 $\mathcal C[a,b]$라고 하고, 최대 $n$차의 다항식들의 집합을 $\mathcal P_n$이라고 하자. 그러면 $\mathcal P_n$은 (normed, linear space) $\mathcal C[a,b]$의 finite-dimensional subspace가 된다. $p \in \mathcal P_n$이 주어진 문제의 정답이라고 하자. 그러면, 적어도 $\lVert f - p \rVert < \lVert f \rVert$여야 한다. 즉, $p$는 집합 $K = \{q \in \mathcal P_n: \lVert f - q \rVert < \lVert f \rVert \}$ 내부에 존재한다. 이제 사상 $L(q) = \lVert f - q \rVert$를 생각하면, $K$는 컴팩트이고 $L$은 연속이므로 $L$을 최소화하는 점이 $K$ 내부에 존재하고, 이 점이 우리가 찾던 $p$이다.

## Alternating Sets and Chebyshev Equioscillation Theorem

미니맥스 근사 문제를 처음 고안하고 풀어낸 것은 러시아의 수학자 파프누티 체비셰프(Pafnuty Chebyshev)였다. 그는 이 문제의 답을 1854년에 찾았는데, 한 가지 놀라운 사실은 체비셰프의 결과는 위에서 살펴본 바이어슈트라우스의 정리보다 30년이나 앞선다는 사실이다. 즉, 체비셰프가 이 문제를 풀었을 때에는 해답이 존재하는지 존재하지 않는지조차 명확하지 않았다.

먼저 Alternating Set의 개념을 짚고 넘어가자.

**Definition.** (Alternating Set.) $f$에 대해서 만약 점들 $a \le x_1 < \cdots < x_k \le b$이 다음 두 가지 조건을 만족한다면,

1. $\lvert f(x_i) \rvert = \lVert f \rVert$ 
2. $f(x_i) = - f(x_{i-1})$

우리는 $x_i$들을 $f$의 Alternating Set이라고 하며, 이 때 $k$를 이 Alternating Set의 길이(length)라고 한다.

다소 생소하게 등장하는 개념이지만, 일단 다음과 같은 관계를 쉽게 관찰할 수 있다.

**Theorem.** $p$가 $f$의 최적 근사라고 하자. 그러면 $f-p$는 항상 길이 2의 Alternating Set을 가진다.

**pf.** 그러지 않다고 가정하자. 즉, 오차 $E = \lVert f-p \rVert$에 대해서 $f(x) - p(x) = E$를 만족하는 $x$가 유일하다고 하자. 또, $e = \min (f(x) - p(x)) > -E$라고 정의하자. 이제 $q = p + (E+e)/2$라고 하면, $q$가 $p$보다 더 최적의 근사가 된다. 이는 모순이다.

체비셰프는 최적 근사와 Alternating Set 사이에 더 심오하고 신기한 관계가 숨어 있음을 발견했다. 우리는 이 정리를 (Chebyshev) Equioscillation Theorem, 혹은 Alternating Theorem이라고 부른다. (우리말로는 교번 정리라고 부르는 모양이다.)

**Theorem.** (Chebyshev.) $p$가 $f$의 최적 근사인 것은 $f - p$가 길이 $n+2$의 Alternating Set을 가진다는 것과 동치이다.

**pf.** 증명을 쓸 수 있겠다면 좋겠지만... 여기에 전부 쓰기엔 너무 길다. 관심이 있는 독자라면 [A Short Course on Approximation Theory](http://fourier.math.uoc.gr/~mk/approx1011/carothers.pdf)의 챕터 4를 읽어보기를 바란다. 증명의 아이디어 자체는 위의 케이스와 크게 다르지 않지만, 조금 더 복잡한 과정이 필요하다.

**Collary.** 미니맥스 근사 문제의 해답은 유일하다.

**pf.** 그렇지 않다고 가정하자. 즉, 서로 다른 두 다항식 $p, q$가 $f$의 최적 근사라고 가정하자. 그렇다면, Equioscillation Theorem에 의해서 $r = (p + q)/2$도 $f$의 최적 근사가 된다. 이제 다시 $x_1, \cdots, x_{n+2}$를 $f-r$의 Alternating Set이라고 하자. 정의상,

$$
\lvert (f-p)(x_i) + (f-q)(x_i) \rvert = 2E
$$

이 때 물론 $E = \lVert f - p \rVert = \lVert f - q \rVert$이다. 따라서, $\lvert (f-p)(x_i) \rvert, \lvert (f-q)(x_i) \rvert$는 $E$보다 작거나 같다. 그런데 이 둘의 합은 $2E$보다 크고, 이것은 두 값이 $E$라는 것을 함의한다. 즉, $f-p$와 $f-q$의 Alternating Set은 같다. 그런데 Alternating Set은 $p$와 $q$를 각각 유일하게 결정하므로, 결국 $p=q$여야만 한다. 이는 모순이다.

이 정리를 이해하는 데 주의할 점은, $E$를 먼저 정하고 조건을 만족하는 $p$를 찾는 것으로 오해하면 안 된다는 것이다. 결국 $E$도 $p$에 의존하는 함수이기 때문이다. 그보다 더 정확한 비유는 다음과 같다. 주어진 $f$에 대해서, 먼저 그것을 대충 근사하는 다항식 $p$를 그린다. 그리고, $\lvert f-p \rvert$의 최댓값 $E$를 따라서 $f+E$와 $f-E$를 그린다. 이 때 두 선이 $p$와 $n+2$개 이하의 점에서 만난다면, 이 오차를 더 강하게 쥐어짜서 더 좋은 근사 $p'$를 찾을 수 있다는 것이 Equioscillation Theorem이다.

## Remez Algorithm

우리는 Equioscillation Theorem을 통해 미니맥스 근사 문제의 만족할 만할 답을 그럭저럭 찾아냈다. 답이 존재한다는 것과, 유일하다는 것, 그리고 그 대답의 필요충분조건까지 알아냈기 때문이다. 그런데, Alternating Set을 구하는 문제는 여전히 남아 있다.

$f$가 비교적 간단하고 $n$이 작을 때에는, 적당히 손으로 구해도 문제는 없다. 실제로 체비셰프는 직접 수기로 $x^n$을 $[-1, 1]$에서 최대 $n-1$차 다항식으로 근사하는 문제를 풀었고, 이를 체비셰프 다항식(Chebyshev Polynomial)이라고 부른다. 조금 더 복잡한 함수의 경우엔 컴퓨터의 도움을 받아야 하는데, 그 방법은 소련의 수학자 에브게니 레메즈(Evgeny Remez)가 1934년에 발표했다. 이것을 레메즈 알고리즘(Remez Algorithm)이라고 부른다.

레메즈 알고리즘은 드 라 발레푸생(de la Vallee-Poussin)의 정리로부터 출발한다.

**Theorem.** (de la Vallee-Poussin.) $f-p$가 $n+2$개의 점 $x_1, \cdots, x_{n+2}$에서 부호가 교차한다고 하자. (Alternating Set은 아니다.) 이 때, 다음이 성립한다.

$$
E \ge \min_{1 \le i \le n+2} \lvert f(x_i) - p(x_i) \rvert 
$$

Equioscillation Theorem에 따라서, 등호는 $p$가 최적 근사이고 $x_i$가 $f-p$의 Alternating Set일 때 성립한다.

드 라 발레푸생의 정리는 Alternating Set의 조건을 만족하는 점들이 아니라 구간 내의 아무 점에 대해서나 만족한다는 점을 생각하자. 레메즈 알고리즘은 우변을 최대화해나가는 점들을 반복적으로 찾아나간다. 그러다 등호 조건을 만족하는 점들을 찾는다면, 알고리즘을 종료한다.

**Definition.** (Remez Algorithm.) 다음 알고리즘은 주어진 $f$의 최적 근사 $p$, 오차 $E$, 그리고 $f-p$의 Alternating Set $x_1, \cdots, x_{n+2}$를 찾는다.

1. 구간 내의 점 $x_1, \cdots, x_{n+2}$를 임의로 잡는다. 보통 체비셰프 방정식의 해 $\cos(k/(n+2) \pi)$를 사용한다.
2. 미지수 $a_0, \cdots, a_n, E$에 대해서 연립방정식 $a_0 + a_1x_i + \cdots + a_nx_i^n + (-1)^iE = f(x_i)$을 푼다. 
3. $p = a_0+a_1x + \cdots +a_nx^n$으로 잡고, $f-p$의 극점들의 집합 $M$을 찾는다.
    - 만약 고른 점들 $x_1, \cdots, x_{n+2}$가 $M$과 같다면, 알고리즘을 종료한다.
    - 다르다면, $M$을 새로운 점들 $x_1, \cdots, x_{n+2}$로 잡고 2번으로 돌아간다.

3번에서, $M$은 결국 $\lvert f-p \rvert$의 값들을 최대화시키는 점들이다. 즉, 이 점에서 드 라 발레푸생 정리의 식의 우변이 최대가 된다는 것을 확인할 수 있다.

## Haar Condition

지금까지 우리는 $p$를 다항식으로 가정해 왔다. 그런데, 사실은 위에서 살펴본 내용 중에 다항식의 특수한 성질을 이용한 내용은 없었다. 즉, Equioscillation Theorem은 조금 더 일반적인 $p$에 대해서도 성립한다. 우리는 그 조건을 하르 조건(Haar Condition)이라고 한다.

**Definition.** (Haar Condition.) 서로 선형 독립인 연속 함수 $v_1, \cdots, v_n$에 대해서, 0이 아닌 함수 $p = a_1v_1 + \cdots + a_nv_n$이 언제나 $n-1$개의 해를 갖는다고 하자. 이 조건을 하르 조건(Haar Condition)이라고 하며, $v_1, \cdots, v_n$이 생성하는 공간을 체비셰프 시스템(Chebyshev system)이라고 한다.

당연히, $1, x, \cdots, x^n$은 하르 조건을 만족한다. 삼각함수들 또한 하르 조건을 만족함을 쉽게 확인할 수 있다.
