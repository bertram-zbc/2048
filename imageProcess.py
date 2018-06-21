# -*- coding: UTF-8 -*-  
'''
imageProcess.py
'''
from config import *

import pytesseract
import cv2
import time
import numpy as np
import cmath

'''
img = cv2.imread('test.png')

#part1 = img[618:834, 63:279]
part1 = img[864:846+216, 70:270]

cv2.imwrite("part1.png", part1)

print(pytesseract.image_to_string(part1, config="-psm 6"))
'''

def getArray(image):
	record = [] #转化为的二维数组
	for i in range(0,4):
		line = [] #每一行的结果
		for j in range(0,4):
			beginY = STARTY + (SQUARE+MARGIN) * i
			endY = beginY + SQUARE
			beginX = STARTX + (SQUARE+MARGIN) * j
			endX = beginX + SQUARE
			part = image[beginY:endY, beginX:endX]
			#cv2.imwrite("part"+str(i*4+j)+".png", part)
			text = pytesseract.image_to_string(part, config="-psm 9")
			#print text
			line.append(text)
		record.append(line)
	return record

def getArray2(image):
	#图像识别算法2，不通过pytesseract，直接比较图像像素均值
	record = []
	for i in range(0,4):
		line = []
		for j in range(0,4):
			beginY = STARTY + (SQUARE+MARGIN) * i
			endY = beginY + SQUARE
			beginX = STARTX + (SQUARE+MARGIN) * j
			endX = beginX + SQUARE
			part = image[beginY:endY, beginX:endX]
			text = getValue(part)
			line.append(text)
		record.append(line)
	return record

def getValue(image):
	#根据图片的像素均值判断图片中的数值
	pixal_mean = np.mean(image)
	for x in xrange(0,len(pixal_means)):
		if abs(pixal_means[x] - pixal_mean) <= 0.1:
			return pixal_values[x]
	return ''

if __name__ == '__main__':
	#for test
	start = time.time()
	image = cv2.imread('test.png')
	record = getArray2(image)
	end = time.time()
	print record
	print "running time: ", end-start
