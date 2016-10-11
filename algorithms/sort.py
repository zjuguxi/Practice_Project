import timeit
import numpy.random as nprnd
import sys

sys.setrecursionlimit(999999)

list_start = timeit.default_timer()
origin_list = list(nprnd.randint(1000000, size=200))
list_end = timeit.default_timer()
list_time = round((list_end - list_start), 4)
print('List time : %s s' % list_time)
print('Length of the list: ', len(origin_list))

test_list = origin_list
test_list_start = timeit.default_timer()
test_list.sort()
test_list_end = timeit.default_timer()
test_list_time = round((list_end - list_start), 4)
print('Python sort time: %s s' % test_list_time)
print('==============')

bubble_list = origin_list
selection_list = origin_list

bubble_elapse_time = 0
selection_elapse_time = 0
class Sort(object):
    def __init__(self):
        pass

    def sort(cls):
        pass

    def get_time(self):
        pass


class Bubble_sort(Sort): ############## Bubble Sort
    @classmethod
    def sort(cls):
        global bubble_elapse_time
        n = len(bubble_list)
        bubble_start_time = timeit.default_timer()

        for i in range(n):
            for j in range(1, n - i):
                if bubble_list[j - 1] > bubble_list[j]:
                    bubble_list[j - 1], bubble_list[j] = bubble_list[j], bubble_list[j - 1]
        # return bubble_list

        bubble_end_time = timeit.default_timer()
        bubble_elapse_time = round((bubble_end_time - bubble_start_time), 3)
        return bubble_elapse_time
        print('Bubble Sort Time: {}s'.format(bubble_elapse_time))

    @classmethod
    def get_time(cls):
        return bubble_elapse_time


class Selection_sort(Sort): ############## Selection Sort
    @classmethod
    def sort(cls):
        global selection_elapse_time
        n = len(selection_list)
        selection_start_time = timeit.default_timer()
        for i in range(0,n):
            min = i
            for j in range(i+1,n):
                if selection_list[j] < selection_list[min] :
                    min = j
            selection_list[min],selection_list[i] = selection_list[i],selection_list[min]
        #return selection_list
        selection_end_time = timeit.default_timer()
        selection_elapse_time = round((selection_end_time - selection_start_time), 3)
        return selection_elapse_time

    @classmethod
    def get_time(cls):
        return selection_elapse_time