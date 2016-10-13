import unittest
import sort

class TestSort(unittest.TestCase):

    def test_bubble(self):

        self.assertEqual(sort.bubble.sort(), sort.test_list)

if __name__ == '__main__':
    unittest.main()