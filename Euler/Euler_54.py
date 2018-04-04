import numpy as np
import numpy.core.defchararray as npc
import requests
import bs4

def get_poker_file():
    req = requests.get('https://projecteuler.net/project/resources/p054_poker.txt')
    req.raise_for_status()
    url = bs4.BeautifulSoup(req.text, features='lxml')
    poker = np.array([list(x.replace(' ', '')) for x in url.text.split("\n")][:-1])
    return poker

def alter_poker_values(poker):
    d = {'T': '10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'}
    for k in d:
        poker = npc.replace(poker, k, d[k])
    return poker

poker = get_poker_file()
poker = alter_poker_values(poker)

p1, p2 = np.hsplit(poker.astype(str), [10])

values = poker[:, ::2].astype(int)
suits = poker[:, 1::2]
p1_values, p2_values = np.hsplit(values, [10])
p1_suits, p2_suits = np.hsplit(suits, [10])


np.equal.reduce(p1_values)

