import cv2

def crop_scan(where = "sudoku_sken.png"):
    img = cv2.imread(where)
    h, w = img.shape[:2]
    img = cv2.resize(img, (w // 2,h // 2))
    h, w = img.shape[:2]

    img = img[1 : int(h // 2.1), 1 : w]

    cv2.imwrite("cropped_scan.png", img)
# cv2.imshow("img",img)

# cv2.waitKey(0)