

def longest_palandromic_substring(s):
    '''
    Example:
        s = 'babadd'
        counter = 0
        s[0:6] = 'babadd'
        counter +=1
        s[0:5] = 'babad' # start = 0, end = end - counter
        s[1:6] = 'abadd' # start + 1, end + 1
        counter += 1
        s[0:4] = 'baba'  # start = 0, end = end - counter
        s[1:5] = 'abad'  # start + 1, end + 1
        s[2:6] = 'badd'  # start + 1, end + 1
        counter += 1
        s[0:3] = 'bab'   # start = 0, end = end - counter
        ....
    '''
    if len(s) == 1:
        return s
    start = 0
    end = len(s)
    counter = 1
    while counter <= len(s):
        while end <= len(s):
            # check if palandromic
            substring = s[start:end]
            reverse = substring[::-1]
            if substring == reverse:
                return substring
            # sliding window
            start += 1
            end += 1
        # shorten sliding window
        counter += 1
        start = 0
        end -= counter


assert longest_palandromic_substring('a') == 'a'
assert longest_palandromic_substring('babad') in ['aba', 'bab']
assert longest_palandromic_substring('cbbd') == 'bb'
assert longest_palandromic_substring('abb') == 'bb'
assert longest_palandromic_substring('bb') == 'bb'
assert longest_palandromic_substring('abcda') == 'a'
