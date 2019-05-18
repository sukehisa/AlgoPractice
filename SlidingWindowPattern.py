__author__ = 'yusuke'

import math


def max_sub_array_of_size_k(k, arr):
    """
    O(N) and O(1)
    """
    _sum = 0
    _max = -1
    window_start = 0

    if len(arr) < k or k == 0:
        return -1

    for window_end in range(len(arr)):
        _sum += arr[window_end]
        if window_end >= k-1:
            _max = max(_max, _sum)
            _sum -= arr[window_start]
            window_start += 1

    return _max


def smallest_subarray_with_given_sum_(s, arr):
    """
    1st try:
    Given an array of positive numbers and a positive number ‘S’, find the length of the smallest subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
    O(N*N), O(N)

    :param s:
    :param arr:
    :return:
    """
    for window_size in range(1, len(arr)+1):
        for left in range(len(arr) - window_size + 1):
            if sum(arr[left:left+window_size]) >= s:
                return window_size
    return 0


def smallest_subarray_with_given_sum(s, arr):
    """
    O(N+N) -> O(N)
    O(1)
    :param s:
    :param arr:
    :return:
    """
    ans = math.inf
    window_sum = 0
    window_start = 0
    for window_end in range(0, len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            ans = min(ans, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if ans == math.inf:
        return 0
    else:
        return ans

def longest_substring_with_k_distinct_dup(str, k):
    ans = -1
    cntmap = {}
    window_start = 0
    for window_end in range(0, len(str)):
        end_char = str[window_end]
        end_cnt = cntmap.get(end_char, 0) + 1
        cntmap[end_char] = end_cnt
        if end_cnt > k:
            while True:
                window_start += 1
                start_char = str[window_start]
                start_cnt = cntmap.get(start_char, 0) - 1
                cntmap[start_char] = start_cnt
                if start_char == end_char:
                    break
        ans = (window_end - window_start) + 1
    return ans

def longest_substring_with_k_distinct(str, k):
    """
    Given a string, find the length of the longest substring in it with no more than K distinct characters.
    Input: String="araaci", K=2
    Output: 4
    Explanation: The longest substring with no more than '2' distinct characters is "araa".

    araaci, 1 => 2  (which is [aa])

    O(N+N) -> O(N), O(k)

    :param str:
    :param k:
    :return:
    """
    ans = -1
    charset = set()

    window_start = 0
    for window_end in range(0, len(str)):
        end_char = str[window_end]
        charset.add(end_char)
        while len(charset) > k:
            start_char = str[window_start]
            try:
                charset.remove(start_char)
            except KeyError:
                pass
            window_start += 1
        ans = max(ans, (window_end - window_start) + 1)

    return ans


def fruits_into_baskets(fruits):
    """
    find the length of the longest subarray with no more than two distinct characters (or fruit types!).
    ['A', 'B', 'C', 'B', 'B', 'C'] -> 5  (b, c, b, b, c)
    :param fruits:
    :return:
    """
    ans = -1
    fruitset = set()

    window_start = 0
    for window_end in range(len(fruits)):
        end_char = fruits[window_end]
        fruitset.add(end_char)

        while len(fruitset) > 2:
            start_char = fruits[window_start]
            try:
                fruitset.remove(start_char)
            except KeyError:
                pass
            window_start += 1

        ans = max(ans, window_end - window_start + 1)

    return ans

def non_repeat_substring__(str):
    """
    数は数えなくていい。non repeatingなので
    :param str:
    :return:
    """
    ans = -1
    charmap = {}
    window_start = 0
    for window_end in range(0, len(str)):
        ch = str[window_end]
        chcnt = charmap.get(ch, 0) + 1
        charmap[ch] = chcnt
        if chcnt > 1:
            while True:
                removing_ch = str[window_start]
                charmap[removing_ch] -= 1
                window_start += 1
                if removing_ch == ch:
                    break

        ans = max(ans, window_end - window_start + 1)
    return ans


def non_repeat_substring(str):
    """
    O(N): 外側のwindow_endのループ内に別のループはなし。
    O(N): worst caseでstr文字列長文のhashmapが必要
    :param str:
    :return:
    """
    ans = -1
    charindexmap = {}
    window_start = 0
    for window_end in range(0, len(str)):
        ch = str[window_end]
        if ch in charindexmap:
            # 重複なしなので、同じ文字を見つけたら、window_startは既存箇所の次のindexに動かす。
            window_start = max(window_start, charindexmap[ch]+1)
        charindexmap[ch] = window_end

        ans = max(ans, window_end - window_start + 1)
    return ans


def length_of_longest_substring(str, k):
    """
    Longest Substring with Same Letters after Replacement (hard)
    Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter,
    find the length of the longest substring having the same letters after replacement.
    aabccbb, k=2 -> 5 ('c'->'b'  ==> 'bbbbb')
    Time: O(N + N) -> O(N)
    Space: O(N)
    :param str:
    :param k:
    :return:
    """
    ans = -1
    maxrepeating = 0
    chmap = {}
    window_start = 0
    for window_end in range(0, len(str)):
        ch = str[window_end]
        chmap[ch] = chmap.get(ch, 0) + 1
        maxrepeating = max(maxrepeating, chmap[ch])

        if ((window_end - window_start + 1) - maxrepeating) > k:
            chmap[str[window_start]] -= - 1
            window_start += 1

        ans = max(ans, window_end - window_start + 1)
    return ans

