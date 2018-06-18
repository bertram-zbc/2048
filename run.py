# -*- coding:utf-8 -*-
'''
run.py

'''
import os
import re
import cv2

from imageProcess import getArray
from action import move

def run():
	while 1==1:
		#截图并读取
		os.system('adb shell screencap -p /sdcard/2048.png')
		os.system('adb pull /sdcard/2048.png')
		screen_image = cv2.imread('2048.png')
		#转换为数组
		array = getArray(screen_image)
		#手势操作
		move(array)

run()