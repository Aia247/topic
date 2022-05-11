from PIL import Image
import numpy as np
import json


def one():
    json_path = "boxes.json"
    data = json.load(open(json_path, "r", encoding="utf-8"))
    for i in range(len(data["boxes"])):
        if data["boxes"][i]["name"] == "box_b":
            print(data["boxes"][i]["rectangle"])

            return data["boxes"][i]["rectangle"]


def resize_a(img, size):
    img = img.resize(size, Image.ANTIALIAS)

    return img


def resize_b(img, size):
    canvas = Image.new("RGB", size=size, color="#FFFFFF")
    target_width, target_height = size
    width, height = img.size
    offset_x = 0
    offset_y = 0
    if height > width:
        height_ = target_height  # 直接将高调整为目标尺寸
        scale = height_ / height  # 计算高具体调整了多少，得出一个放缩比例
        width_ = int(width * scale)  # 宽以相同的比例放缩
        offset_x = (target_width - width_) // 2
    else:
        width_ = target_width
        scale = width_ / width
        height_ = int(height * scale)
        offset_y = (target_height - height_) // 2
    img = img.resize((width_, height_), Image.BILINEAR)  # 将高和宽放缩
    canvas.paste(img, box=(offset_x, offset_y))

    return canvas


a = one()

pattern = input("请输入填充的模式：")
image1 = Image.open("dog.jpg")
image2 = Image.open("1.jpg")
target__size = (a["right_bottom"][1] - a["left_top"][1], a["right_bottom"][0] - a["left_top"][0])

if pattern == "a":
    res = resize_a(image1, target__size)
elif pattern == "b":
    res = resize_b(image1, target__size)
mat = np.array(res)
mat1 = np.array(image2)
mat1[100:200, 100:300, :] = mat
im = Image.fromarray(mat1)
im.show()