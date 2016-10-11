import sys
import unittest
from sort import Sort
import numpy.random as nprnd

sys.setrecursionlimit(999999)
origin_list = list(nprnd.randint(1000000, size=200))
print('Length of the list: ', len(origin_list))

test_list = origin_list
test_list.sort()

Bubble_sort.sort()

class TestSort(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual(Bubble_sort.sort(), test_list)

if __name__ == '__main__':
    unittest.main()