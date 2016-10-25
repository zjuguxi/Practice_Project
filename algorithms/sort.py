# coding=utf-8
import timeit
import sys
import threading

sys.setrecursionlimit(999999) # 设置递归深度

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

class MergeMT(Sort): ############## Merge Sort - MultiThreading

    def sort(self, mergemt_list):
        mergemt_start_time = timeit.default_timer()
        if len(mergemt_list) != 1:
            thread_main = threading.Thread(target=MergeMT.mergemt_sort, args = (0, len(mergemt_list)-1, mergemt_list))
            # 等待线程结束
            thread_main.start()
            thread_main.join()
        merge_end_time = timeit.default_timer()
        self.time = round((merge_end_time - mergemt_start_time), 4)
        return mergemt_list

    @staticmethod
    def mergemt_sort(l, r, arr_list):
        index_l = l
        index_r = r
        mergemt_list = arr_list

        if index_l < index_r:

            middle = (index_l+(index_r-1))// 2

            thread1 = threading.Thread(target=MergeMT.mergemt_sort, args = (index_l, middle,mergemt_list))
            thread2 = threading.Thread(target=MergeMT.mergemt_sort, args = (middle+1,index_r,mergemt_list))

            # 等待结束后归并
            thread1.start()
            thread2.start()
            thread1.join()
            thread2.join()
            MergeMT.mergemt(mergemt_list,index_l, middle, index_r)

    @staticmethod
    def mergemt(mergemt_list, index_l, middle, index_r):

        half1 = middle - index_l + 1
        half2 = index_r - middle
        first = mergemt_list[index_l:index_l+half1]
        second = mergemt_list[middle+1:middle+half2+1]

        k = index_l

        # 将数组按照大小顺序从新放入arr数组中
        i = 0
        j = 0
        while i < half1 and j < half2:

            if first[i] <= second[j]:
                mergemt_list[k] = first[i]
                i += 1
            else:
                mergemt_list[k] = second[j]
                j += 1

            k += 1

        # 将剩余的数据放入数组尾部
        while j < half2:
            mergemt_list[k] = second[j]
            j += 1
            k += 1

        while i < half1:
            mergemt_list[k] = first[i]
            i += 1
            k += 1


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