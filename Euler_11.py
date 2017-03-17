import pandas as pd
import itertools
import time

def main(df):
    ''' From a DataFrame of equal dimensions, extract a 
        list of numbers from from all possible directions,
        split into fours and determine which list of four 
        values gives the highest number when multiplied 
        together.
    
    Args:
        df: DataFrame of equal dimensions
    
    Returns:
        The greatest product of four adjacent numbers in all 
        possible directions of the given DataFrame.
        
    '''
    start = time.time()
    # extract the maximum key from a dict
    get_max = lambda x: max([k for k, v in x.items()])

    max_total_all = {}
    for comb in itertools.product([False, True], repeat=4):
        one, two, three, four = comb
        thing = up_down_left_right(df, forward=one, column=two, diagonal=three, diag_left=four)
        max_num = get_max(thing)
        max_values = thing.get(max_num)
        max_total_all[max_num] = max_values
    
    abs_max = get_max(max_total_all)
    
    
    elapsed = (time.time() - start)
    print("Completed in {} seconds".format(elapsed))
    
    return "{} in {}".format(abs_max, max_total_all.get(abs_max))



def up_down_left_right(df, forward=True, column=False, diagonal=False, diag_left=True):
    ''' From a DataFrame of equal dimensions, extract a list of numbers
        in a given direction, split the list into groups of fours and
        multiply all four number. Store the number in a dict along with 
        the list of four numbers.
        
    Args:
        df: DataFrame of equal dimensions
        forward: traverse the list of numbers forward or backwards
        column: traverse the df by column by column or row by row
        diaganol: traverse diaganolly across the dataframe or not
        diag_left: traverse diaganolly left to right or right to left
    
    Returns:
        a dictionary storing the four numbers as the value and the
        multiplication of the four numbers as the key
    '''
    
    if forward:
        count=range(20)
    else:
        count=range(20,-1,-1)

    sums = {}

    
    for num in range(20):
        # determine which direction to extract the numbers from
        if column and not diagonal: # column by column
            line = df[num]
        elif column and diagonal: # diagnol column
            line = diag(df, col=num, left_to_right=diag_left)
        elif not column and diagonal: # diagnol row
            line = diag(df, row=num, left_to_right=diag_left)
        elif not column and not diagonal: # row by row
            line = df.iloc[num]

        # split line into list of fours, multiply and ad to dictionary
        for start in count:

            if forward:
                end = start+4
                split_line = line[start:end]
                #print(start, end)
            else: # backward
                end = start-4
                split_line = line[end:start]
                #print(end, start)

            if start < 21 and end < 21:
                
                fours = split_line.tolist() if not isinstance(split_line, list) else split_line
                total = multiply(fours)
                sums[total] = fours
    
    return sums



def diag(df, col=0, row=0, left_to_right=True):
    ''' From a dataframe of equal dimensions, get all 
        numbers in a diaganol direction from thea given
        starting point and return all extracted numbers 
        in a list.
        
    Args:
        df: DataFrame of equal dimensions
        col: column index to start from
        row: crow index to start from
        left_to_right: travel diaganolly from left to right or right to left
    
    Return:
        a list of extracted numbers
    '''
    if not left_to_right:
        count = range(19, -1, -1)
    else:
        count = range(20)
    
    diag_line = []
    for fpos, rpos in zip(range(0,20), count):
        #print(fpos, rpos)
        if fpos+col < 20 and  rpos-row < 20 and rpos-row > -1:
            
            n = df.iloc[fpos+col, rpos-row]
            diag_line.append(n)
        
    return diag_line



def multiply(numbers):  
    ''' Multiply all numbers in a given list
    '''
    total = 1
    for x in numbers:
        total *= x  
    return total  




# prepare DataFrame
nums = [
        ['08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08'],
        ['49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00'],
        ['81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65'],
        ['52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91'],
        ['22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80'],
        ['24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50'],
        ['32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70'],
        ['67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21'],
        ['24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72'],
        ['21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95'],
        ['78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92'],
        ['16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57'],
        ['86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58'],
        ['19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40'],
        ['04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66'],
        ['88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69'],
        ['04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36'],
        ['20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16'],
        ['20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54'],
        ['01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48']
       ]

split_nums = [x.split(" ") for y in nums for x in y]

df = pd.DataFrame(split_nums)
df = df.apply(pd.to_numeric, args=('coerce',))

print(main(df))
# Completed in 0.4679758548736572 seconds
# 70600674 in [89, 94, 97, 87]

