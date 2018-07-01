# -*- coding:utf-8 -*-
'''
strategies.py
数组移动策略
'''
import time

left = 0
right = 1
up = 2
down = 3

def improved_greddyStrategy(array):
	#改进贪心算法
	can = [] #可以移动的方向
	forbidden = [] #禁止移动的方向
	maxRow = 0
	maxCol = 0
	maxValue = 0
	for i in xrange(0,4):
		for j in xrange(0,4):
			if array[i][j]!='' and array[i][j] > maxValue:
				maxValue = array[i][j]
				maxRow = i
				maxCol = j
	print maxRow,maxCol
	if array[0][3] == maxValue:
		maxRow = 0
		maxCol = 3
	elif array[3][0] == maxValue:
		maxRow = 3
		maxCol = 0
	elif array[3][3] == maxValue:
		maxRow = 3
		maxCol = 3

	if maxRow == 0 and maxCol == 0: #左上角
		can.append(left)
		can.append(up)
		forbidden.append(right)
		forbidden.append(down)
	elif maxRow == 0 and maxCol == 3:
		can.append(right)
		can.append(up)
		forbidden.append(left)
		forbidden.append(down)
	elif maxRow == 3 and maxCol == 0:
		can.append(left)
		can.append(down)
		forbidden.append(right)
		forbidden.append(up)
	elif maxRow == 3 and maxCol == 3:
		can.append(right)
		can.append(down)
		forbidden.append(left)
		forbidden.append(up)
	else:
		return getDirection(array,maxRow,maxCol)

	result = []
	leftscore = 0
	rightscore = 0
	upscore = 0
	downscore = 0
	for i in xrange(0,4):
		tmpRow = []
		tmpCol = []
		for j in xrange(0,4):
			if array[i][j]!='':
				tmpRow.append(array[i][j])
			if array[j][i] != '':
				tmpCol.append(array[j][i])
		leftscore += calScore(tmpRow)
		rightscore = leftscore
		upscore += calScore(tmpCol)
		downscore = upscore
	result.append(leftscore)
	result.append(rightscore)
	result.append(upscore)
	result.append(downscore)

	sequense = []
	if result[can[0]] >= result[can[1]]:
		sequense.append(can[0])
		sequense.append(can[1])
		sequense.append(forbidden[0])
		sequense.append(forbidden[1])
	else:
		sequense.append(can[1])
		sequense.append(can[0])
		sequense.append(forbidden[1])
		sequense.append(forbidden[0])


	direction = 0
	for i in xrange(0,4):
		direction = sequense[i]
		if canMove(array,direction)==True:
			break

	return direction

def getDirection(array,maxRow,maxCol):
	print "enter getDirection"
	if maxRow == 0 or maxRow == 3:
		print "maxRow"
		leftTag = 0
		for i in xrange(0,maxCol):
			if array[maxRow][i] != '':
				leftTag = 1
				break
		if leftTag == 0:
			return left
		rightTag = 0
		for i in xrange(maxCol+1,4):
			if array[maxRow][i] != '':
				rightTag = 1
				break
		if rightTag == 0:
			return right
	elif maxCol == 0 or maxCol == 3:
		print "maxCol"
		upTag = 0
		for i in xrange(0,maxRow):
			if array[i][maxCol]!='':
				upTag = 1
				break
		if upTag == 0:
			return up
		downTag = 0
		for i in xrange(maxRow+1,4):
			if array[i][maxCol]!='':
				downTag = 1
				break
		if downTag == 0:
			return down

	print "greddyStrategy"
	return greddyStrategy(array)
	

def greddyStrategy(array):
	#贪心算法，计算上下左右移动能取得的分数，并取最大分数对应的移动，返回需要移动的方向
	result = []
	leftscore = 0
	rightscore = 0
	upscore = 0
	downscore = 0

	for i in xrange(0,4):
		tmpRow = []
		tmpCol = []
		for j in xrange(0,4):
			if array[i][j]!='':
				tmpRow.append(array[i][j])
			if array[j][i] != '':
				tmpCol.append(array[j][i])
		leftscore += calScore(tmpRow)
		rightscore = leftscore
		upscore += calScore(tmpCol)
		downscore = upscore

	result.append(leftscore)
	result.append(rightscore)
	result.append(upscore)
	result.append(downscore)

	maxscore = 0
	direction = left #默认移动方向为向左移动
	for i in xrange(0,4):
		if result[i] > maxscore :
			maxscore = result[i]
			direction = i

	#print "direction: ", direction
	#判断当前移动是否有效动，如果无效则采取下一个操作
	for i in xrange(0,4):
		direction = (direction + i) % 4
		if canMove(array, direction) == True:
			break

	return direction

def calScore(array):
	#计算每一行或者每一列可以得到的分数
	#l左右移动分数是一样的，上下移动也是
	score = 0
	for i in xrange(0,len(array)-1):
		if array[i] == array[i+1]:
			score += long(array[i])
			i+=1
	return score

def canMove(array,direction):
	if direction == left:
		return canMoveLeft(array)
	elif direction == right:
		return canMoveRight(array)
	elif direction == up:
		return canMoveUp(array)
	else:
		return canMoveDown(array)

def canMoveLeft(array):
	#判断当前数组是否可以向左移动
	for i in xrange(0,4):
		for j in xrange(0,3):
			if array[i][j]=='' and array[i][j+1]!='':
				return True
	for i in xrange(0,4):
		tmpRow = []
		for j in xrange(0,4):
			if array[i][j]!='':
				tmpRow.append(array[i][j])
		cal = calScore(tmpRow)
		if cal != 0:
			return True
	return False

def canMoveRight(array):
	#判断当前数组是否可以向右移动
	for i in xrange(0,4):
		for j in xrange(3,0,-1):
			if array[i][j]=='' and array[i][j-1]!='':
				return True
	for i in xrange(0,4):
		tmpRow = []
		for j in xrange(0,4):
			if array[i][j]!='':
				tmpRow.append(array[i][j])
		cal = calScore(tmpRow)
		if cal != 0:
			return True
	return False

def canMoveUp(array):
	for i in xrange(0,4):
		for j in xrange(0,3):
			if array[j][i]=='' and array[j+1][i]!='':
				return True
	for i in xrange(0,4):
		tmpCol = []
		for j in xrange(0,4):
			if array[j][i]!='':
				tmpCol.append(array[j][i])
		cal = calScore(tmpCol)
		if cal != 0:
			return True
	return False

def canMoveDown(array):
	for i in xrange(0,4):
		for j in xrange(3,0,-1):
			if array[j][i] == '' and array[j-1][i] != '':
				return True
	for i in xrange(0,4):
		tmpCol = []
		for j in xrange(0,4):
			if array[j][i]!='':
				tmpCol.append(array[j][i])
		cal = calScore(tmpCol)
		if cal != 0:
			return True
	return False

	

if __name__ == '__main__':
	#for test
	array = [[4,8,2,4],
			 [64,8,32,2],
			 [4,2,4,8],
			 [2,8,4,2]]
	print canMoveLeft(array)
	print canMoveRight(array)
	print canMoveUp(array)
	print canMoveDown(array)
