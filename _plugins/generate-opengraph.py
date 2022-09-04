from PIL import Image, ImageDraw, ImageFont
from urllib.request import urlopen
from textwrap import wrap, fill
import os

BOLD_FONT_URL = "https://cdn.jsdelivr.net/npm/pretendard@latest/dist/public/static/Pretendard-Bold.otf"
LIGHT_FONT_URL = "https://cdn.jsdelivr.net/npm/pretendard@latest/dist/public/static/Pretendard-Regular.otf"

OPENGRAPH_SIZE = (1200, 630)

OFFSET_X = 180
OFFSET_Y = 90

WHITE = "#fff"
BLACK = "#333"
GRAY = "#777"

BLOG_NAME = "Null Space"
DEFAULT_INFO_TEXT = "sp301415의 블로그"
POSTPATH = "./_posts"

title_font = ImageFont.truetype(urlopen(BOLD_FONT_URL), size=80)
info_font = ImageFont.truetype(urlopen(LIGHT_FONT_URL), size=40)
info_height = info_font.getbbox(BLOG_NAME)[3]

if not os.path.exists("./assets/opengraph"):
    os.mkdir("./assets/opengraph")

for filename in os.listdir(POSTPATH):
    if not filename.endswith(".md"):
        continue

    # Make image
    img = Image.new("RGB", OPENGRAPH_SIZE, color=WHITE)
    res = ImageDraw.Draw(img)

    # Generate text to write
    text = ""
    with open(POSTPATH + "/" + filename, "r") as f:
        for line in f.readlines():
            if line.startswith("title"):
                text = line[line.find(":") + 1 :].strip()
                break

    wrap_width = len(text)  # sane default value
    while True:
        title = wrap(text, wrap_width)
        title_fits = [
            title_font.getlength(t) <= OPENGRAPH_SIZE[0] - 2 * OFFSET_X for t in title
        ]
        if all(title_fits):
            break
        wrap_width -= 1

    title = fill(text, wrap_width)

    res.multiline_text(
        xy=(OFFSET_X, (OFFSET_Y + (OPENGRAPH_SIZE[1] - OFFSET_Y)) / 2 - info_height),
        text=title,
        font=title_font,
        fill=BLACK,
        anchor="lm",
        spacing=25,
    )

    res.text(
        xy=(OFFSET_X, OPENGRAPH_SIZE[1] - OFFSET_Y - info_height),
        text=BLOG_NAME,
        font=info_font,
        fill=GRAY,
        anchor="lm",
        spacing=25,
    )

    filename = filename.strip(".md")
    filename = "-".join(filename.split("-")[3:])

    img.save(f"./assets/opengraph/{filename}.png")

# Generate Default image.
img = Image.new("RGB", OPENGRAPH_SIZE, color=WHITE)
res = ImageDraw.Draw(img)

res.multiline_text(
    xy=(OFFSET_X, (OFFSET_Y + (OPENGRAPH_SIZE[1] - OFFSET_Y)) / 2 - info_height),
    text=BLOG_NAME,
    font=title_font,
    fill=BLACK,
    anchor="lm",
    spacing=25,
)

res.text(
    xy=(OFFSET_X, OPENGRAPH_SIZE[1] - OFFSET_Y - info_height),
    text=DEFAULT_INFO_TEXT,
    font=info_font,
    fill=GRAY,
    anchor="lm",
    spacing=25,
)

img.save(f"./assets/opengraph/default.png")
