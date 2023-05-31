def search_num(arr, num, left, right):
    if left > right or not arr:
        return -1
    else:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid
        else:
            if num > arr[mid]:
                return search_num(arr, num, mid + 1, right)
            else:
                return search_num(arr, num, left, mid - 1)


# tests
import unittest

class BinarySearchTests(unittest.TestCase):
    num_list = [5, 6, 7, 12, 12, 12, 13, 15, 16, 17, 17, 21, 33, 37, 39, 40, \
            43, 45, 45, 45, 45, 55, 56, 58, 59, 62, 63, 65, 75, 77, 77, 88, \
            89, 91, 92, 92, 94, 96, 98, 99]

    empty_list = []

    def test_search_for_valid_number(self):
        self.assertEqual(
            search_num(self.num_list, 56, 0, len(self.num_list)),
            self.num_list.index(56))
    
    def test_search_for_invalid_number(self):
        self.assertEqual(
            search_num(self.num_list, 2, 0, len(self.num_list)), -1)

    def test_search_for_empty_list(self):
        self.assertEqual(
            search_num(self.empty_list, 2, 0, len(self.num_list)), -1)


if __name__ == '__main__':
    unittest.main()
