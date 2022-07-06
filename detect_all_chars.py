import cv2
from read_img import read_img

img = cv2.imread("cropped_scan.png")
h, w = img.shape[:2]

step_h = h // 9
step_w = w // 9

out = []

ac_h = 0
for line in range(9):
    ac_w = 0
    temp = []
    for row in range(9):
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
        text = int(text)
        # num = int(text)
        # print(read_img("temp.png"), end = "")
        print(text, end = "  ")
        temp.append(text)
        # cv2.imshow("win", crop)
        # cv2.waitKey(100)
    out.append(temp)
    ac_h += step_h
    print()
print()
print()

print(out)