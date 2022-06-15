from typing import List

def sat360(x: str, parts=['I', 'love', 'dumplings', '!', ''], string="I_love_dumplings_!_"):
    return string.split(x) == parts
def sol360(parts=['I', 'love', 'dumplings', '!', ''], string="I_love_dumplings_!_"):
    """Find a separator that when used to split a given string gives a certain result"""
    if len(parts) <= 1:
        return string * 2
    length = (len(string) - len("".join(parts))) // (len(parts) - 1)
    start = len(parts[0])
    return string[start:start + length]
# assert sat360(sol360())

def sat361(x: str, parts=['I!!', '!love', 'dumplings', '!', ''], string="I!!!!!love!!dumplings!!!!!"):
    return x.join(parts) == string
def sol361(parts=['I!!', '!love', 'dumplings', '!', ''], string="I!!!!!love!!dumplings!!!!!"):
    """
    Find a separator that when used to join a given string gives a certain result.
    This is related to the previous problem but there are some edge cases that differ.
    """
    if len(parts) <= 1:
        return ""
    length = (len(string) - len("".join(parts))) // (len(parts) - 1)
    start = len(parts[0])
    return string[start:start + length]
# assert sat361(sol361())

def sat362(parts: List[str], sep="!!", string="I!!!!!love!!dumplings!!!!!"):
    return sep.join(parts) == string and all(sep not in p for p in parts)
def sol362(sep="!!", string="I!!!!!love!!dumplings!!!!!"):
    """Find parts that when joined give a specific string."""
    return string.split(sep)
# assert sat362(sol362())

def sat363(li: List[int], dups=42155):
    return len(set(li)) == len(li) - dups
def sol363(dups=42155):
    """Find a list with a certain number of duplicate items"""
    return [1] * (dups + 1)
# assert sat363(sol363())

def sat364(li: List[int], target=[17, 9, -1, 17, 9, -1], n=2):
    return li * n == target
def sol364(target=[17, 9, -1, 17, 9, -1], n=2):
    """Find a list that when multiplied n times gives the target list"""
    if n == 0:
        return []
    return target[:len(target) // n]
# assert sat364(sol364())

def sat365(li: List[int], n=85012):
    return len(li) == n
def sol365(n=85012):
    """Find a list of a given length n"""
    return [1] * n
# assert sat365(sol365())

def sat366(i: int, li=[17, 31, 91, 18, 42, 1, 9], target=18):
    return li[i] == target
def sol366(li=[17, 31, 91, 18, 42, 1, 9], target=18):
    """Find the index of an item in a list. Any such index is fine."""
    return li.index(target)
# assert sat366(sol366())

def sat367(i: int, li=[17, 31, 91, 18, 42, 1, 9], target=91):
    return li[i] == target and i < 0
def sol367(li=[17, 31, 91, 18, 42, 1, 9], target=91):
    """Find the index of an item in a list using negative indexing."""
    return li.index(target) - len(li)
# assert sat367(sol367())

def sat368(inds: List[int], li=[42, 18, 21, 103, -2, 11], target=[-2, 21, 42]):
    i, j, k = inds
    return li[i:j:k] == target
def sol368(li=[42, 18, 21, 103, -2, 11], target=[-2, 21, 42]):
    """Find three slice indices to achieve a given list slice"""
    from itertools import product
    for i, j, k in product(range(-len(li) - 1, len(li) + 1), repeat=3):
        try:
            if li[i:j:k] == target:
                return [i, j, k]
        except (IndexError, ValueError):
            pass
# assert sat368(sol368())

def sat369(item: int, li=[17, 2, 3, 9, 11, 11], index=4):
    return li.index(item) == index
def sol369(li=[17, 2, 3, 9, 11, 11], index=4):
    """Find the item whose first index in li is index"""
    return li[index]
# assert sat369(sol369())

