from typing import List

def sat20(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3
def sol20():
    """
    Find a list integers containing exactly three distinct values, such that no integer repeats
    twice consecutively among the first eleven entries. (So the list needs to have length greater than ten.)
    """
    return list(range(3)) * 10
# assert sat20(sol20())

def sat21(s: str):
    return s[::2] in s and len(set(s)) == 5
def sol21():
    """
    Find a string s containing exactly five distinct characters which also contains as a substring every other
    character of s (e.g., if the string s were 'parrotfish' every other character would be 'profs').
    """
    return """abacadaeaaaaaaaaaa"""
# assert sat21(sol21())

def sat22(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')
def sol22():
    """
    Find a list of characters which are aligned at the same indices of the three strings 'dee', 'doo', and 'dah!'.
    """
    return list(next(zip('dee', 'doo', 'dah!')))
# assert sat22(sol22())

def sat23(li: List[int]):
    return li.count(17) == 3 and li.count(3) >= 2
def sol23():
    """Find a list of integers with exactly three occurrences of seventeen and at least two occurrences of three."""
    return [17] * 3 + [3] * 2
# assert sat23(sol23())

def sat24(s: str):
    return sorted(s) == sorted('Permute me true') and s == s[::-1]
def sol24():
    """Find a permutation of the string 'Permute me true' which is a palindrome."""
    s = sorted('Permute me true'[1:])[::2]
    return "".join(s + ['P'] + s[::-1])
# assert sat24(sol24())

def sat25(ls: List[str]):
    return "".join(ls) == str(8 ** 88) and all(len(s) == 8 for s in ls)
def sol25():
    """Divide the decimal representation of 8^88 up into strings of length eight."""
    return [str(8 ** 88)[i:i + 8] for i in range(0, len(str(8 ** 88)), 8)]
# assert sat25(sol25())

def sat26(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[li[0]]] == li[li[li[1]]]
def sol26():
    """
    Consider a digraph where each node has exactly one outgoing edge. For each edge (u, v), call u the parent and
    v the child. Then find such a digraph where the grandchildren of the first and second nodes differ but they
    share the same great-grandchildren. Represented this digraph by the list of children indices.
    """
    return [1, 2, 3, 3]
# assert sat26(sol26())

def sat27(li: List[int]):
    return all(i in range(1000) and abs(i - j) >= 10 for i in li for j in li if i != j) and len(set(li)) == 100
def sol27():
    """Find a list of one hundred integers between 0 and 999 which all differ by at least ten from one another."""
    return list(range(0, 1000, 10))
# assert sat27(sol27())

def sat28(l: List[int]):
    return all(i in range(1000) and abs(i * i - j * j) >= 10 for i in l for j in l if i != j) and len(set(l)) > 995
def sol28():
    """
    Find a list of more than 995 distinct integers between 0 and 999, inclusive, such that each pair of integers
    have squares that differ by at least 10.
    """
    return [0, 4] + list(range(6, 1000))
# assert sat28(sol28())

def sat29(li: List[int]):
    return all([123 * li[i] % 1000 < 123 * li[i + 1] % 1000 and li[i] in range(1000) for i in range(20)])
def sol29():
    """
    Define f(n) to be the residue of 123 times n mod 1000. Find a list of integers such that the first twenty one
    are between 0 and 999, inclusive, and are strictly increasing in terms of f(n).
    """
    return sorted(range(1000), key=lambda n: 123 * n % 1000)[:21]
# assert sat29(sol29())

