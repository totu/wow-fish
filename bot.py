#!/usr/bin/env python3

import cv2
from PIL import ImageGrab
import numpy as np
from skimage.metrics import structural_similarity
import win32api, win32con
import math
import time
from pynput.keyboard import Controller

LAST = None
AVG = 1.0
KB = Controller()

def set_cursor(height, width):
    try:
        col, row = cv2.findNonZero(LAST)[0][0]
        x = width + col
        y = height + row + 25
        win32api.SetCursorPos((x, y))
        time.sleep(1.0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
    except:
        pass

def caputer():
    img = ImageGrab.grab()
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    return frame

def crop(frame):
    height, width = frame.shape
    q_width = width // 3 
    q_height = height // 3
    cropped = frame[q_height:q_height*2, q_width:q_width*2]
    h, w = cropped.shape 
    assert h == q_height
    assert w == q_width
    return cropped

def cast_fishing():
    KB.press('1')
    KB.release('1')
    time.sleep(2.0)

if __name__ == "__main__":
    cv2.startWindowThread()
    cv2.namedWindow("test")

    while True:
        frame = caputer()
        cropped = crop(frame)
        edges = cv2.Canny(cropped, 50, 200)
        cv2.imshow("test", edges)

        if LAST is not None:
            score, _ = structural_similarity(LAST, edges, full=True)
            # print(score)
            if score == 1.0:
                cast_fishing()

            if math.floor(score*100) < math.floor(AVG*100):
                height, width = cropped.shape
                set_cursor(height, width)
            
            AVG = (AVG+score)/2
            print(AVG, "vs", score)


        while LAST is None:
            if cv2.waitKey(1) &0xFF == ord('q'):
                break

        LAST = edges
        if cv2.waitKey(1) &0xFF == ord('q'):
            break

    
    cv2.destroyAllWindows()