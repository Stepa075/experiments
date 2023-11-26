from rembg import remove
from PIL import Image


def remove_bg():
    input_path = "cl.jpg"
    output_path = "output.png"
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)


if __name__ == '__main__':
    remove_bg()


