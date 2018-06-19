# -*- coding: UTF-8 -*-  
'''
imageProcess.py
'''
from config import *

import pytesseract
import cv2

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

if __name__ == '__main__':
	#for test
	image = cv2.imread('test.png')
	record = getArray(image)
	print record