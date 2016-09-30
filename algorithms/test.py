import time
import random

origin_list = []

for i in range(100000):
    n = random.randint(1, 9999999999)
    origin_list.append(n)

print('Length of the list: ', len(origin_list))

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