import sys
import unittest
from sort import Bubble_sort
import numpy.random as nprnd

# sys.setrecursionlimit(999999)
origin_list = list(nprnd.randint(1000000, size=200))
# print('Length of the list: ', len(origin_list))

# test_list = origin_list # 用Python内置函数sort()对test_list排序
# test_list.sort()

bubble_list = origin_list # 用冒泡算法对bubble_list排序
# Bubble_sort.sort()

class TestSort(unittest.TestCase):

    @staticmethod
    def test_bubble_sort(bubble_list):
        #bubble_list = origin_list
        test_list = origin_list.sort()
        assert Bubble_sort.sort(bubble_list) == origin_list

test = TestSort()
test.test_bubble_sort(origin_list)

if __name__ == '__main__':
    unittest.main()