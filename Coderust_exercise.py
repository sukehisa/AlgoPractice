__author__ = 'yusuke'

import unittest
from collections import deque
from typing import List

def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (right - left) // 2 + left
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def find_max_sliding_window(arr, window_size):
    if len(arr) == 0 or window_size > len(arr):
        return
    window = deque()
    result = []

    # 最初のwindowのmaxを検索する
    for i in range(0, window_size):
        while window and arr[i] >= arr[window[-1]]:
            window.pop()
        window.append(i)

    result.append(arr[window[0]])

    for i in range(window_size, len(arr)):
        # 対象の数値よりも
        while window and arr[i] >= arr[window[-1]]:
            window.pop()

        # windowの外側のindexは捨てる
        if window and (window[0] <= i-window_size):
            window.popleft()

        window.append(i)
        result.append(arr[window[0]])

    return result


def binary_search_rotated(arr, key):
    left = 0
    right = len(arr) - 1

    if left > right:
        return -1
    while left <= right:
        mid = left + (right-left) // 2

        if arr[mid] == key:
            return mid
        # 左半分がソートされている　かつ　keyが左半分にいる
        elif arr[left] <= arr[mid] and (arr[left] <= key <= arr[mid]):
            right = mid - 1
        # 右半分がソートされている かつ keyが右半分にいる
        elif arr[mid] <= arr[right] and (arr[mid] <= key <= arr[right]):
            left = mid + 1
        # 左半分がソートされていない
        elif arr[left] >= arr[mid]:
            right = mid - 1
        # 右半分がソートされていない
        elif arr[mid] >= arr[right]:
            left = mid + 1
    return -1


def find_least_common_number_binary_search(a: List, b: List, c: List) -> int:
    """
    n log(n) Runtime complexity: binary search is log(n) Runtime Complexity
    O(n) Memory complexity
    """
    for elem in a:
        if binary_search(b, elem) != -1 and binary_search(c, elem) != -1:
            return elem


def find_least_common_number(a: List, b: List, c: List) -> int:
    i, j, k = 0, 0, 0  # type: int

    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] == c[k]:
            return a[i]
        if a[i] <= b[j] and a[i] <= c[k]:
            i += 1
        elif b[j] <= a[i] and b[j] <= c[k]:
            j += 1
        else:
            k += 1

    return -1


def rotate_array(arr: List[int], n: int):
    """
    Computational Complexity: O(n)
    Memory Complexity:O(1)
    """
    n %= len(arr)
    return arr[-n:] + arr[:-n]


def rotate_array_(arr: List[int], n: int):
    result = [0] * len(arr)
    for i, elem in enumerate(arr):
        result[(i+(n % len(arr))+len(arr)) % len(arr)] = elem
    return result


def find_low_index_(arr: List[int], key: int) -> int:
    """
    my 1st try
    binary search を使用する. O(log n), O(1)
    入力のarrには重複数字ありのため、mid-1を検査するロジックがある
    :param arr: 重複数字あり。
    :param key:
    :return:
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if (mid == 0) and (arr[mid] == key):
            return mid
        elif (key == arr[mid]) and ((mid != 0) and (arr[mid-1] != arr[mid])):
            return mid
        elif arr[mid] >= key:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def find_low_index(arr: List[int], key: int) -> int:
    """
    Coderustより：
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] >= key:    # lowerな方向へ探索するので、等号が必要
            high = mid - 1
        else:
            low = mid + 1

    if arr[low] == key:        # lowがhighを追い越した瞬間の、low
        return low
    else:
        return -1


def find_high_index_(arr: List[int], key: int) -> int:
    """
    my 1st try
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if (mid == (len(arr)-1)) and (arr[mid] == key):
            return mid
        elif (key == arr[mid]) and ((mid != len(arr)-1) and (arr[mid+1] != arr[mid])):
            return mid
        elif arr[mid] <= key:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def find_high_index(arr: List[int], key: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] <= key:
            low = mid + 1
        else:
            high = mid - 1

    if arr[high] == key:
        return high
    else:
        return -1


def move_zeros_to_left_(A):
    """
    Computation: O(n)  propotional to input array
    Memory: O(n) : requires additional array
    """
    if len(A) <= 1:
        return A

    nzs = []
    zero_cnt = 0
    for e in A:
        if e == 0:
            zero_cnt += 1
        else:
            nzs.append(e)
    return [0] * zero_cnt + nzs


def move_zeros_to_left(arr):
    """
    Computation: O(n)  propotional to input array
    Memory: O(1) : only uses memory of input array
    """
    size = len(arr)
    if size <= 1:
        return arr

    read_index, write_index = size - 1, size - 1
    while write_index >= 0:
        if read_index < 0:
            arr[write_index] = 0
            write_index -= 1
        elif arr[read_index] != 0:
            arr[write_index] = arr[read_index]
            read_index -= 1
            write_index -= 1
        elif arr[read_index] == 0:
            read_index -= 1
    return arr


class CodeRustExTest(unittest.TestCase):
    # Arrays: Binary Search
    def test_binary_search(self):
        # test 1
        nums = [1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162, 176, 188, 199, 200, 210, 222]
        k = 47
        self.assertEqual(binary_search(nums, k), 3, "'47' is at 3rd index")

        nums = [2, 3, 4, 5, 6, 7, 9, 10]
        k = 0
        self.assertEqual(binary_search(nums, k), -1, "'0' is not in the array returning -1")

    def test_find_max_sliding_window(self):
        # test 1
        self.assertEqual(find_max_sliding_window([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4), [4, 5, 6, 7, 8, 9, 10])
        # test 2
        self.assertEqual(find_max_sliding_window([-4, 2, -5, 1, -1, 6], 3), [2, 2, 1, 6])

    def test_binary_search_rotated(self):
        # test 1
        arr = [176, 188, 199, 200, 210, 222, 1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162]
        key = 200
        self.assertEqual(binary_search_rotated(arr, key), 3)

    def test_find_least_common_number(self):
        # test1
        a = [6, 7, 10, 25, 30, 63, 64]
        b = [-1, 4, 5, 6, 7, 8, 50]
        c = [1, 6, 10, 14]
        self.assertEqual(find_least_common_number(a, b, c), 6)

    def test_rotate_array(self):
        # test1
        arr = [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]
        self.assertEqual(rotate_array(arr, -1), [10, 20, 0, 59, 86, 32, 11, 9, 40, 1])
        # test 2
        self.assertEqual(rotate_array(arr, 2), [9, 40, 1, 10, 20, 0, 59, 86, 32, 11])
        # test 3
        self.assertEqual(rotate_array(arr, 2+len(arr)), [9, 40, 1, 10, 20, 0, 59, 86, 32, 11])

    def test_find_low_and_high_index(self):
        # test 1
        arr = [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 20]
        self.assertEqual(find_low_index(arr, 1), 0)
        self.assertEqual(find_low_index(arr, 2), 1)
        self.assertEqual(find_low_index(arr, 5), 2)
        self.assertEqual(find_low_index(arr, 20), 10)
        self.assertEqual(find_high_index(arr, 1), 0)
        self.assertEqual(find_high_index(arr, 2), 1)
        self.assertEqual(find_high_index(arr, 5), 9)
        self.assertEqual(find_high_index(arr, 20), 10)

    def test_move_zeros_to_left(self):
        # test: empty
        arr = []
        self.assertEqual(move_zeros_to_left(arr), [])
        # test: 1 elem with zero
        arr = [0]
        self.assertEqual(move_zeros_to_left(arr), [0])
        # test: 1 elem with non-zero
        arr = [10]
        self.assertEqual(move_zeros_to_left(arr), [10])
        # test: N elem
        arr = [10, 20, 30]
        self.assertEqual(move_zeros_to_left(arr), [10, 20, 30])
        # test: N elem
        arr = [10, 0, 30]
        self.assertEqual(move_zeros_to_left(arr), [0, 10, 30])
        # test: N elem
        arr = [10, 0, 0]
        self.assertEqual(move_zeros_to_left(arr), [0, 0, 10])
        # test: N elem
        arr = [0, 0, 0]
        self.assertEqual(move_zeros_to_left(arr), [0, 0, 0])
