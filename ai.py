# -*- coding: UTF-8 -*-  
'''
ai.py
'''
import time
import copy
import math
import sys
from logic import move
from strategies import canMove

MAX = sys.maxint #beta初始值
MIN = -MAX #alpha初始值

maxWeight = 1.0
emptyWeight = 2.7
monoWeight = 1.5
smoothWeight = 0.1

maxDepth = 4

def alpha_beta(array):
	#alpha-beta剪枝
	alpha = MIN
	beta = MAX
	directions = []
	for i in xrange(0,4):
		#得到所有可以移动的方向
		if canMove(array,i)==True:
			directions.append(i)
	direction = directions[0]
	for i in xrange(0,len(directions)):
		newArray = move(array,directions[i])
		tmp = alpha_beta_min(maxDepth-1,newArray,alpha,beta)
		if tmp > alpha:
			alpha = tmp
			direction = directions[i]
	return direction


def alpha_beta_min(depth,array,alpha,beta):
	if isFull(array)==True:
		return evaluation(array)
	if depth == 0:
		for i in xrange(0,4):
			for j in xrange(0,4):
				if array[i][j]=='':
					tmpArray = copy.deepcopy(array)
					tmpArray[i][j] = 2
					tmp = evaluation(tmpArray)
					if tmp < beta:
						beta = tmp
					if alpha > beta:
						return beta
					tmpArray[i][j] = 4
					tmp = evaluation(tmpArray)
					if tmp < beta:
						beta = tmp
					if alpha > beta:
						return beta
	else:
		for i in xrange(0,4):
			for j in xrange(0,4):
				if array[i][j]=='':
					tmpArray = copy.deepcopy(array)
					tmpArray[i][j] = 2
					tmp = alpha_beta_max(depth-1,tmpArray,alpha,beta)
					if tmp < beta:
						beta = tmp
					if alpha > beta:
						return beta
					tmpArray[i][j] = 4
					tmp = alpha_beta_max(depth-1,tmpArray,alpha,beta)
					if tmp < beta:
						beta = tmp
					if alpha > beta:
						return beta
	return beta

def alpha_beta_max(depth,array,alpha,beta):
	if depth == 0:
		for i in xrange(0,4):
			newArray = move(array,i)
			tmp = evaluation(newArray)
			if tmp > alpha:
				alpha = tmp
			if alpha > beta:
				return alpha
	else:
		for i in xrange(0,4):
			newArray = move(array,i)
			tmp = alpha_beta_min(depth-1,newArray,alpha,beta)
			if tmp > alpha:
				alpha = tmp
			if alpha > beta:
				return alpha
	return alpha



def isFull(array):
	#判断当前数组是否是满的
	for i in xrange(0,4):
		for j in xrange(0,4):
			if array[i][j]=='':
				return False
	return True

def isEnd(array):
	for i in xrange(0,4):
		if canMove(array,i)==True:
			return False
	return True

def evaluation(array):
	#评估函数
	if isEnd(array) == True:
		return -1000;
	return getMax(array) * maxWeight + \
		   getEmpty(array) * emptyWeight + \
		   getMono(array) * monoWeight + \
		   getSmooth(array) * smoothWeight \
		   #+ getBonus(array)

def getMax(array):
	#得到数组中最大值
	maxValue = 0
	for i in xrange(0,4):
		for j in xrange(0,4):
			if array[i][j]!='' and array[i][j] > maxValue:
				maxValue = array[i][j]
	return math.log(maxValue,2)

def getEmpty(array):
	#得到数组中为空的元素个数
	num = 0
	for i in xrange(0,4):
		for j in xrange(0,4):
			if array[i][j] == '':
				num += 1
	if num == 0:
		return 0
	return math.log(num)

def getSmooth(array):
	#计算数组的平滑度
	smooth = 0
	for i in xrange(0,3):
		for j in xrange(0,3):
			if array[i][j] != '':
				if array[i+1][j] != '':
					smooth -= abs(math.log(array[i][j],2)-math.log(array[i+1][j],2))
				if array[i][j+1] != '':
					smooth -= abs(math.log(array[i][j],2)-math.log(array[i][j+1],2))
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
				scores[0] += math.log(tmp[x+1],2) - math.log(tmp[x],2)
			else:
				scores[1] += math.log(tmp[x],2) - math.log(tmp[x+1],2)
	#上下方向
	for i in xrange(0,4):
		tmp = []
		for j in xrange(0,4):
			if array[j][i] != '':
				tmp.append(array[j][i])
		for x in xrange(0,len(tmp)-1):
			if tmp[x] > tmp[x+1]:
				scores[2] += math.log(tmp[x+1],2) - math.log(tmp[x],2)
			else:
				scores[3] += math.log(tmp[x],2) - math.log(tmp[x+1],2)
	return max(scores[0],scores[1])+ max(scores[2],scores[3])

def getBonus(array):
	#返回递减或递增的行列数
	num = 0
	for i in xrange(0,4):
		tmp = []
		for j in xrange(0,4):
			if array[i][j]!='':
				tmp.append(array[i][j])
		if isSeq(tmp) == True:
			num += 1
	for i in xrange(0,4):
		tmp=[]
		for j in xrange(0,4):
			if array[j][i] != '':
				tmp.append(array[j][i])
		if isSeq(tmp) == True:
			num += 1
	return num

def isSeq(array):
	increase = 1
	for i in xrange(0,len(array)-1):
		if array[i] > array[i+1]:
			increase = 0
			break
	decrease = 1
	for i in xrange(0,len(array)-1):
		if array[i] < array[i+1]:
			decrease = 0
			break
	result = increase or decrease
	if result == 1:
		return True
	else:
		return False




if __name__ == '__main__':
	#for test
	array = [['','','',''],
			 ['','','',''],
			 [2,'','',''],
			 [4,'','','']]

	start = time.time()
	print alpha_beta(array)
	end = time.time()
	print end-start
	
			