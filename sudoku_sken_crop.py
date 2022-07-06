import cv2

def crop_scan(where):
    img = cv2.imread(where)
    h, w = img.shape[:2]
    img = cv2.resize(img, (w // 2,h // 2))
    h, w = img.shape[:2]

    img = img[1 : int(h // 2.1), 1 : w]
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    img = cv2.blur(img, (5,5))
    _, img = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)
    cv2.imwrite("crop_img.png", img)
    # cv2.imshow("img",yimg)
    # cv2.waitKey(0)
