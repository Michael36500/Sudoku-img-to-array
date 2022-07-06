import cv2
from cv2 import THRESH_BINARY

def crop_scan(where = "sudoku_sken.png"):
    img = cv2.imread(where)
    h, w = img.shape[:2]
    img = cv2.resize(img, (w // 2,h // 2))
    h, w = img.shape[:2]

    img = img[1 : int(h // 2.1), 1 : w]
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    img = cv2.blur(img, (5,5))
    _, img = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)
    cv2.imwrite("cropped_scan.png", img)
    cv2.imshow("img",img)
    cv2.waitKey(0)
crop_scan()
