def reverse_arr(arr, left, right):
    if left < right:
        arr[left], arr[right] = arr[right], arr[left]
        reverse_arr(arr, left + 1, right - 1)
    return arr


# tests
import unittest

class ReverseArrayTests(unittest.TestCase):
    num_list = [1, 2, 3, 4, 5]
    empty_list = []

    def test_reverse_valid_array(self):
        self.assertEqual(
            reverse_arr(self.num_list, 0, len(self.num_list) - 1),
            [5, 4, 3, 2, 1]
        )

    def test_reverse_empty_list(self):
        self.assertEqual(
            reverse_arr(self.empty_list, 0, len(self.empty_list) - 1), [])


if __name__ == '__main__':
    unittest.main()
