import cv2
from read_img import read_img

img = cv2.imread("hidden_board.png")
h, w = img.shape[:2]

step_h = h // 9
step_w = w // 9

ac_h = 0
for line in range(9):
    ac_w = 0
    for row in range(9):
        crop = img [ac_h : ac_h + step_h, ac_w : ac_w + step_w]
        crop = crop [3 : 52, 5 : 52]
        cv2.imwrite("temp.png", crop)
        ac_w += step_w

        print(read_img("temp.png"))

        cv2.imshow("win", crop)
        cv2.waitKey(0)
    ac_h += step_h
    print()