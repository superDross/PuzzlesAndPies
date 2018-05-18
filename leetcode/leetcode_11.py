
def int2rom(n):
    d = {'1': 'I', '10': 'X',
         '5': 'V',  '50': 'L',
         '100': 'C', '500': 'D',
         '1000': 'M', '4': 'IV',
         '9': 'IX', '40': 'XL',
         '90': 'XC', '400': 'CD',
         '900': 'CM'}
    numerals = []
    n = list(str(n))
    for i in range(0, len(n)):
        digit = n[i]
        # add apropriate number of zeros
        zeros = '0' * (len(n) - (i + 1))
        digit += zeros
        numeral = d.get(digit)
        numerals.append(numeral)
    return ''.join(numerals)


print(int2rom(499))


dd = {'1': 'I', '10': 'X',
      '5': 'V',  '50': 'L',
      '100': 'C', '500': 'D',
      '1000': 'M', '4': 'IV',
      '9': 'IX', '40': 'XL',
      '90': 'XC', '400': 'CD',
      '900': 'CM'}

for n in range(1, 3999):
    # l = list(str(n))
    # for i in range(0, len(l)):
    #     get_zeros(l[0], i+1)
    if 1 < int(n) < 5:
        n = dd.get('1') * int(n)
    elif 5 < int(n) < 9:
        five = dd.get('5')
        ones = dd.get('1') * (int(n) - 5)
        n = five+ones
    else:
        n = dd.get(str(n))
    print(n)

