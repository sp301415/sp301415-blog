---
title: kramdown에서의 KaTeX 서버 측 렌더링 구현기
tags: [개발]
description: Jekyll과 kramdown에서 KaTeX의 서버 측 렌더링 기능을 구현하면서, 삽질한 부분들을 정리합니다.
---

얼마 전 블로그를 새로 개발했다. 원래는 [Pixyll](https://github.com/johno/pixyll) 테마를 적당히 수정해서 쓰고 있었는데, HTML과 CSS를 더 배우고 싶기도 했고, 나만의 공간을 직접 꾸며보고 싶다는 생각에 밑바닥부터 다시 개발한 것이다. 

이 블로그에는 수학 글이 자주 올라오기 때문에 수식 렌더링 기능이 필수적이다. 보통 이것은 [MathJax](https://www.mathjax.org/)나 [KaTeX](https://katex.org/) 같은 라이브러리의 자동 렌더링 기능을 이용해서 구현한다. 그렇지만 이것은 결국 클라이언트에서 도는 자바스크립트 파일이고, 단순함에 목숨을 건 나는 이것이 탐탁치 않았다(...) KaTeX은 서버 측 렌더링 기능도 지원하기 때문에, 별 생각없이 이 방법을 택했다.

다행스럽게도 Jekyll에서는 이 기능을 쉽게 구현할 수 있는 젬이 두 개 있다. 하나는 [katex](https://github.com/glebm/katex-ruby)에 기반한 [kramdown-math-katex](https://github.com/kramdown/math-katex)이고, 다른 하나는 [sskatex](https://github.com/ccorn/sskatex/)에 기반한 [kramdown-math-sskatex](https://github.com/kramdown/math-sskatex)이다. 전자의 경우 자바스크립트와 CSS 파일이 내장되어 있어 편하게 쓸 수 있지만, 구버전의 KaTeX가 강제된다. 후자의 경우 관리가 중단되었지만, 필요한 자바스크립트와 CSS 파일 등을 직접 설정해 줄 수 있다. 나는 둘 중 후자의 젬을 선택했다. 관리가 중단되었다고는 해도 코드가 워낙 간단해서 작동하지 않을 염려는 별로 없는 것 같았고, 최신 버전의 KaTeX를 쓰는 것이 더 중요하다고 생각했다.

## JS / CSS 설정하기

설정법은 간단하다. `Gemfile`에 `gem "kramdown-math-sskatex"`을 추가하고 `bundle install`을 실행하면 젬을 다운받을 수 있다. 자바스크립트와 CSS, 폰트 파일의 경우엔 항상 최신 버전을 다운받도록 플러그인을 짰다. 말은 쉽지만, 루비는 처음이라 꽤나 고생했다.

```ruby
require "open-uri"


KATEX_URL = "https://cdn.jsdelivr.net/npm/katex@latest/dist"

# Download css to _katex.scss
katex_css = URI.open("#{KATEX_URL}/katex.min.css").read()
File.write("_sass/_katex.scss", katex_css)

# Download fonts
CSS_PATH = "assets/css"
Dir.mkdir(CSS_PATH + "/fonts") unless File.exists?(CSS_PATH + "/fonts")
katex_css.scan(/src:url\((.*?)\)/).each { |font| 
    File.write("#{CSS_PATH}/#{font[0]}", URI.open("#{KATEX_URL}/#{font[0]}").read())
}

# Download katex
katex_js = URI.open("#{KATEX_URL}/katex.min.js").read()
JS_PATH = "_plugins"
Dir.mkdir(JS_PATH) unless File.exists?(JS_PATH)
File.write("#{JS_PATH}/katex.js", katex_js)
```

이제 이 파일을 `_plugins` 디렉토리에 넣으면, Jekyll이 알아서 컴파일 전에 이 파일을 실행시킨다. 마지막으로, CSS에 `@include 'katex';`를 적어주고, `_config.yml`에 

```yml
kramdown:
  math_engine: sskatex
  math_engine_opts:
    katex_js: _plugins/katex.js
```

설정을 넣어주면 된다.

## 수식 인라인 기호 설정하기

일반 LaTeX을 포함한 내가 아는 거의 모든 수식 에디터는 `$...$`을 인라인 수식 렌더링 기호로 쓴다. KaTeX의 자동 렌더링 스크립트에는 `delimiter` 옵션을 통해 이것을 조절할 수 있다. 하지만, Jekyll이 사용하는 마크다운 엔진인 kramdown에서는 무조건 `$$...$$`을 인라인 수식 기호로 사용해야 한다. 정확히 말하면, 일반 문단 사이에 섞인 `$$...$$`는 인라인 수식으로, 독립된 블록은 블록 수식으로 파싱된다. 

나는 이게 싫었다. 작성 습관을 바꾸는 것도 고역이었지만, 글을 쓸 때 애용하는 VSCode의 마크다운 렌더러에서는 `$$...$$`을 모조리 블록 수식으로 파싱하기 때문에 블로그와 다르게 보이는 것도 마음에 들지 않았다. 인라인 수식이 많은 글은 VSCode에서는 거의 볼 수도 없을 정도였다. 구글링을 좀 해 보니, kramdown에 [등록된 이슈](https://github.com/gettalong/kramdown/issues/672) 중 정확히 나와 같은 문제를 겪는 사람이 있었다. 하지만 이슈에 달린 개발자의 답글을 보면 이것은 의도된 기능이며 바꿀 계획도 없다고 한다. ㅠㅠ 

그렇다고 좌절할 수는 없다. 처음에는 Jekyll의 Hook 기능을 써서 직접 파서를 짜보기로 했다. 파싱까지는 regex 매칭을 이용하면 크게 어렵지는 않았지만, 문제는 예외 케이스가 너무 많다는 것이었다. 일단 코드 블럭 안의 달러는 무시해야 하고, 앞에 escape 문자를 붙인 달러 `\$`도 무시해야 하고... 등등.

결국 내가 선택한 방법은 kramdown의 파서를 직접 연장하는 것이었다. kramdown의 [parser.rb](https://github.com/gettalong/kramdown/blob/master/lib/kramdown/parser/kramdown.rb)를 보면, 간단한 설명과 함께 파서 구현 예제가 적혀 있다. 이것을 참고해서 루비 파일을 작성했다.

```ruby
require 'kramdown/parser/kramdown'
require 'kramdown-parser-gfm'

class Kramdown::Parser::GFMKatex < Kramdown::Parser::GFM
    # Override inline math parser
    @@parsers.delete(:inline_math)

    INLINE_MATH_START = /(\$+)([^\$]+)(\$+)/m

    def parse_inline_math
        start_line_number = @src.current_line_number
        @src.pos += @src.matched_size
        @tree.children << Element.new(:math, @src.matched[1..-2], nil, category: :span, location: start_line_number)
    end

    define_parser(:inline_math, INLINE_MATH_START, '\$')
end
```

kramdown의 파서는 `@@parser` 변수에 파서의 목록을 넣어 놓는다. 그렇기 때문에 여기에서 내장된 `:inline_math` 파서를 제거한 다음 직접 만든 새로운 파서를 끼워넣기만 하면 된다. 위와 같이 이 파일을 `_plugins` 디렉토리에 저장하고, `_config.yml`의 `kramdown` 밑에 새로운 파서를 지정해 준다.

```yml
kramdown:
  input: GFMKatex
```

이제 일반 문단에서 `$...$`를 이용해서 인라인 수식을 작성할 수 있다. 원래 이슈에도 설명과 함께 이 코드를 첨부했고, 감사인사와 함께 따봉을 받았다. 문제 해결!

## 결론

처음에는 간단할 줄 알았는데 어쩌다 보니 kramdown의 소스코드까지 분석하게 됐다. Gatsby같은 NodeJS 기반의 프레임워크에서는 그냥 플러그인 하나 추가하는 것으로 쉽게 끝나는 것 같던데, Jekyll은 루비 기반이다 보니 자바스크립트와는 상성이 잘 맞지 않는 듯하다. 길게 보면 결국 Gatsby로 넘어가는 것이 좋을 것 같지만, 자바스크립트를 언제 배울 수 있을지... 일단 내가 원하는 기능은 어찌저찌 구현이 되었으니 블로그 글이나 열심히 써야겠다.