# -*- coding:utf-8 -*-
'''
action.py
手势操作的行为模拟
'''
import os
import re
import time

from config import *
from strategies import greddyStrategy

def moveUp():
	#向上移动手势操作
	cmd = 'adb shell input touchscreen swipe '+str(DOWNX)+' '+str(DOWNY)+' '+str(UPX)+' '+str(UPY)+' '+str(DURATION)
	#print cmd
	os.system(cmd)

def moveDown():
	cmd = 'adb shell input touchscreen swipe '+str(UPX)+' '+str(UPY)+' '+str(DOWNX)+' '+str(DOWNY)+' '+str(DURATION)
	#print cmd
	os.system(cmd)

def moveLeft():
	
	cmd = 'adb shell input touchscreen swipe '+str(RIGHTX)+' '+str(RIGHTY)+' '+str(LEFTX)+' '+str(LEFTY)+' '+str(DURATION)
	#print cmd
	os.system(cmd)

def moveRight():
	
	cmd = 'adb shell input touchscreen swipe '+str(LEFTX)+' '+str(LEFTY)+' '+str(RIGHTX)+' '+str(RIGHTY)+' '+str(DURATION)
	#print cmd
	os.system(cmd)

def move(array):
	#根据数组判断应该如何操作
	result = greddyStrategy(array)
	print "result: ", result
	if result == 0:
		moveLeft()
	elif result == 1:
		moveRight()
	elif result == 2:
		moveUp()
	else:
		moveDown()

if __name__ == '__main__':
	#for test
	array = [[2,'','',''],[16,'',2,''],[64,32,'',''],[4,2,'','']]
	lastArray = []
	lastMove = 0
	start = time.time()
	move(array, lastArray, lastMove)
	end = time.time()
	print end-start