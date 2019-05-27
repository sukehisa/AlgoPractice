__author__ = 'yusuke'

import math
from typing import List

def pair_with_targetsum(arr, target_sum):
    """
    Pair with Target Sum (easy)
    Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
    Time: O(N)
    Space: O(1)
    """
    left, right = 0, len(arr)-1

    while left < right:
        cur_sum = arr[left] + arr[right]
        if cur_sum == target_sum:
            return [left, right]
        elif cur_sum < target_sum:
            left += 1
        else:
            right -= 1

    return [-1, -1]


def remove_duplicates(arr):
    """
    Remove Duplicates (easy)
    Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space;
    after removing the duplicates in-place return the new length of the array.
    Time: O(N)
    Space: O(1), this is in-place algorithm
    :param arr:
    :return:
    """
    nextnondup = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[nextnondup-1]:
            arr[nextnondup] = arr[i]
            nextnondup += 1
    return nextnondup

def remove_element(arr, key):
    """
    Remove Duplicates (easy)
    Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place
    and return the new length of the array.
    :param arr:
    :param key:
    :return:
    """
    next = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[next] = arr[i]
            next += 1
    return next


def make_squares(arr):
    """
    Squaring a Sorted Array (easy)
    Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.
    Input: [-2, -1, 0, 2, 3]
    Output: [0, 1, 4, 4, 9]

    Educative.ioの回答よりこっちのほうが良さそう
    Computation: O(N), as we are iterating the input array only once
    Space: O(N), size of array as an output

    :param arr:
    :return:
    """
    ans = []
    left, right = 0, len(arr) - 1
    while left <= right:
        if abs(arr[right]) > abs(arr[left]):
            ans.insert(0, pow(arr[right], 2))
            right -= 1
        else:
            ans.insert(0, pow(arr[left], 2))
            left += 1
    return ans


def search_triplets(arr: List):
    """
    Triplet Sum to Zero (medium)
    Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
    Example 1:
    Input: [-3, 0, 1, 2, -1, 1, -2]
    Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
    Explanation: There are four unique triplets whose sum is equal to zero.

    Computation: O(N^2),  sortでO(N log N), 外側のループでO(N), 内側（search_pair)でO(N）⇛ O(N log N) + O(N^2)
    Space: O(N): sortでこのメモリ量
    """

    def search_pair(arr, target_sum, left, triplets):
        right = len(arr) - 1
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target_sum:
                triplets.append([-target_sum, arr[left], arr[right]])
                left += 1
                right -= 1
                # 重複は排除するため、前の要素と同じ場合はskipする
                while left < right and (arr[left-1] == arr[left]):
                    left += 1
                # 重複は排除するため、前の要素と同じ場合はskipする
                while left < right and (arr[right+1] == arr[right]):
                    right -= 1
            elif target_sum > current_sum:
                left += 1
            else:
                right -= 1

    arr.sort()
    triplets = []
    for i in range(len(arr)):
        # 重複は排除するため、前の軸要素と同じ場合はskipする
        if i > 0 and arr[i-1] == arr[i]:
            continue
        search_pair(arr, -arr[i], i + 1, triplets)
    return triplets


def triplet_sum_close_to_zero_(arr, target_sum) -> int:
    """
    Triplet Sum Close to Target (medium)
    Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to
    the target number as possible.
    Input: [-2, 0, 1, 2], target=2
    Output: 1
    Explanation: The triplet [-2, 1, 2] has the closest sum to the target
    """
    arr.sort()
    closest_sum = -99999
    for i in range(len(arr)):
        if i > 0 and arr[i-1] == arr[i]:
            continue
        closest_pair_sum = get_closest_pair(arr, target_sum - arr[i], i+1)
        if abs(target_sum - closest_sum) > abs(target_sum - (closest_pair_sum + arr[i])):
            closest_sum = closest_pair_sum + arr[i]
    return closest_sum


def get_closest_pair(arr, target_sum, left) -> int:
    right = len(arr) - 1
    closest_sum = -99999
    while left < right:
        current_sum = arr[left] + arr[right]
        if abs(target_sum - current_sum) < abs(target_sum - closest_sum):
            closest_sum = current_sum

        if (target_sum - current_sum) > 0:
            left += 1
        else:
            right -= 1
    return closest_sum


def triplet_sum_close_to_zero(arr, target_sum) -> int:
    """
    Triplet Sum Close to Target (medium)
    Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to
    the target number as possible.
    Input: [-2, 0, 1, 2], target=2
    Output: 1
    Explanation: The triplet [-2, 1, 2] has the closest sum to the target

    Computation: O(n log n) + O(N)*O(N) --> O(N^2)
    Memory: O(N) for sorting
    """
    arr.sort()
    smallest_diff = math.inf
    for i in range(len(arr)-2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            # ピタリ賞を発見
            if target_sum == current_sum:
                return target_sum

            diff = target_sum - current_sum
            if abs(smallest_diff) > abs(diff):
                smallest_diff = diff
            if diff > 0:
                left += 1
            else:
                right -= 1
    return target_sum - smallest_diff


def triplet_with_smaller_sum(arr: List, target: int) -> int:
    """
    Triplets with Smaller Sum (medium)
    Given an array arr of unsorted numbers and a target sum, count all triplets in it such that
    arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
    Write a function to return the count of such triplets.

    Example 1:
    Input: [-1, 0, 2, 3], target=3
    Output: 2
    Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

    Computation: O(n log n) for sorting + O(N)*O(N) ==> O(N^2)
    Memory: O(N) for sorting which is in-place algorithm
    """
    arr.sort()

    count = 0
    for i in range(len(arr)-2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            cursum = arr[i] + arr[left] + arr[right]
            if cursum < target:
                count += right - left  # arrはsortされているので、rightを、rightとleft間のどの要素にしてもHitする
                left += 1
            else:
                right -= 1
    return count


def triplet_with_smaller_sum_l(arr: List, target: int) -> List:
    """
    triplet_with_smaller_sumのカウントではなく、tripletのリストを返すバージョン
    Computation: O(n log n) + O(N) * O(N) * O(N) ==> O(N^3)
    Memory: O(N) for sorting + O(N) for triplets
    """
    arr.sort()
    triplets = []
    for i in range(len(arr)-2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum < target:
                # right-left間で、rightを動かして、組み合わせを作る
                for right_idx in range(right, left, -1):
                    triplets.append([arr[i], arr[left], arr[right_idx]])
                left += 1
            else:
                right -= 1
    return triplets
