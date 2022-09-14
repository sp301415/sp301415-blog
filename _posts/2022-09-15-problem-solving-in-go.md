---
title: Go로 알고리즘 문제 풀기
tag: [개발]
---

요즘 다시 백준에 취미를 붙이면서 내가 좋아하는 언어 중 하나인 Go로 문제를 풀고 있다. 항상 파이썬과 C++ 그 어디 사이에 있는 언어를 원했는데, Go가 딱 그 빈 자리를 채워주는 느낌이다. 이 글에서는 Go로 PS 문제를 푸는데 유용한 여러 팁과 스니펫을 정리하고자 한다. <!--more-->

## Fast IO
Go에서 가장 많이 쓰이는 `fmt.Scan`, `fmt.Println`에는 기본적으로 buffer가 쓰이지 않는다. 흔히 말하는 Fast IO를 Go에서 쓰려면, `bufio` 패키지를 이용해야 한다. 내가 자주 쓰는 형식은 이렇다.

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

var stdio = bufio.NewReadWriter(
	bufio.NewReader(os.Stdin),
	bufio.NewWriter(os.Stdout),
)

func main() {
	defer stdio.Flush()

	var a, b int
	fmt.Fscan(stdio, &a, &b)
	fmt.Fprintln(stdio, a+b)
}
```

이제 `fmt.Scan(...)`, `fmt.Println(...)` 대신 `fmt.Fscan(stdio, ...)`, `fmt.Fprintln(stdio, ...)`를 쓰면 된다. 아래는 [백준 1000번 A+B](https://www.acmicpc.net/problem/1000)을 Go로 푼 예시이다.

```go
package main

import (
	"bufio"
	"os"
)

var stdio = bufio.NewReadWriter(
	bufio.NewReader(os.Stdin),
	bufio.NewWriter(os.Stdout),
)

func main() {
	defer stdio.Flush()

    // Code goes here
}
```

## 자료구조 스니펫
한 가지 거슬리는 점 중 하나는 Go의 내장 라이브러리에는 자료 구조에 대한 지원이 제대로 되어있지 않다는 점이다. 아마 제네릭이 최근에야 추가돼서 그런 거 같은데, 기본적인 큐나 스택도 없다는 것은 이해할 수 없다. 슬라이스로 대체해서 쓰라는 것 같긴 하지만. 하여간, 나는 간단한 코드 스니펫을 만들어서 돌려쓰고 있다. 백준은 Go 1.18이 지원되어서 제네릭을 쓸 수 있지만, 코드포스 같은 곳은 아직 지원하지 않으므로 참고하길 바란다.

### Queue
```go
type Queue[T any] []T

func (q Queue[T]) Front() T  { return q[0] }
func (q Queue[T]) Back() T   { return q[len(q)-1] }
func (q *Queue[T]) Push(x T) { *q = append(*q, x) }
func (q *Queue[T]) Pop() T {
	x := (*q)[0]
	*q = (*q)[1:]
	return x
}
```

### Stack
```go
type Stack[T any] []T

func (s Stack[T]) Front() T  { return s[0] }
func (s Stack[T]) Back() T   { return s[len(s)-1] }
func (s *Stack[T]) Push(x T) { *s = append(*s, x) }
func (s *Stack[T]) Pop() T {
	x := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return x
}
```

### Deque
```go
type Deque[T any] struct{ items *list.List }

func NewDeque[T any]() Deque[T]  { return Deque[T]{list.New()} }
func (d Deque[T]) Front() T      { return d.items.Front().Value.(T) }
func (d Deque[T]) Back() T       { return d.items.Back().Value.(T) }
func (d Deque[T]) PushFront(x T) { d.items.PushFront(x) }
func (d Deque[T]) PushBack(x T)  { d.items.PushBack(x) }
func (d Deque[T]) PopFront() T   { return d.items.Remove(d.items.Front()).(T) }
func (d Deque[T]) PopBack() T    { return d.items.Remove(d.items.Back()).(T) }
func (d Deque[T]) Len() int      { return d.items.Len() }
```

### Heap
Heap은 사용법이 좀 독특하다. [container/heap](https://pkg.go.dev/container/heap)의 도큐멘테이션을 참고하길 바란다. 또 heap의 constraint로 `constraints.Ordered`를 쓰면 좋겠지만, 이 또한 아직 표준 라이브러리로 편입되지 않은 관계로... 일단 `int`, `float64`, `string`만 지원한다.

```go
type Heap[T int | float64 | string] []T

func (h Heap[T]) Len() int           { return len(h) }
func (h Heap[T]) Less(i, j int) bool { return h[i] < h[j] }
func (h Heap[T]) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *Heap[T]) Push(x any)        { *h = append(*h, x.(T)) }
func (h *Heap[T]) Pop() any {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return x
}
```
