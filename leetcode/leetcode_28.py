''' 28 - Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        if not needle or haystack == needle:
            return 0
        for i in range(len(haystack)):
            for j in range(i+1, len(haystack)+1):
                if haystack[i:j] == needle:
                    return i
        return -1


haystack, needle = ('hello', 'll')
haystack, needle = ('aaaaa', 'bba')
haystack, needle = ("mississippi", "pi")


print(Solution().strStr(haystack, needle))
