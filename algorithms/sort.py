import timeit
import numpy.random as nprnd
import sys
import collections
from collections import deque # for merge sort

sys.setrecursionlimit(999999) # 设置递归深度
list_start = timeit.default_timer()
origin_list = list(nprnd.randint(1000000, size=2000)) # 创建随机数组
list_end = timeit.default_timer()
list_time = round((list_end - list_start), 4)
print('==============')
print('List time : %s s' % list_time)
print('Length of the list: ', len(origin_list))
test_list = origin_list[:]
test_list_start = timeit.default_timer()
test_list.sort()
test_list_end = timeit.default_timer()
test_list_time = round((test_list_end - test_list_start), 4)

print('Python sort time: %s s' % test_list_time)
print('==============')

bubble_list = origin_list[:]
selection_list = origin_list[:]
insertion_list = origin_list[:]
shell_list = origin_list[:]
merge_list = origin_list[:]
quick_list = origin_list[:]
heap_list = origin_list[:]

class Sort(object): ############## Base Class
    def __init__(self):
        self.time = 0

    def sort(self):
        pass

    def get_time(self):
        return self.time

class Bubble(Sort): ############## Bubble Sort
    def sort(self):
        n = len(bubble_list)
        bubble_start_time = timeit.default_timer()
        for i in range(n):
            for j in range(1, n - i):
                if bubble_list[j - 1] > bubble_list[j]:
                    bubble_list[j - 1], bubble_list[j] = bubble_list[j], bubble_list[j - 1]        
        bubble_end_time = timeit.default_timer()
        self.time = round((bubble_end_time - bubble_start_time), 4)
        return bubble_list
        print('Bubble Sort Time: {}s'.format(self.time))
bubble = Bubble()



class Selection(Sort): ############## Selection Sort
    def sort(self):
        n = len(selection_list)
        selection_start_time = timeit.default_timer()
        for i in range(0,n):
            min = i
            for j in range(i+1,n):
                if selection_list[j] < selection_list[min] :
                    min = j
            selection_list[min],selection_list[i] = selection_list[i],selection_list[min]
        
        selection_end_time = timeit.default_timer()
        self.time = round((selection_end_time - selection_start_time), 4)
        return selection_list
selection = Selection()

class Insertion(Sort):  ############## Insertion Sort
    def sort(self):
        insertion_start_time = timeit.default_timer()
        n = len(insertion_list)
        for i in range(1,n):
            if insertion_list[i] < insertion_list[i-1]:
                temp = insertion_list[i]
                index = i
                for j in range(i-1,-1,-1):
                    if insertion_list[j] > temp :
                        insertion_list[j+1] = insertion_list[j]
                        index = j
                    else :
                        break
                insertion_list[index] = temp
        insertion_end_time = timeit.default_timer()
        self.time = round((insertion_end_time - insertion_start_time), 4)
        return insertion_list
insertion = Insertion()

class Shell(Sort): ############## Shell Sort
    def sort(self):
        shell_start_time = timeit.default_timer()
        n = len(shell_list)
        gap = round(n/2) 
        while gap > 0 :
            for i in range(gap,n): 
                temp = shell_list[i]
                j = i
                while ( j >= gap and shell_list[j-gap] > temp ): 
                    shell_list[j] = shell_list[j-gap]
                    j = j - gap
                shell_list[j] = temp
            gap = round(gap/2) 
        shell_end_time = timeit.default_timer()
        self.time = round((shell_end_time - shell_start_time), 4)
        return shell_list
shell = Shell()

'''
class Merge(Sort): ############## Merge Sort
    def sort(self):
        if len(merge_list) <= 1 : return merge_list
        num = int(len(merge_list)/2)
        left = Merge.sort(merge_list[:num])
        right = Merge.sort(merge_list[num:])
        return merge(left,right)

    def merge(left,right):
        l,r = 0,0
        result = []
        while l<len(left) and r<len(right) :
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        result += left[l:]
        result += right[r:]
        return result
merge = Merge()
'''
class Quick(Sort): ############## Quick Sort
    
    def sort(self):
        global quick_list
        quick_start_time = timeit.default_timer()
        quick_list = Quick.qsort(quick_list,0,len(quick_list)-1)
        quick_end_time = timeit.default_timer()
        self.time = round((quick_end_time - quick_start_time), 4)
        return quick_list
        
    def qsort(quick_list,left,right):
        if left >= right : return quick_list
        key = quick_list[left]
        lp = left
        rp = right
        while lp < rp :
            while quick_list[rp] >= key and lp < rp :
                rp -= 1
            while quick_list[lp] <= key and lp < rp :
                lp += 1
            quick_list[lp],quick_list[rp] = quick_list[rp],quick_list[lp]
        quick_list[left],quick_list[lp] = quick_list[lp],quick_list[left]
        Quick.qsort(quick_list,left,lp-1)
        Quick.qsort(quick_list,rp+1,right)
        return quick_list  
quick = Quick()

class Heap(Sort): ############## Heap Sort
    
    def sort(self):
        heap_start_time = timeit.default_timer()
        n = len(heap_list)
        first = int(n/2-1) 
        for start in range(first,-1,-1) : 
            Heap.max_heapify(heap_list,start,n-1)
        for end in range(n-1,0,-1): 
            heap_list[end],heap_list[0] = heap_list[0],heap_list[end]
            Heap.max_heapify(heap_list,0,end-1)
        heap_end_time = timeit.default_timer()
        self.time = round((heap_end_time - heap_start_time), 4)
        return heap_list

    def max_heapify(heap_list,start,end):
        root = start
        while True :
            child = root*2 +1
            if child > end : break
            if child+1 <= end and heap_list[child] < heap_list[child+1] :
                child = child+1 
            if heap_list[root] < heap_list[child] :   
                heap_list[root],heap_list[child] = heap_list[child],heap_list[root]
                root = child
            else :
                break
heap = Heap()
'''
bubble.sort()
selection.sort()
insertion.sort()
shell.sort()
#merge.sort()
quick.sort()
heap.sort()

print(bubble.get_time())
print(selection.get_time())
print(insertion.get_time())
print(shell.get_time())
#print(merge.get_time())
print(quick.get_time())
print(heap.get_time())
'''