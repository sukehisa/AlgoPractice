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
