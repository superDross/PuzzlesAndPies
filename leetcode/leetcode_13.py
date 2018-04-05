''' LeetCode 13

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''


def rom2int(s):
    d = {'I': 1, 'X': 10,
         'V': 5,  'L': 50,
         'C': 100, 'D': 500,
         'M': 1000}

    dd = {'IV': 4,
          'IX': 9, 'XL': 40,
          'XC': 90, 'CD': 400,
          'CM': 900}
    # convert double numerals
    converted_doubles = []
    for k in dd.keys():
        if k in s:
            converted_doubles.append(dd.get(k))
            s = s.replace(k, '')
    converted = sum(converted_doubles + [d.get(x) for x in list(s)])
    if converted < 4000:
        return converted


print(rom2int("MCMXCVI"))
