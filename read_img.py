import pytesseract
from PIL import Image


def read_img(path):
    text = pytesseract.image_to_string(Image.open(path), config="--psm 13")
    # print(text)
    # print(len(text))
    # if len(text) == 1:
    #     print("tesseract detect less/more than one char")
    # if "—" in text:
    #     text = 0
    # if not str(text) in list('0123456789'):
        # print("Tesseract detected characters, not ints")
        # print("something different than ints")
        # text = 0
    # if not str(text) in list("0123456789"):
        # print("tesseract detected non ints")
        # text = 0
    # print(text, end = "")
    # print("T", text, end = "")
    text.replace(" ", "")
    text.replace("\n", "")
    # print("text", text)
    # if text == "0" or text == "1" or text == "2" or text == "3" or text == "4" or text == "5" or text == "6" or text == "7" or text == "8" or text == "9":
    #     text = text
    # else:
    #     text = 0

    # print("afte", text)
    # if text == "0" or text == "1" or text == "2" or text == "3" or text == "4" or text == "5" or text == "6" or text == "7" or text == "8" or text == "9":
    #     text = int(text)
    # else:
    #     # text = 0
    #     print("|", end = "")
        
        
    return text

# print(read_img("hidden_board.png"))