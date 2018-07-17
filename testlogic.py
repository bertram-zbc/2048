# -*- coding:utf-8 -*-
'''
testlogic.py
测试上下左右移动的逻辑是否正确
'''

import os
import re
import cv2
import time
from imageProcess import getArray,getArray2
from logic import *

#单步操作
os.system('adb shell screencap -p /sdcard/2048.png')
os.system('adb pull /sdcard/2048.png')

screen_image = cv2.imread('2048.png')

#转换为数组
array = getArray2(screen_image)

print 'left: ',moveLeft(array)
print 'right: ',moveRight(array)
print 'up: ',moveUp(array)
print 'down: ',moveDown(array)
