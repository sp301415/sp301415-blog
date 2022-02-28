---
title: 최적의 다항 근사, 체비셰프 정리와 레메즈 알고리즘
tag: [수학]
description: 임의의 연속 함수를 다항식으로 근사하는 방법을 체비셰프 정리(Chebyshev Equioscillation Theorem)과 레메즈 알고리즘(Remez Algorithm)을 중심으로 알아봅니다.
---

이 글에서 다룰 문제는 아주 간단하다.

**Problem.** $[a, b]$에서 연속인 함수 $f$에 가장 가까운 다항식 $p$는 무엇일까?

더 진행하기 전에, 먼저 문제를 조금 더 엄밀하게 정의하고 넘어가자. 여기서 "가깝"다는 것은 보통 다음과 같은 Supreme Norm의 관점에서 말하는 것이다.

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

