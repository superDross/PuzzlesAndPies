class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if '' in strs or not strs:
            return ''
        match = ''
        for i in range(len(strs[0])):
            try:
                letter = strs[0][i]
                if all(s[i] == letter for s in strs):
                    match += letter
                else:
                    return match
            except IndexError:
                return match
        return match
