# -*- coding:utf-8 -*-
'''
run.py

'''
import os
import re
import cv2
import time
from imageProcess import getArray
from action import move

def run():

	lastArray = [] #记录上次移动的数组，用来判断上一步操作是否有效
	lastMove = 0 #

	while 1==1:
		#截图并读取
		os.system('adb shell screencap -p /sdcard/2048.png')
		os.system('adb pull /sdcard/2048.png')

		start = time.time()
		screen_image = cv2.imread('2048.png')
		end = time.time()
		print "load pic: ", end-start
		#转换为数组
		array = getArray(screen_image)
		start = time.time()
		print "process image: ", start-end
		#手势操作
		lastMove = move(array, lastArray, lastMove)
		lastArray = array
		end = time.time()
		print "calculate move: ", end-start

run()