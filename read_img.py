from logging import raiseExceptions
import pytesseract
from PIL import Image


def read_img(path):
    text = pytesseract.image_to_string(Image.open(path))
    if text == "":
        text = 0
    if text != "0" or text != "1" or text != "2" or text != "3" or text != "4" or text != "5" or text != "6" or text != "7" or text != "8" or text != "9":
        print("Tesseract detected characters, not ints")
    return text

# read_img("test.png")