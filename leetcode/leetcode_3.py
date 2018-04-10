''' LeetCode 3

Given a string, find the length of the longest substring without
repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence
and not a substring.
'''
# return 0 is nothing
# get longest substring without repeating characters
# longest in order e.g. 'pwek' then 'pwe' instead of 'wek' as 'pwe' is first


def length_of_longest_substring(s):
    if not s:
        return 0
    # for completely repeatitive strings
    if len(set(s)) == 1:
        return 1
    capture = []
    start = 0
    for i in range(1, len(s)):
        substring = s[start:i + 1]
        # if repeated characters in substring then slide
        if len(set(substring)) < len(substring):
            start += 1
            continue
        # add all non-repeated substring to a list
        capture.append(substring)
    capture.sort(key=len, reverse=True)
    return len(capture[0])


assert length_of_longest_substring('abcabcbb') == 3  # 'abc'
assert length_of_longest_substring('bbbbb') == 1  # 'b'
assert length_of_longest_substring('pwwkew') == 3  # 'wke'
assert length_of_longest_substring('au') == 2  # 'au'
assert length_of_longest_substring('aab') == 2  # 'ab'
assert length_of_longest_substring('a') == 1  # 'a'
