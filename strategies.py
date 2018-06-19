# -*- coding:utf-8 -*-
'''
strategies.py
数组移动策略
'''

left = 0
right = 1
up = 2
down = 3

def greddyStrategy(array):
	#贪心算法，计算上下左右移动能取得的分数，并取最大分数对应的移动
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
		leftscore += calScore(tmpRow, left)
		rightscore += calScore(tmpRow, right)
		upscore += calScore(tmpCol, left)
		downscore += calScore(tmpCol, right)

	result.append(leftscore)
	result.append(rightscore)
	result.append(upscore)
	result.append(downscore)

	maxscore = 0
	tag = 0 #默认移动方向为向左移动
	for i in xrange(0,4):
		if result[i] > maxscore :
			maxscore = result[i]
			tag = i
	return tag

def calScore(array, leftRright):
	#计算每一行或者每一列可以得到的分数
	score = 0
	if leftRright == left:
		for i in xrange(0,len(array)-1):
			if array[i] == array[i+1]:
				score += long(array[i])
				i+=1
	else:
		for i in xrange(len(array)-1,0,-1):
			if array[i] == array[i-1]:
				score += long(array[i])
				i-=1
	return score
