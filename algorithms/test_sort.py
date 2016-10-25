import unittest
import sys
import random

n = random.randint(3*10**2,3*10**3)
sys.argv = ['test_sort.py', 'all', n, 'reversed'] # 随便写了一个命令行变量传进程序中，以供测试
import table


class TestSort(unittest.TestCase):

    def test_bubble(self):

        self.assertEqual(table.g_sort_list['Bubble'], table.test_list)

    def test_selection(self):
        self.assertEqual(table.g_sort_list['Selection'], table.test_list)

    def test_insertion(self):
        self.assertEqual(table.g_sort_list['Insertion'], table.test_list)

    def test_shell(self):
        self.assertEqual(table.g_sort_list['Shell'], table.test_list)

    def test_merge(self):
        self.assertEqual(table.g_sort_list['Merge'], table.test_list)

    def test_mergemt(self):
        self.assertEqual(table.g_sort_list['MergeMT'], table.test_list)

    def test_quick(self):
        self.assertEqual(table.g_sort_list['Quick'], table.test_list)

    def test_heap(self):
        self.assertEqual(table.g_sort_list['Heap'], table.test_list)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(('test_default_size'))
    suite.addTest(WidgetTestCase('test_resize'))
    return suite

if __name__ == '__main__':
    unittest.main()