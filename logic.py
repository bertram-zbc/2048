# -*- coding: UTF-8 -*-  
'''
logic.py
2048游戏逻辑和移动规则
'''
def move(array,direction):
	if direction == 0:
		return moveLeft(array)
	elif direction == 1:
		return moveRight(array)
	elif direction == 2:
		return moveUp(array)
	else:
		return moveDown(array)

def moveLeft(array):
	#当前数组左移后能得到的新数组
	newArray = []
	for i in xrange(0,4):
		tmp = []
		for j in xrange(0,4):
			if array[i][j] != '':
				tmp.append(array[i][j])
		newTmp = []
		tag = False
		for x in xrange(0,len(tmp)):
			if tag == True:
				tag = False
				continue
			elif x == len(tmp) - 1:
				newTmp.append(tmp[x])
			elif tmp[x] == tmp[x+1]:
				newTmp.append(2*tmp[x])
				tag = True
			else:
				newTmp.append(tmp[x])
		for y in xrange(len(newTmp),4):
			newTmp.append('')
		newArray.append(newTmp)
	return newArray

def moveRight(array):
	newArray = []
	for i in xrange(0,4):
		tmp = []
		for j in xrange(0,4):
			if array[i][j]!='':
				tmp.append(array[i][j])
		newTmp = []
		tag = False
		for x in xrange(len(tmp)-1,-1,-1):
			if tag == True:
				tag = False
				continue
			elif x==0:
				newTmp.append(tmp[x])
			elif tmp[x] == tmp[x-1]:
				newTmp.append(2*tmp[x])
				tag = True
			else:
				newTmp.append(tmp[x])
		for y in xrange(len(newTmp),4):
			newTmp.append('')
		newTmp.reverse()
		newArray.append(newTmp)
	return newArray

def moveUp(array):
	newArray = []
	for i in xrange(0,4):
		tmp = []
		for j in xrange(0,4):
			if array[j][i]!='':
				tmp.append(array[j][i])
		newTmp = []
		tag = False
		for x in xrange(0,len(tmp)):
			if tag == True:
				tag = False
				continue
			elif x == len(tmp) - 1:
				newTmp.append(tmp[x])
			elif tmp[x] == tmp[x+1]:
				newTmp.append(2*tmp[x])
				tag = True
			else:
				newTmp.append(tmp[x])
		for y in xrange(len(newTmp),4):
			newTmp.append('')
		newArray.append(newTmp)
	return transposition(newArray) #矩阵转置，行列互换

def moveDown(array):
	newArray = []
	for i in xrange(0,4):
		tmp = []
		for j in xrange(0,4):
			if array[j][i]!='':
				tmp.append(array[j][i])
		newTmp = []
		tag = False
		for x in xrange(len(tmp)-1,-1,-1):
			if tag == True:
				tag = False
				continue
			elif x==0:
				newTmp.append(tmp[x])
			elif tmp[x] == tmp[x-1]:
				newTmp.append(2*tmp[x])
				tag = True
			else:
				newTmp.append(tmp[x])
		for y in xrange(len(newTmp),4):
			newTmp.append('')
		newTmp.reverse()
		newArray.append(newTmp)
	return transposition(newArray)

def transposition(array):
	#转置矩阵
	return [[row[col] for row in array] for col in xrange(len(array[0]))]




if __name__ == '__main__':
	#for test
	array = [[4,4,8,2],
			 [2,2,'',4],
			 ['','','',8],
			 [2,'','',16]]
	print moveDown(array)