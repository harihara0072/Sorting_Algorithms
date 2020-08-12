import unittest
from src.insertion_sort import insertion_sort


class Test(unittest.TestCase):

    def test_unsorted_array(self):
        actual = insertion_sort([1, 5, 3, 2])
        expected = [1, 2, 3, 5]
        self.assertEqual(actual, expected)

    def test_empty_array(self):
        actual = insertion_sort([])
        expected = []
        self.assertEqual(actual, expected)

    def test_all_same_digits(self):
        actual = insertion_sort([1, 1, 1, 1])
        expected = [1, 1, 1, 1]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
