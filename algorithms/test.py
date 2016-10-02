import timeit
import random

origin_list = []

for i in range(1000):
    n = random.randint(1, 9999999999)
    origin_list.append(n)

print('Length of the list: ', len(origin_list))

bubble_list = origin_list

def bubble_sort(bubble_list):
    n = len(bubble_list)                   #获得数组的长度
    for i in range(n):
        for j in range(1,n-i):
            if  bubble_list[j-1] > bubble_list[j] :       #如果前者比后者大
                bubble_list[j-1], bubble_list[j] = bubble_list[j], bubble_list[j-1]       #则交换两者
    return bubble_list

start = timeit.default_timer()
bubble_sort(bubble_list)
end = timeit.default_timer()

bubble_elapse_time = end - start
print("Bubble Sort:  %s second " % (round(bubble_elapse_time, 3)))