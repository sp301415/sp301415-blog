from PIL import Image, ImageDraw, ImageFont
from urllib.request import urlopen
from textwrap import wrap
import os

BOLD_FONT_URL = "https://cdn.jsdelivr.net/gh/spoqa/spoqa-han-sans@latest/Subset/SpoqaHanSansNeo/SpoqaHanSansNeo-Bold.ttf"
LIGHT_FONT_URL = "https://cdn.jsdelivr.net/gh/spoqa/spoqa-han-sans@latest/Subset/SpoqaHanSansNeo/SpoqaHanSansNeo-Regular.ttf"

OPENGRAPH_SIZE = (1200, 630)

OFFSET_X = 180
OFFSET_Y = 90

WHITE = "#fff"
BLACK = "#333"
GRAY = "#777"

BLOG_NAME = "Null Space"
DEFAULT_INFO_TEXT = "a blog by sp301415"
POSTPATH = "./_posts"

titlefont = ImageFont.truetype(urlopen(BOLD_FONT_URL), size=80)
infofont = ImageFont.truetype(urlopen(LIGHT_FONT_URL), size=40)

if not os.path.exists("./assets/ogimg"):
    os.mkdir("./assets/ogimg")

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

    titlelines = wrap(text, width=15)
    titleheight = 0
    for line in titlelines:
        titleheight += titlefont.getsize(line)[1]
    for line in titlelines[:-1]:
        titleheight += titlefont.getsize(line)[1] * 0.2
    infoheight = infofont.getsize(BLOG_NAME)[1]

    # Upper margin: OFFSET_Y, Lower margin: OFFSET_Y + infoheight
    # Center text accordingly.
    middle = (OFFSET_Y + (OPENGRAPH_SIZE[1] - OFFSET_Y)) / 2 - infoheight
    titlepos = middle - titleheight / 2

    y = titlepos
    for line in titlelines:
        res.text((OFFSET_X, y), line, font=titlefont, fill=BLACK)
        y += titlefont.getsize(line)[1] * 1.2

    res.text(
        (OFFSET_X, OPENGRAPH_SIZE[1] - OFFSET_Y - infoheight),
        BLOG_NAME,
        font=infofont,
        fill=GRAY,
    )

    filename = filename.strip(".md")
    filename = "-".join(filename.split("-")[3:])

    img.save(f"./assets/ogimg/{filename}.jpg")

# Generate Default image.
img = Image.new("RGB", OPENGRAPH_SIZE, color=WHITE)
res = ImageDraw.Draw(img)

titleheight = titlefont.getsize(BLOG_NAME)[1]
infoheight = infofont.getsize(DEFAULT_INFO_TEXT)[1]

middle = (OFFSET_Y + (OPENGRAPH_SIZE[1] - OFFSET_Y)) / 2 - infoheight
titlepos = middle - titleheight / 2

res.text((OFFSET_X, titlepos), BLOG_NAME, font=titlefont, fill=BLACK)
res.text(
    (OFFSET_X, OPENGRAPH_SIZE[1] - OFFSET_Y - infoheight),
    DEFAULT_INFO_TEXT,
    font=infofont,
    fill=GRAY,
)

img.save(f"./assets/ogimg/default.jpg")
