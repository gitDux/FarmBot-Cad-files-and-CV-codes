#encoding：utf-8
#  黄色检测

import numpy as np
import argparse
import cv2
def zh_ch(string):    
	return string.encode("gbk").decode(errors="ignore")

frame = cv2.imread('weed2.jpg')

mask_kernel = cv2.GaussianBlur(frame,(5,5),0)
hsv = cv2.cvtColor(mask_kernel,cv2.COLOR_BGR2HSV) 
low_hsv = np.array([30,50,50],dtype = np.uint8)
upper_hsv = np.array([100,255,255],dtype = np.uint8)
mask = cv2.inRange(hsv,low_hsv,upper_hsv)

img1_bg = cv2.bitwise_and(frame,frame,mask = mask)

cv2.imshow(zh_ch("HSV"),cv2.resize(img1_bg,(320,320),0))
cv2.imshow('mask',cv2.resize(mask,(320,320),0))
'''
cv2.imshow('step1',cv2.resize(T1,(320,320),0))
cv2.imshow('step2',cv2.resize(T2,(320,320),0))
cv2.imshow('step3',cv2.resize(T3,(320,320),0))
'''
cv2.waitKey(0)
