from cv2 import imwrite
import numpy as np
import cv2
import glob

for i, img in enumerate(glob.glob('*.jpg')):
    s = cv2.imread(img,0)
    s = cv2.medianBlur(s,5)

    # threshold 값 설정
    t = 100

    # Global Thresholding
    ret,th1 = cv2.threshold(s,t,255,cv2.THRESH_BINARY)

    # Adaptive Thresholding(MEAN)
    th2 = cv2.adaptiveThreshold(s,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,2)
    cv2.imwrite('sk_{}'.format(img), th2)
