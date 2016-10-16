# 算法测试程序 sort.py 文档
## 背景
在处理大量数据时，不同算法的时间开销差距很大，本程序对7种常见的排序算法(冒泡/选择/插入/希尔/归并/快速/堆排序)进行比较和验证，并向用户提供了调整待排数组的方法。

## 用法
如果想对某种排序进行测试，可以输入
> python sort.py bubble 1000 reversed

最后三个参数 bubble/1000/reversed 为用户自定义部分。

- 『bubble』：算法名称，一共有8种选项：bubble/selection/insertion/shell/merge/quick/heap/all。除最后一个all为所有算法均参与测试外，其他均为单一算法测试。

- 『1000』：数组规模，可输入任意正整数，生成该规模的随机排序数组。

- 『reversed』：可选项，用以生成一个逆序数组，测试某些算法在极端情况的效率（例如快速排序）。

截图：
![屏幕快照 2016-10-16 下午3.41.01](media/14765493497422/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202016-10-16%20%E4%B8%8B%E5%8D%883.41.01.png)

## 数组的生成
数组通过numpy生成，默认所有元素为1000000000以内正整数，可以通过调节参数改变元素的范围：

```
origin_list = list(nprnd.randint(100000000, size=sort_number))
```

## 各算法的实现
所有算法继承自基类Sort，可以通过self.get_time()方法来获取运行时间

	class Sort(object): 
    	def __init__(self):
        	self.time = 0
    	def sort(self, x):
        	pass
    	def get_time(self):
        	return self.time

每个算法子类有一个以算法英文命名的实例，可以用实例方法测试排序和提取运行时间,如冒泡算法的实例为：

```
bubble = Bubble()
bubble.sort(bubble_list) # 排序
bubble.get_time() # 获取冒泡算法的运行时间
```

## 结果验证
首先将生成的随机数组 origin_list 赋值给一个验证数组 test_list，然后用 Python 内置的 sort() 函数对 test_list进行排序，最后将排序后的 test_list 与隔算法排序后的数组进行比较，如果完全相同，则验证成功，否则失败。

Python 内置函数 sort() 使用的是 Timsort 算法，由 Tim Peters 发明于2002年。该算法明显快于本程序中的其他算法，因此被用于验证。

这一思路也被用于单元测试中。

## 表格生成
本程序使用了第三方包 Tabulate 对数据进行表格化。
[Tabulate 文档](https://pypi.python.org/pypi/tabulate)

## FAQ
**1.为什么验证和单元测试以另一个算法的排序结果为基准、而非用其他方法？**

最简单的验证方法：

```
for i in range(len(array)-1):
	if array[i] <= array[i+1]:
		return True
	else:
		return False
```
该方法只能验证第i个元素是否小于第i+1个元素，一旦代码由于各种Bug将数组进行修改(元素被改变)，该方法是无法判断的。例如原数组为[5,4,3,2,1]，排序后为[6,7,8,9,10,11,12]。如果想检测这种情况，首先需要看输出的数组的每个元素是否都在待排数组中，同时看数组规模是否有变化。

即便这样测试，也无法避免某些情况。例如当待排数组为『2,3,3』、而输出为[2,2,3]时，以上方法都失灵。

因此最好也最简单粗暴的方法是用一个效率很高的、可以保证正确的算法对待排数组进行排序，以其结果为基准验证其他算法。

**2.为什么需要 sys.setrecursionlimit(999999)**

Python 默认递归深度为1000（可以用 sys.getrecursionlimit()查看），在某些算法进行递归时，可能会到达最大递归深度，因此可以先设置一个较大的数数值。





