import timeit
import numpy.random as nprnd
import sys

sys.setrecursionlimit(999999)
list_start = timeit.default_timer()
origin_list = list(nprnd.randint(1000000, size=2000))
list_end = timeit.default_timer()
list_time = round((list_end - list_start), 4)
print('List time : %s s' % list_time)
print('Length of the list: ', len(origin_list))
print('==============')
test_list = origin_list
test_list_start = timeit.default_timer()
test_list.sort()
test_list_end = timeit.default_timer()
test_list_time = round((test_list_end - test_list_start), 4)

print('Python sort time: %s s' % test_list_time)
print('==============')

bubble_list = origin_list
selection_list = origin_list

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
    def __init__(self):
        self.time = 0
    def sort(self):
        global selection_elapse_time
        n = len(selection_list)
        selection_start_time = timeit.default_timer()
        for i in range(0,n):
            min = i
            for j in range(i+1,n):
                if selection_list[j] < selection_list[min] :
                    min = j
            selection_list[min],selection_list[i] = selection_list[i],selection_list[min]
        
        selection_end_time = timeit.default_timer()
        selection_elapse_time = round((selection_end_time - selection_start_time), 4)
        return selection_list

    @classmethod
    def get_time(cls):
        return selection_elapse_time