import cv2
from read_img import read_img
from sudoku_sken_crop import crop_scan
from tqdm import tqdm

def gen_grid(path = "sudoku_sken.png"):
    crop_scan(path)


    img = cv2.imread("crop_img.png")
    h, w = img.shape[:2]

    step_h = h // 9
    step_w = w // 9

    out = []

    ac_h = 0
    for _ in tqdm(range(9)):
        ac_w = 0
        temp = []
        for _ in range(9):
            crop = img [ac_h : ac_h + step_h, ac_w : ac_w + step_w]
            crop = crop [8 : 47, 10 : 47]
            cv2.imwrite("temp.png", crop)
            ac_w += step_w

            text = read_img("temp.png")
            if len(text) != 0:
                text = text [0]
            else:
                text = 0
            if text == "g":
                text = "9"
            if text == "‘":
                text = "5" 
            if text == "1" or text == "2" or text == "3" or text == "4" or text == "5" or text == "6" or text == "7" or text == "8" or text == "9":
                text = int(text)
            else:
                # print("|", end = "")
                text = 0
                
            # num = int(text)
            # print(read_img("temp.png"), end = "")
            # print(text, end = "  ")
            temp.append(text)
            # cv2.imshow("win", crop)
            # cv2.waitKey(100)
            # print(temp)
        out.append(temp)
        ac_h += step_h
        # print()
    # print()
    # print()

    print(out)
    return out
