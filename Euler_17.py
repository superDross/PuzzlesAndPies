''' Euler 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
     8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
     14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
     19: 'nineteen', 0:''}


dd = {2: 'twenty', 3: 'thirty', 4:'forty', 5: 'fifty', 6:'sixty', 7: 'seventy',
      8: 'eighty', 9: 'ninety'}


def num2words():

    numbers = ['onethousand']

    for n in range(1, 1000):
        if not d.get(n):
            s = str(n)

            if len(s) == 2:
                z = dd.get(int(s[0])) + d.get(int(s[1]))
                numbers.append(z)

            elif len(s) == 3:
                if s[1] == '1':
                    z = d.get(int(s[0])) + 'hundred' + 'and' + d.get(int(s[1:]))
                    
                elif int(s[1]) > 1:
                    z = d.get(int(s[0])) + 'hundred' + 'and' + dd.get(int(s[1])) + d.get(int(s[2]))

                elif s[1:] == '00':
                    z = d.get(int(s[0])) + 'hundred'

                else:
                    z = d.get(int(s[0])) + 'hundred' + 'and' + d.get(int(s[2]))
                numbers.append(z)

        else:
            numbers.append(d.get(n))

    return numbers


# 21124
w = num2words()
answer = len(''.join(w))
print(answer)


