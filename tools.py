# -*- coding: UTF-8 -*-  
'''
获取样式图片
并计算出样式图片的像素均值用于比较
'''

import pytesseract
import cv2
import time
import numpy as np

from config import *

def getImage(image):
	record = [] 
	for i in range(0,4):
		line = [] 
		for j in range(0,4):
			beginY = STARTY + (SQUARE+MARGIN) * i
			endY = beginY + SQUARE
			beginX = STARTX + (SQUARE+MARGIN) * j
			endX = beginX + SQUARE
			part = image[beginY:endY, beginX:endX]
			cv2.imwrite("./parts/part"+str(i*4+j)+".png", part)
	return record


img = cv2.imread("2048.png")
getImage(img)
for x in xrange(0,16):
	file = "./parts/part"+str(x)+".png"
	image = cv2.imread(file)
	print np.mean(image)