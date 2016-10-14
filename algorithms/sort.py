import timeit
import numpy.random as nprnd
import sys
from collections import deque # for merge sort

sys.setrecursionlimit(999999) # 设置递归深度
list_start = timeit.default_timer()
origin_list = list(nprnd.randint(1000000, size=2000)) # 创建随机数组
list_end = timeit.default_timer()
list_time = round((list_end - list_start), 4)
print('List time : %s s' % list_time)
print('Length of the list: ', len(origin_list))
print('==============')
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


class Merge(Sort):
    def sort(self):
        if len(merge_list) <= 1 : return merge_list
        num = int(len(merge_list)/2)
        left = sort(merge_list[:num])
        right = sort(merge_list[num:])
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


