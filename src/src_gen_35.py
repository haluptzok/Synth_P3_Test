from typing import List

def sat350(s: str, n=1000):
    return len(s) == n
def sol350(n=1000):
    """Find a string of length n"""
    return 'a' * n
# assert sat350(sol350())

def sat351(i: int, s="cat", target="a"):
    return s[i] == target
def sol351(s="cat", target="a"):
    """Find the index of target in string s"""
    return s.index(target)
# assert sat351(sol351())

def sat352(i: int, s="cat", target="a"):
    return s[i] == target and i < 0
def sol352(s="cat", target="a"):
    """Find the index of target in s using a negative index."""
    return - (len(s) - s.index(target))
# assert sat352(sol352())

def sat353(inds: List[int], s="hello world", target="do"):
    i, j, k = inds
    return s[i:j:k] == target
def sol353(s="hello world", target="do"):
    """Find the three slice indices that give the specific target in string s"""
    from itertools import product
    for i, j, k in product(range(-len(s) - 1, len(s) + 1), repeat=3):
        try:
            if s[i:j:k] == target:
                return [i, j, k]
        except (IndexError, ValueError):
            pass
# assert sat353(sol353())

def sat354(s: str, big_str="foobar", index=2):
    return big_str.index(s) == index
def sol354(big_str="foobar", index=2):
    """Find a string whose *first* index in big_str is index"""
    return big_str[index:]
# assert sat354(sol354())

def sat355(big_str: str, sub_str="foobar", index=2):
    return big_str.index(sub_str) == index
def sol355(sub_str="foobar", index=2):
    """Find a string whose *first* index of sub_str is index"""
    i = ord('A')
    while chr(i) in sub_str:
        i += 1
    return chr(i) * index + sub_str
# assert sat355(sol355())

def sat356(s: str, a="hello", b="yellow", length=4):
    return len(s) == length and s in a and s in b
def sol356(a="hello", b="yellow", length=4):
    """Find a string of length length that is in both strings a and b"""
    for i in range(len(a) - length + 1):
        if a[i:i + length] in b:
            return a[i:i + length]
# assert sat356(sol356())

def sat357(substrings: List[str], s="hello", count=15):
    return len(substrings) == len(set(substrings)) >= count and all(sub in s for sub in substrings)
def sol357(s="hello", count=15):
    """Find a list of >= count distinct strings that are all contained in s"""
    return [""] + sorted({s[j:i] for i in range(len(s) + 1) for j in range(i)})
# assert sat357(sol357())

def sat358(string: str, substring="a", count=10, length=100):
    return string.count(substring) == count and len(string) == length
def sol358(substring="a", count=10, length=100):
    """Find a string with a certain number of copies of a given substring and of a given length"""
    c = chr(1 + max(ord(c) for c in (substring or "a")))  # a character not in substring
    return substring * count + (length - len(substring) * count) * '^'
# assert sat358(sol358())

def sat359(x: str, parts=['I', 'love', 'dumplings', '!'], length=100):
    return len(x) == length and x.split() == parts
def sol359(parts=['I', 'love', 'dumplings', '!'], length=100):
    """Find a string of a given length with a certain split"""
    joined = " ".join(parts)
    return joined + " " * (length - len(joined))
# assert sat359(sol359())

