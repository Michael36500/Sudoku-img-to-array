# Made by Michael36500

import cv2
# from tqdm import tqdm

# my idea here is to load predefined image of sudoku board and draw into it.
def save_board(board, name = "solved.png", where = "sudoku_sken.png"):
    # loads empty sudoku board into img
    img = cv2.imread(where)
    # gap equals space between each number
    h, w = img.shape[:2]
    gap = w // 9
    # gap = 52
    actual_line = -18
    # for line in tqdm(board):
    for line in board:
        if "-" in str(line):
            pass
        else:
            actual_char = 25
            actual_line += gap
            for char in line:
                if char == "|":
                    continue
                cv2.putText(img, str(char), (actual_char, actual_line), cv2.FONT_HERSHEY_PLAIN, 5, (0,0,0), 5)
                actual_char += gap
    cv2.imwrite("{}".format(str(name)), img)
