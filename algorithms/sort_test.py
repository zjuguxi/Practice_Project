import sys
import unittest
from sort import Bubble_sort
import numpy.random as nprnd

# sys.setrecursionlimit(999999)
# origin_list = list(nprnd.randint(1000000, size=200))
# print('Length of the list: ', len(origin_list))

# test_list = origin_list # 用Python内置函数sort()对test_list排序
# test_list.sort()

# bubble_list = origin_list # 用冒泡算法对bubble_list排序
# Bubble_sort.sort()

class TestSort(unittest.TestCase):

    def setUp(self):
        self.origin_list = list(nprnd.randint(1000000, size=200))
        bubble_list = self.origin_list
        test_list = self.origin_list.sort()

    def test_bubble_sort(self):
        self.assertEqual(Bubble_sort.sort(self.origin_list), self.origin_list.sort())

if __name__ == '__main__':
    unittest.main()