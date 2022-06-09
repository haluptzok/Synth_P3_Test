from typing import List
def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 0
def sol():
    """Find a string with 1000 'o's but no two adjacent 'o's."""
    return ('h' + 'o') * 1000
assert sat(sol())

def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801
def sol():
    """Find a string with 1000 'o's, 100 pairs of adjacent 'o's and 801 copies of 'ho'."""
    return 'ho' * (800 + 1) + 'o' * (100 * 2 - 1)
assert sat(sol())

def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))
def sol():
    """Find a permutation of [0, 1, ..., 998] such that the ith element is *not* i, for all i=0, 1, ..., 998."""
    return [((i + 1) % 999) for i in range(999)]
assert sat(sol())

