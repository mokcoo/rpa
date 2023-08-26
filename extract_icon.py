import cv2
import numpy as np
import pyautogui
import time


screenshot = cv2.imread("screenshot.jpg")
screen_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

_,binary_image = cv2.threshold(screen_gray,127,255,cv2.THRESH_BINARY)
contours,_ = cv2.findContours(binary_image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
icons = []
for contour in contours:
    x,y,w,h = cv2.boundin-gRect(contour)
    icon = screenshot[y:y+h,x:x+w]
    icons.append((icon,(x,y)))