# coding=utf-8
import timeit
import numpy.random as nprnd
from sort import *
import sys
from tabulate import tabulate

headers = ['Algorithms', 'Time (s)', 'Verification']

class_name = {
    'bubble': ['Bubble'],
    'selection': ['Selection'],
    'insertion': ['Insertion'],
    'shell': ['Shell'],
    'merge': ['Merge'],
    'mergemt': ['MergeMT'],
    'quick': ['Quick'],
    'heap': ['Heap'],
    'all': ['Bubble','Selection','Insertion','Shell','Merge','MergeMT','Quick','Heap'],
}

test_list = None
g_sort_list = {} #定义一个词典，把所有排序结果按照{bubble: bubble.sort(bubble_list)}的键值关系放进去，以供提取

def main():

    try: # 判断第二个参数是否是整数，如果不是抛出异常，如果是，则赋值给sort_number
        sort_number=int(sys.argv[2])
    except ValueError:
        print('That\'s not an integer!')

    list_start = timeit.default_timer()
    origin_list = list(nprnd.randint(100000000, size=sort_number)) # 创建随机数组，规模是sort_number
    list_end = timeit.default_timer()
    list_time = round((list_end - list_start), 4)

    print('==============')
    print('Random array generated in %s s' % list_time)
    print('Size of the array: ', len(origin_list))

    if len(sys.argv) > 3:
        if sys.argv[3] == "reversed": # 如果含reversed参数，则将origin_list逆序化
            origin_list.sort()
            origin_list = list(reversed(origin_list)) # 
        elif sys.argv[3] == '':                            # t
            pass
        else:
            raise NameError('reversed?')
    else:
        pass

    global test_list
    test_list = origin_list[:]
    test_list_start = timeit.default_timer()
    test_list.sort()
    test_list_end = timeit.default_timer()
    test_list_time = round((test_list_end - test_list_start), 4)

    print('Python built-in sort() time: %s s' % test_list_time)
    print('==============')

    # 按参数生成实例
    global g_sort_list
    if len(sys.argv) > 1 and sys.argv[1] in class_name.keys(): # 把sys.argv[1]当做class_name的key，提取对应的value
        table_list = []
        name_list = class_name[sys.argv[1]] # 把命令参数中包含的class_name的value保存到name_list，bubble转成Bubble
        for name in name_list:
            sort_list = origin_list[:]
            obj = eval(name+ '()') # 把用户输入的命令变成表达式，创建实例
            #obj = eval('{}'.format(name) + '()') 
            obj.sort(sort_list) # 使用该实例的sort方法，对sort_list排序
            g_sort_list[name] = sort_list # 将此键值加入g_sort_list词典
            table_list.append(['%s Sort' % name , obj.get_time(),"True" if sort_list == test_list else "False"])
    else:
        raise NameError("arg sort name error")

    print(tabulate(table_list, headers,tablefmt='fancy_grid'))

main()