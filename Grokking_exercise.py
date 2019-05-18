__author__ = 'yusuke'
"""
Grokking the Coding Interview: Patterns for Coding Questions
"""

import unittest
from SlidingWindowPattern import *


class GrokkingExTest(unittest.TestCase):
    def test_max_sub_array_of_size_k(self):
        # test: empty arr
        arr = []
        self.assertEqual(max_sub_array_of_size_k(3, arr), -1)
        # test: arr size is less than k
        arr = [2, 1, 5, 1, 3, 2]
        self.assertEqual(max_sub_array_of_size_k(10, arr), -1)
        # test:
        arr = [2, 1, 5, 1, 3, 2]
        self.assertEqual(max_sub_array_of_size_k(3, arr), 9)
        # test:
        arr = [2, 3, 4, 1, 5]
        self.assertEqual(max_sub_array_of_size_k(2, arr), 7)
        # test:
        arr = [2, 3, 4, 1, 5]
        self.assertEqual(max_sub_array_of_size_k(1, arr), 5)

    def test_smallest_subarray_with_given_sum(self):
        self.assertEqual(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]), 2)
        self.assertEqual(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]), 1)
        self.assertEqual(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]), 3)
        self.assertEqual(smallest_subarray_with_given_sum(8, [2, 2, 1, 1, 2]), 5)

    def test_longest_substring_with_k_distinct(self):
        self.assertEqual(longest_substring_with_k_distinct("araaci", 2), 4)
        self.assertEqual(longest_substring_with_k_distinct("araaci", 1), 2)
        self.assertEqual(longest_substring_with_k_distinct("cbbebi", 3), 5)

    def test_fruits_into_baskets(self):
        self.assertEqual(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']), 3)
        self.assertEqual(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']), 5)

    def test_non_repeat_substring(self):
        input = ["aabccbb", "abbbb", "abccde"]
        ans = [3, 2, 3]

        for i, instr in enumerate(input):
            self.assertEqual(non_repeat_substring(instr), ans[i])

    def test_length_of_longest_substring(self):
        mut = length_of_longest_substring
        input_a = ["aabccbb", "abbcb", "abccde"]
        input_b = [2, 1, 1]
        ans = [5, 4, 3]

        for i in range(len(ans)):
            self.assertEqual(mut(input_a[i], input_b[i]), ans[i])