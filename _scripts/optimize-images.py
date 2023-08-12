from PIL import Image
import os

for path, _, names in os.walk("./static/images"):
    for name in names:
        if name.endswith(".jpg") or name.endswith(".png"):
            imgpath = os.path.join(path, name)
            img = Image.open(imgpath)
            img.save(imgpath, optimize=True)
