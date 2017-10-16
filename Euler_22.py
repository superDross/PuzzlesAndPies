''' Euler 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin 
by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its 
alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th 
name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

'''
import requests
import bs4

def get_names():
    req = requests.get("https://projecteuler.net/project/resources/p022_names.txt")
    req.raise_for_status()
    url = bs4.BeautifulSoup(req.text, features='lxml')
    return url.text

def get_sorted_names():
    names = get_names()
    name_list = [x.replace('"', '') for x in names.split(',')]
    sorted_name_list = sorted(name_list)
    return sorted_name_list

def total_n(sorted_name_list):
    numbers = []
    count = 0
    for name in sorted_name_list:
        name_number = []
        for letter in name.lower():
            n = ord(letter) - 96
            name_number.append(n)
        count += 1
        numbers.append(sum(name_number) * count)
    return numbers

# 871198282
s = get_sorted_names()
answer = sum(total_n(s))
print(answer)

# quicker but not very readable
#print(sum([sum([ord(l.lower()) - 96 for l in list(n)]) * c for c, n in enumerate(s, 1)]))
