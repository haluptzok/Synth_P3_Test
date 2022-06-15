from typing import List

def sat0(s: str):
    return s.count('o') == 1000 and s.count('oo') == 0
def sol0():
    """Find a string with 1000 'o's but no two adjacent 'o's."""
    return ('h' + 'o') * 1000
# assert sat0(sol0())

def sat1(s: str):
    return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801
def sol1():
    """Find a string with 1000 'o's, 100 pairs of adjacent 'o's and 801 copies of 'ho'."""
    return 'ho' * (800 + 1) + 'o' * (100 * 2 - 1)
# assert sat1(sol1())

def sat2(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))
def sol2():
    """Find a permutation of [0, 1, ..., 998] such that the ith element is *not* i, for all i=0, 1, ..., 998."""
    return [((i + 1) % 999) for i in range(999)]
# assert sat2(sol2())

def sat3(li: List[int]):
    return len(li) == 10 and li.count(li[3]) == 2
def sol3():
    """Find a list of length 10 where the fourth element occurs exactly twice."""
    return list(range(10 // 2)) * 2
# assert sat3(sol3())

def sat4(li: List[int]):
    return all([li.count(i) == i for i in range(10)])
def sol4():
    """Find a list integers such that the integer i occurs i times, for i = 0, 1, 2, ..., 9."""
    return [i for i in range(10) for j in range(i)]
# assert sat4(sol4())

def sat5(i: int):
    return i % 123 == 4 and i > 10 ** 10
def sol5():
    """Find an integer greater than 10^10 which is 4 mod 123."""
    return 4 + 10 ** 10 + 123 - 10 ** 10 % 123
# assert sat5(sol5())

def sat6(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3
def sol6():
    """Find a three-digit pattern  that occurs more than 8 times in the decimal representation of 8^2888."""
    s = str(8 ** 2888)
    return max({s[i: i + 3] for i in range(len(s) - 2)}, key=lambda t: s.count(t))
# assert sat6(sol6())

def sat7(ls: List[str]):
    return ls[1234] in ls[1235] and ls[1234] != ls[1235]
def sol7():
    """Find a list of more than 1235 strings such that the 1234th string is a proper substring of the 1235th."""
    return [''] * 1235 + ['a']
# assert sat7(sol7())

def sat8(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")
def sol8():
    """
    Find a way to rearrange the letters in the pangram "The quick brown fox jumps over the lazy dog" to get
    the pangram "The five boxing wizards jump quickly". The answer should be represented as a list of index
    mappings.
    """
    return ['The quick brown fox jumps over the lazy dog'.index(t)
            for t in 'The five boxing wizards jump quickly']
# assert sat8(sol8())

def sat9(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11
def sol9():
    """Find a palindrome of length greater than 11 in the decimal representation of 8^1818."""
    s = str(8 ** 1818)
    return next(s[i: i + le]
                for le in range(12, len(s) + 1)
                for i in range(len(s) - le + 1)
                if s[i: i + le] == s[i: i + le][::-1]
                )
# assert sat9(sol9())

