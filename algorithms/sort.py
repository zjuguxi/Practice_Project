import timeit
import numpy.random as nprnd
import sys
from tabulate import tabulate

try: # 判断第二个参数是否是整数，如果不是抛出异常，如果是，则赋值给sort_number
    sort_number=int(sys.argv[2])
except ValueError:
    print('That\'s not an integer!')

sys.setrecursionlimit(999999) # 设置递归深度

list_start = timeit.default_timer()
origin_list = list(nprnd.randint(100000000, size=sort_number)) # 创建随机数组，规模是sort_number
list_end = timeit.default_timer()
list_time = round((list_end - list_start), 4)

print('==============')
print('Random array generated in %s s' % list_time)
print('Size of the array: ', len(origin_list))

test_list = origin_list[:]
test_list_start = timeit.default_timer()
test_list.sort()
test_list_end = timeit.default_timer()
test_list_time = round((test_list_end - test_list_start), 4)

if len(sys.argv) > 3:
    if sys.argv[3] == "reversed": # 如果含reversed参数，则传入的初识列表origin_list
        origin_list = list(reversed(test_list)) # 为逆序，此处为了方便，直接取排序后的
    elif sys.argv[3] == '':                            # test_list并将之逆序化
        pass
    else:
        raise NameError('reversed?')
else:
    pass

print('Python built-in sort() time: %s s' % test_list_time)
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

    def sort(self, x):
        pass

    def get_time(self):
        return self.time

class Bubble(Sort): ############## Bubble Sort
    def sort(self,bubble_list):
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
    def sort(self, selection_list):
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
    def sort(self, insertion_list):
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
    def sort(self, shell_list):
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

class Merge(Sort): ############## Merge  Sort
    def sort(self,merge_list):
        merge_start_time = timeit.default_timer() 
        if len(merge_list) == 1:
            return merge_list
        else:
            mid = int(len(merge_list)/2)
            left = self.sort(merge_list[:mid])
            right = self.sort(merge_list[mid:])

            i, j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merge_list[k] = left[i]
                    i += 1; k += 1
                else:
                    merge_list[k] = right[j]
                    j += 1; k += 1

            remaining = left if i < j else right
            r = i if remaining == left else j

            while r < len(remaining):
                merge_list[k] = remaining[r]
                r += 1; k += 1
            
            merge_end_time = timeit.default_timer()
            self.time = round((merge_end_time - merge_start_time), 4)
            return merge_list
merge = Merge()

class Quick(Sort): ############## Quick Sort
    
    def sort(self, quick_list):
        #global quick_list
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
    
    def sort(self, heap_list):
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


# 以下是生成表格的方法
table = []
headers = ['Algorithms', 'Time (s)', 'Verification']
sort_name = ['bubble','selection','insertion','shell','merge','quick','heap', 'all']

if sys.argv[1] == sort_name[0]:
    bubble.sort(bubble_list)
    if bubble_list == test_list:
        table.append(['Bubble Sort', bubble.get_time(), 'True'])
    else:
        table.append(['Bubble Sort', bubble.get_time(), 'False'])
elif sys.argv[1] == sort_name[1]:
    selection.sort(selection_list)
    if selection_list == test_list:
        table.append(['Selection Sort', selection.get_time(), 'True'])
    else:
        table.append(['Selection Sort', selection.get_time(), 'False'])
elif sys.argv[1] == sort_name[2]:
    insertion.sort(insertion_list)
    if insertion_list == test_list:
        table.append(['Insertion Sort', insertion.get_time(), 'True'])
    else:
        table.append(['Insertion Sort', insertion.get_time(), 'False'])
elif sys.argv[1] == sort_name[3]:
    shell.sort(shell_list)
    if shell_list == test_list:
        table.append(['Shell Sort', shell.get_time(), 'True'])
    else:
        table.append(['Shell Sort', shell.get_time(), 'False'])
elif sys.argv[1] == sort_name[4]:
    merge.sort(merge_list)
    if merge_list == test_list:
        table.append(['Merge Sort', merge.get_time(), 'True'])
    else:
        table.append(['MergeSort', merge.get_time(), 'False'])
elif sys.argv[1] == sort_name[5]:
    quick.sort(quick_list)
    if quick_list == test_list:
        table.append(['Quick Sort', quick.get_time(), 'True'])
    else:
        table.append(['Quick Sort', quick.get_time(), 'False'])
elif sys.argv[1] == sort_name[6]:
    heap.sort(heap_list)
    if selection_list == test_list:
        table.append(['Selection Sort', selection.get_time(), 'True'])
    else:
        table.append(['Selection Sort', selection.get_time(), 'False'])

elif sys.argv[1] == sort_name[7]:
    bubble.sort(bubble_list)
    if bubble_list == test_list:
        table.append(['Bubble Sort', bubble.get_time(), 'True'])
    else:
        table.append(['Bubble Sort', bubble.get_time(), 'False'])
    selection.sort(selection_list)
    if selection_list == test_list:
        table.append(['Selection Sort', selection.get_time(), 'True'])
    else:
        table.append(['Selection Sort', selection.get_time(), 'False'])
    insertion.sort(insertion_list)
    if insertion_list == test_list:
        table.append(['Insertion Sort', insertion.get_time(), 'True'])
    else:
        table.append(['Insertion Sort', insertion.get_time(), 'False'])
    shell.sort(shell_list)
    if shell_list == test_list:
        table.append(['Shell Sort', shell.get_time(), 'True'])
    else:
        table.append(['Shell Sort', shell.get_time(), 'False'])
    merge.sort(merge_list)
    if merge_list == test_list:
        table.append(['Merge Sort', merge.get_time(), 'True'])
    else:
        table.append(['MergeSort', merge.get_time(), 'False'])
    quick.sort(quick_list)
    if quick_list == test_list:
        table.append(['Quick Sort', quick.get_time(), 'True'])
    else:
        table.append(['Quick Sort', quick.get_time(), 'False'])
    heap.sort(heap_list)
    if selection_list == test_list:
        table.append(['Selection Sort', selection.get_time(), 'True'])
    else:
        table.append(['Selection Sort', selection.get_time(), 'False'])
else:
    raise NameError('It is not a sorting algotithms')
print(tabulate(table, headers,tablefmt='fancy_grid'))