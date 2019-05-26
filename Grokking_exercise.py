__author__ = 'yusuke'
"""
Grokking the Coding Interview: Patterns for Coding Questions
"""

import unittest
from SlidingWindowPattern import *
from TwoPointersPattern import *

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

    def test_pair_with_targetsum(self):
        self.assertEqual(pair_with_targetsum([1, 2, 3, 4, 6], 6), [1, 3])
        self.assertEqual(pair_with_targetsum([2, 5, 9, 11], 11), [0, 2])

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([2, 3, 3, 3, 6, 9, 9]), 4)
        self.assertEqual(remove_duplicates([2, 2, 2, 11]), 2)

    def test_remove_element(self):
        self.assertEqual(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3), 4)
        self.assertEqual(remove_element([2, 11, 2, 2, 1], 2), 2)

    def test_make_squares(self):
        self.assertEqual(make_squares([-2, -1, 0, 2, 3]), [0, 1, 4, 4, 9])
        self.assertEqual(make_squares([-3, -1, 0, 1, 2]), [0, 1, 1, 4, 9])

    def test_search_triplets(self):
        self.assertEqual(search_triplets([-3, 0, 1, 2, -1, 1, -2]), [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]])
        self.assertEqual(search_triplets([-5, 2, -1, -2, 3]), [[-5, 2, 3], [-2, -1, 3]])

    def test_triplet_sum_close_to_zero(self):
        self.assertEqual(triplet_sum_close_to_zero([-2, 0, 1, 2], 2), 1)
        self.assertEqual(triplet_sum_close_to_zero([-3, -1, 1, 2], 1), 0)
        self.assertEqual(triplet_sum_close_to_zero([1, 0, 1, 1], 100), 3)