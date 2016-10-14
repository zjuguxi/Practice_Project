import unittest
import sort

class TestSort(unittest.TestCase):

    def test_bubble(self):

        self.assertEqual(sort.bubble.sort(), sort.test_list)

    def test_selection(self):
        self.assertEqual(sort.selection.sort(), sort.test_list)

    def test_insertion(self):
        self.assertEqual(sort.insertion.sort(), sort.test_list)

    def test_shell(self):
        self.assertEqual(sort.shell.sort(), sort.test_list)

    # def test_merge(self):
    #     self.assertEqual(sort.merge.sort(), sort.test_list)

    def test_quick(self):
        self.assertEqual(sort.quick.sort(), sort.test_list)

    def test_heap(self):
        self.assertEqual(sort.heap.sort(), sort.test_list)

if __name__ == '__main__':
    unittest.main()