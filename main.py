import pyautogui
from PIL import ImageGrab, Image
import numpy as np
import cv2
# screenWidth, screenHeight = pyautogui.size()
# currentMouseX, currentMouseY = pyautogui.position()
# pyautogui.moveTo(100, 150)

# cap = ImageGrab.grab(bbox=(157, 403, 629, 491))
# pyautogui.mouseInfo()
# print(cap)
# cap.save('din.png')

# numpydata = asarray(cap)
# print(numpydata)
# 244,457
# img = cv2.imread("din.png", 0)
# # show image
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
    # cap = ImageGrab.grab(bbox=(157, 403, 629, 491))
    # numpydata = asarray(cap)
    # if [247, 247, 247] in numpydata[244:245, 457:458]:
    #     pyautogui.press('up')
while True:
    cap = ImageGrab.grab(bbox=(157, 403, 629, 491))
    numpydata = np.array(cap)
    if [83, 83, 83] in numpydata[55:67, 125]:
        pyautogui.press('up')
