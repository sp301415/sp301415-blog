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
