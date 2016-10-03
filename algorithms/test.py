import timeit
import random
import sys
#sys.setrecursionlimit(99999)
origin_list = []
list_start = timeit.default_timer()
for i in range(10000000):
    n = random.randint(1, 9999999999)
    origin_list.append(n)
list_end = timeit.default_timer()
list_time = list_end - list_start
print('List time : %s' % list_time) 
print('Length of the list: ', len(origin_list))

quick_sort_list = origin_list
def quick_sort(quick_sort_list):
    if len(quick_sort_list) <= 1: return quick_sort_list
    return quick_sort([x for x in quick_sort_list if x < quick_sort_list[0]]) + [x for x in quick_sort_list if x == quick_sort_list[0]] + quick_sort([x for x in quick_sort_list if x > quick_sort_list[0]])


start = timeit.default_timer()
quick_sort(quick_sort_list)
end = timeit.default_timer()

quick_sort_elapse_time = end - start
print("Quick Sort:  %s second " % (round(quick_sort_elapse_time, 3)))