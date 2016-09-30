import time
import random

origin_list = []

for i in range(100000):
    n = random.randint(1, 9999999999)
    origin_list.append(n)

print('Length of the list: ', len(origin_list))

############## 归并排序
from collections import deque
merge_list = origin_list

start_time = time.time() 

def merge_sort(merge_list):
    if len(merge_list) <= 1:
        return merge_list

    def merge(left, right):
        merged,left,right = deque(),deque(left),deque(right)
        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft())  # deque popleft is also O(1)
        merged.extend(right if right else left)
        return list(merged)

    middle = int(len(merge_list) // 2)
    left = merge_sort(merge_list[:middle])
    right = merge_sort(merge_list[middle:])
    return merge(left, right)

merge_sort(merge_list)
elapse_time = time.time() - start_time
print("Merge Sort:  %s second " % (round(elapse_time, 3)))

############## 堆排序
heap_list = origin_list
heap_start_time = time.time()

def heap_sort(heap_list) :
    n = len(heap_list)
    first = int(n/2-1)       #最后一个非叶子节点
    for start in range(first,-1,-1) :     #构造大根堆
        max_heapify(heap_list,start,n-1)
    for end in range(n-1,0,-1):           #堆排，将大根堆转换成有序数组
        heap_list[end],heap_list[0] = heap_list[0],heap_list[end]
        max_heapify(heap_list,0,end-1)
    return heap_list

def max_heapify(heap_list,start,end):
    root = start
    while True :
        child = root*2 +1               #调整节点的子节点
        if child > end : break
        if child+1 <= end and heap_list[child] < heap_list[child+1] :
            child = child+1             #取较大的子节点
        if heap_list[root] < heap_list[child] :     #较大的子节点成为父节点
            heap_list[root],heap_list[child] = heap_list[child],heap_list[root]     #交换
            root = child
        else :
            break

heap_sort(heap_list)
heap_elapse_time = time.time() - heap_start_time
print("Heap Sort:  %s second " % (round(heap_elapse_time, 3)))

############## 冒泡排序

bubble_list = origin_list
bubble_start_time = time.time()

def bubble_sort(bubble_list):
    n = len(bubble_list)                   #获得数组的长度
    for i in range(n):
        for j in range(1,n-i):
            if  bubble_list[j-1] > bubble_list[j] :       #如果前者比后者大
                bubble_list[j-1], bubble_list[j] = bubble_list[j], bubble_list[j-1]       #则交换两者
    return bubble_list

bubble_sort(bubble_list)
bubble_elapse_time = time.time() - bubble_start_time
print("Bubble Sort:  %s second " % (round(bubble_elapse_time, 3)))