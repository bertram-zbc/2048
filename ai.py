# -*- coding: UTF-8 -*-  
'''
ai.py
'''
from logic import move
from strategies import canMove
import copy

maxWeight = 1.0
emptyWeight = 2.7
monoWeight = 1.0
smoothWeight = 0.1

maxDepth = 4


def alpha_beta(array):
	#alpha-beta剪枝算法，目前只是全部计算，还没有实现剪枝
	scores = [0,0,0,0]
	for i in xrange(0,4):
		newArray = move(array,i)
		scores[i] = alpha_beta_min(maxDepth-1, newArray)
	print scores
	#最大值对应的方向就是应该移动的方向
	maxValue = scores[0]
	sequence = []
	for i in xrange(0,4):
		maxValue = -100000
		index = 0
		for j in xrange(0,4):
			if scores[j] > maxValue:
				maxValue = scores[j]
				index = j
		scores[index] = -100000
		sequence.append(index)
	print sequence
	direction = 0
	for i in xrange(0,4):
		if canMove(array,sequence[i]) == True:
			direction = sequence[i]
			break
	print direction
	return direction

def alpha_beta_min(depth, array):
	#极大极小值算法中的极小值函数
	scores = []
	if depth == 0:
		for i in xrange(0,4):
			for j in xrange(0,4):
				if array[i][j]=='':
					tmpArray = copy.deepcopy(array)
					tmpArray[i][j] = 2
					scores.append(evaultion(tmpArray))
					tmpArray[i][j] = 4
					scores.append(evaultion(tmpArray))
	else:
		for i in xrange(0,4):
			for j in xrange(0,4):
				if array[i][j]=='':
					tmpArray = copy.deepcopy(array)
					tmpArray[i][j] = 2
					scores.append(alpha_beta_max(depth-1,tmpArray))
					tmpArray[i][j] = 4
					scores.append(alpha_beta_max(depth-1,tmpArray))
	if len(scores) == 0:
		return 0
	return min(scores)

def alpha_beta_max(depth, array):
	#极大极小值算法的极大值函数
	scores = [0,0,0,0]
	if depth == 0:
		for i in xrange(0,4):
			newArray = move(array,i)
			scores[i] = evaultion(newArray)
	else:
		for i in xrange(0,4):
			newArray = move(array,i)
			scores[i] = alpha_beta_min(depth-1,newArray)
	return max(scores)



def evaultion(array):
	#评估函数
	return getMax(array) * maxWeight + \
		   getEmpty(array) * emptyWeight + \
		   getMono(array) * monoWeight + \
		   getSmooth(array) * smoothWeight

def getMax(array):
	#得到数组中最大值
	maxValue = 0
	for i in xrange(0,4):
		for j in xrange(0,4):
			if array[i][j]!='' and array[i][j] > maxValue:
				maxValue = array[i][j]
	return maxValue

def getEmpty(array):
	#得到数组中为空的元素个数
	num = 0
	for i in xrange(0,4):
		for j in xrange(0,4):
			if array[i][j] == '':
				num += 1
	return num

def getSmooth(array):
	#计算数组的平滑度
	smooth = 0
	for i in xrange(0,3):
		for j in xrange(0,3):
			if array[i][j] != '':
				if array[i+1][j] != '':
					smooth -= abs(array[i][j]-array[i+1][j])
				if array[i][j+1] != '':
					smooth -= abs(array[i][j]-array[i][j+1])
	return smooth

def getMono(array):
	#计算单调性，判断每行或者每列是否是递增或者递减的
	scores = [0,0,0,0] #四个方向的分数
	#左右方向
	for i in xrange(0,4):
		tmp = []
		for j in xrange(0,4):
			if array[i][j]!='':
				tmp.append(array[i][j])
		for x in xrange(0,len(tmp)-1):
			if tmp[x] > tmp[x+1]:
				scores[0] += tmp[x+1] - tmp[x]
			else:
				scores[1] += tmp[x] - tmp[x+1]
	#上下方向
	for i in xrange(0,4):
		tmp = []
		for j in xrange(0,4):
			if array[j][i] != '':
				tmp.append(array[j][i])
		for x in xrange(0,len(tmp)-1):
			if tmp[x] > tmp[x+1]:
				scores[2] += tmp[x+1]-tmp[x]
			else:
				scores[3] += tmp[x] - tmp[x+1]
	return max(scores[0],scores[1])+ max(scores[2],scores[3])





if __name__ == '__main__':
	#for test
	array = [['',4,8,2],
			 ['','','',4],
			 ['','','',8],
			 ['','','',16]]
	print alpha_beta(array)
	
			