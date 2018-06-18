# -*- coding:utf-8 -*-
'''
action.py
手势操作的行为模拟
'''
import os
import re
import time

from config import *

def moveUp():
	#向上移动手势操作
	cmd = 'adb shell input swipe '+str(DOWNX)+' '+str(DOWNY)+' '+str(UPX)+' '+str(UPY)+' '+str(DURATION)
	print cmd
	os.system(cmd)

def moveDown():
	cmd = 'adb shell input swipe '+str(UPX)+' '+str(UPY)+' '+str(DOWNX)+' '+str(DOWNY)+' '+str(DURATION)
	print cmd
	os.system(cmd)

def moveLeft():
	cmd = 'adb shell input swipe '+str(RIGHTX)+' '+str(RIGHTY)+' '+str(LEFTX)+' '+str(LEFTY)+' '+str(DURATION)
	print cmd
	os.system(cmd)

def moveRight():
	cmd = 'adb shell input swipe '+str(LEFTX)+' '+str(LEFTY)+' '+str(RIGHTX)+' '+str(RIGHTY)+' '+str(DURATION)
	print cmd
	os.system(cmd)

def move(array):
	#根据数组判断应该如何操作
	moveUp()

if __name__ == '__main__':
	#for test
	moveUp()
	#time.sleep(2)
	moveDown()
	#time.sleep(2)
	moveLeft()
	#time.sleep(2)
	moveRight()