def get_roman_numeral_from_dict(n, fd):
    ''' Create a roman numeral from a dictionary.

    Args:
        n (int): number.
        fd (dict: {int: str): dictionary containing number: roman numeral.

    Example:
        n = 7
        fd = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX'}
        get_roman_numeral_from_dict(n, fd) = 'VII'
    '''
    if 1 <= n < 4:
        return fd.get(1) * n
    if n == 4:
        return fd.get(4)
    if n == 5:
        return fd.get(5)
    if 5 < n < 9:
        return fd.get(5) + (fd.get(1) * (n - 5))
    if n == 9:
        return fd.get(9)


def divide_power(d, i):
    ''' Divide a dictionaries keys to the power of i.

    Args:
        d (dict: {int: str}): dictionary containing keys as int type.
        i (int): number to the power of 10.

    Example:
        d = {400: 'CD', 500: 'D', 900: 'CM', 100: 'C'}
        i = 2
        divide_power(d, i) = {4: 'CD', 5: 'D', 9: 'CM', 1: 'C'}
    '''
    return {(k / (10 ** i)): r for k, r in d.items()}


def filter_roman_dictionary(i):
    ''' Filters roman numeral dictionary to a number of decimal places.

    Args:
        i (int): number to the power of 10.

    Example:
        filter_roman_dictionary(3) = {400: 'CD', 500: 'D', 900: 'CM', 100: 'C'}
    '''
    d = {1: 'I', 50: 'L', 500: 'D', 5: 'V', 1000: 'M', 100: 'C', 10: 'X',
         400: 'CD', 900: 'CM', 40: 'XL', 9: 'IX', 90: 'XC', 4: 'IV'}
    start = 10 ** (i - 1)
    end = 10 ** i
    fd = {num: r for num, r in d.items() if start <= num < end}
    return fd


def get_roman_numeral(n, i):
    ''' Convert a number with leading zeros to a roman numeral.

    Args:
        n (int): single digit representation of the number
                 to convert e.g. 20 then n=2.
        i (int): i to the power of 10; the number of digits.

    Exampe:
        get_roman_numeral(2, 2) = 'XX'
    '''
    n = int(n)
    # filter the roman dictionary keys to the same number of digits
    fd = filter_roman_dictionary(i)
    # divide the roman dictionary keys to single digits
    fd = divide_power(fd, (i - 1))
    # extract the roman numeral from the filtered roman dict
    roman = get_roman_numeral_from_dict(n, fd)
    return roman


def int2roman(n):
    ''' Convert an integer into a roman numeral.

    Args:
        n (int): number to convert into a roman numeral.
    '''
    if 0 < n < 4000:
        roman_numerals_l = []
        # turn the input into a reversed list
        n_list = list(str(n))[::-1]
        # iterate through the list with the number of digits
        for n_digits, n in enumerate(n_list, 1):
            # convert each digit to a roman numeral
            roman_numeral = get_roman_numeral(n, n_digits)
            if roman_numeral:
                roman_numerals_l.append(roman_numeral)
        # reverse roman numerals to correct order, join and return
        complete_roman_numeral = ''.join(roman_numerals_l[::-1])
        return complete_roman_numeral


# Test numerical limits
assert int2roman(-98) is None
assert int2roman(899909) is None
assert int2roman(4000) is None

# Test single digits
assert int2roman(1) == 'I'
assert int2roman(3) == 'III'
assert int2roman(4) == 'IV'
assert int2roman(5) == 'V'
assert int2roman(7) == 'VII'
assert int2roman(9) == 'IX'

# Test double digits
assert int2roman(10) == 'X'
assert int2roman(25) == 'XXV'
assert int2roman(48) == 'XLVIII'
assert int2roman(53) == 'LIII'
assert int2roman(87) == 'LXXXVII'
assert int2roman(96) == 'XCVI'

# Test triple digits
assert int2roman(123) == 'CXXIII'
assert int2roman(386) == 'CCCLXXXVI'
assert int2roman(444) == 'CDXLIV'
assert int2roman(528) == 'DXXVIII'
assert int2roman(798) == 'DCCXCVIII'
assert int2roman(968) == 'CMLXVIII'

# Test quadruple digits
assert int2roman(1994) == 'MCMXCIV'
assert int2roman(2089) == 'MMLXXXIX'
assert int2roman(3001) == 'MMMI'
assert int2roman(3999) == 'MMMCMXCIX'
