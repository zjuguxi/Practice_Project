import unittest
from sorting import Sort
import numpy.random as nprnd

sys.setrecursionlimit(999999)

origin_list = list(nprnd.randint(100000000, size = 10000))
test_list = origin_list

class TestSort(unittest.TestCase):

    def merge_sort(self):
        self.assertEqual(merge_list, test_list)

    def heap_sort(self):
        self.assertEqual(heap_list, test_list)

    def bubble_sort(self):
        self.assertEqual(bubble_list, test_list)

    def insert_sort(self):
        self.assertEqual(insert_list, test_list)

    def quick_sort(self):
        self.assertEqual(quick_list, test_list)

    def select_sort(self):
        self.assertEqual(select_list, test_list)

    def shell_sort(self):
        self.assertEqual(shell_list, test_list)


if __name__ == '__main__':
    unittest.main()