import pytesseract
from PIL import Image


def read_img(path):
    text = pytesseract.image_to_string(Image.open(path), config="--psm 13")
    # print(text)
    # print(len(text))
    # if len(text) != 1:
    #     print("tesseract detect less/more than one char")
    if "—" in text:
        text = 0
    # if not text in list('0123456789'):
    #     print("Tesseract detected characters, not ints")
    if not str(text) in list("0123456789"):
        print("tesseract detected non ints")
    return text

# print(read_img("hidden_board.png"))