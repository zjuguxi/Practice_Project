import time
import random

origin_list = []

for i in range(50000):
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

## bubble_sort(bubble_list)
bubble_elapse_time = time.time() - bubble_start_time
# print("Bubble Sort:  %s second " % (round(bubble_elapse_time, 3)))
print('Bubble Sort: Too slow.............Skip it!')

############## 插入排序

insert_list = origin_list
insert_start_time = time.time()

def insert_sort(insert_list):
    n = len(insert_list)
    for i in range(1,n):
        if insert_list[i] < insert_list[i-1]:
            temp = insert_list[i]
            index = i           #待插入的下标
            for j in range(i-1,-1,-1):  #从i-1 循环到 0 (包括0)
                if insert_list[j] > temp :
                    insert_list[j+1] = insert_list[j]
                    index = j   #记录待插入下标
                else :
                    break
            insert_list[index] = temp
    return insert_list
insert_sort(insert_list)
insert_elapse_time = time.time() - insert_start_time
print("Insert Sort:  %s second " % (round(insert_elapse_time, 3)))

############## 快速排序
'''
quick_list = origin_list
quick_start_time = time.time()

def quick_sort(quick_list):
    return qsort(quick_list,0,len(quick_list)-1)

def qsort(quick_list,left,right):
    #快排函数，quick_list为待排序数组，left为待排序的左边界，right为右边界
    if left >= right : return quick_list
    key = quick_list[left]     #取最左边的为基准数
    lp = left           #左指针
    rp = right          #右指针
    while lp < rp :
        while quick_list[rp] >= key and lp < rp :
            rp -= 1
        while quick_list[lp] <= key and lp < rp :
            lp += 1
        quick_list[lp],quick_list[rp] = quick_list[rp],quick_list[lp]
    quick_list[left],quick_list[lp] = quick_list[lp],quick_list[left]
    qsort(quick_list,left,lp-1)
    qsort(quick_list,rp+1,right)
    return quick_list

quick_sort(quick_list)
quick_elapse_time = time.time() - quick_start_time
print("Quick Sort:  %s second " % (round(quick_elapse_time, 3)))
'''
############## 选择排序
select_list = origin_list
select_start_time = time.time()

def select_sort(select_list):
    n = len(select_list)
    for i in range(0,n):
        min = i                             #最小元素下标标记
        for j in range(i+1,n):
            if select_list[j] < select_list[min] :
                min = j                     #找到最小值的下标
        select_list[min],select_list[i] = select_list[i],select_list[min]   #交换两者
    return select_list

# select_sort(select_list)
select_elapse_time = time.time() - select_start_time
# print("Selection Sort:  %s second " % (round(select_elapse_time, 3)))
print('Selection Sort: Too slow.............Skip it!')

############## 希尔排序

shell_list = origin_list
shell_start_time = time.time()

def shell_sort(shell_list):
    n = len(shell_list)
    gap = round(n/2)       #初始步长 , 用round四舍五入取整
    while gap > 0 :
        for i in range(gap,n):        #每一列进行插入排序 , 从gap 到 n-1
            temp = shell_list[i]
            j = i
            while ( j >= gap and shell_list[j-gap] > temp ):    #插入排序
                shell_list[j] = shell_list[j-gap]
                j = j - gap
            shell_list[j] = temp
        gap = round(gap/2)                     #重新设置步长
    return shell_list

shell_sort(shell_list)
shell_elapse_time = time.time() - shell_start_time
print("Shell Sort:  %s second " % (round(shell_elapse_time, 3)))

############## 堆排序

heap_list = origin_list
heap_start_time = time.time()

def heap_sort(heap_list):
    n = len(heap_list)
    first = int(n/2-1)       #最后一个非叶子节点
    for start in range(first,-1,-1) :     #构造大根堆
        max_heapify(heap_list,start,n-1)
    for end in range(n-1,0,-1):           #堆排，将大根堆转换成有序数组
        heap_list[end],heap_list[0] = heap_list[0],heap_list[end]
        max_heapify(heap_list,0,end-1)
    return heap_list


#最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
#start为当前需要调整最大堆的位置，end为调整边界
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