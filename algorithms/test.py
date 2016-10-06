import numpy.random as nprnd
import timeit

list_start = timeit.default_timer()
origin_list = list(nprnd.randint(100000000, size = 10000))
nprnd.shuffle(origin_list)

list_end = timeit.default_timer()
list_time = round((list_end - list_start),3)
print('List time : %s' % list_time) 
print('Length of the list: ', len(origin_list))
print('==============')

list = origin_list

n = len(list)
for i in (0,n):
    list[i] = min(list)
    for j in 