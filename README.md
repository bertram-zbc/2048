# 2048
adb + python + opencv 实现Android系统2048游戏控制脚本

适配1920x1080分辨率屏幕
适配游戏：<https://play.google.com/store/apps/details?id=com.tpcstld.twozerogame>
其他游戏和不同屏幕分辨率的手机需要修改`config.py`中的参数适配

```
$ python run.py
```



## 流程
- Android设备截取当前图像并发送到电脑
- 图像识别，得到对应的4x4矩阵
- 计算下一步的移动方向
- 执行命令


## 图像识别

先计算出每个方块数字的像素均值并保存，如下图是数字2对应的方块

<img src="https://github.com/bertram-zbc/2048/blob/master/info/sample2.png" width=128 height=128 />

在截取的图片中提取出16个方块，并一一与之前保存好的像素均值列表比较，像素均值相同的方块对应的数字就是图片中的数字，由于每次截图的方块图片并不是完全相同的，像素均值不会完全相等，需要设置一个误差范围，当像素均值的差小于这个误差值就认为是相等的

<img src="https://github.com/bertram-zbc/2048/blob/master/info/sample1.png" width=324 height=576 />


## 移动策略

### 贪心算法
分别计算当前状态向上下左右四个方向移动能够获得的分数，并取得分最高的作为移动方向，尝试后发现效果一般，只能得到128左右

### Minimax算法
由于状态并不是很多，全部遍历也不需要花多少时间，因此就没有使用alpha-beta剪枝。

**评估指标：**
- 最大值
- 空值的数量
- 判断当前矩阵是否“平滑”，即相邻两个方块的差值越大则越不平滑，如果所有方块的值均相同则是最平滑的
- 判断当前矩阵的左/右、上/下方向是否是严格递增或者递减的

**算法流程：**
![](https://github.com/bertram-zbc/2048/blob/master/info/sample3.png)
上图展示了遍历深度为2时的流程：
- 每次从玩家的回合开始，玩家将选择最优的情况，即子节点中的最大值
- 电脑的回合，游戏的逻辑是随机添加一个2或者4的方块，这里我们遍历电脑所有可能添加的位置，并取最坏的情况
- 玩家回合，直接评估得分并取最大值
从而判定当前状态应该向左移动


## Reference
<https://stackoverflow.com/questions/22342854/what-is-the-optimal-algorithm-for-the-game-2048>
<https://www.zhihu.com/question/23029850>
