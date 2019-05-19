__author__ = 'yusuke'



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
