import timeit
import numpy.random as nprnd
import sys

sys.setrecursionlimit(999999)

list_start = timeit.default_timer()
origin_list = list(nprnd.randint(100000000, size = 10000))

list_end = timeit.default_timer()
list_time = round((list_end - list_start),3)

test_list = origin_list
list_start = timeit.default_timer()
test_list.sort()
list_end = timeit.default_timer()
test_list_time = round((list_end - list_start),3)

print('List time : %s s' % list_time) 
print('Length of the list: ', len(origin_list))
print('==============')

bubble_list = origin_list

class Sort(object):
    def __init__(self, array):
        self.sort_list = sort_list

    def bubble_sort(self):
        n = len(bubble_list) 
        for i in range(n):
            for j in range(1,n-i):
                if  bubble_list[j-1] > bubble_list[j] :  
                    bubble_list[j-1], bubble_list[j] = bubble_list[j], bubble_list[j-1]
        return bubble_list
        print("Bubble Sort:  %s s " % (round(bubble_elapse_time, 3)))