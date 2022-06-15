from typing import List

def sat10(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))
def sol10():
    """
    Find a list of strings whose length (viewed as a string) is equal to the lexicographically largest element
    and is equal to the lexicographically smallest element.
    """
    return ['1']
# assert sat10(sol10())

def sat11(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000
def sol11():
    """Find a list of 1,000 integers where every two adjacent integers sum to 9, and where the first
    integer plus 4 is 9."""
    return [9 - 4, 4] * (1000 // 2)
# assert sat11(sol11())

def sat12(x: float):
    return str(x - 3.1415).startswith("123.456")
def sol12():
    """Find a real number which, when you subtract 3.1415, has a decimal representation starting with 123.456."""
    return 123.456 + 3.1415
# assert sat12(sol12())

def sat13(li: List[int]):
    return all([sum(li[:i]) == i for i in range(20)])
def sol13():
    """Find a list of integers such that the sum of the first i integers is i, for i=0, 1, 2, ..., 19."""
    return [1] * 20
# assert sat13(sol13())

def sat14(li: List[int]):
    return all(sum(li[:i]) == 2 ** i - 1 for i in range(20))
def sol14():
    """Find a list of integers such that the sum of the first i integers is 2^i -1, for i = 0, 1, 2, ..., 19."""
    return [(2 ** i) for i in range(20)]
# assert sat14(sol14())

def sat15(s: str):
    return float(s) + len(s) == 4.5
def sol15():
    """Find a real number such that when you add the length of its decimal representation to it, you get 4.5.
    Your answer should be the string form of the number in its decimal representation."""
    return str(4.5 - len(str(4.5)))
# assert sat15(sol15())

def sat16(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))
def sol16():
    """Find a number whose decimal representation is *a longer string* when you add 1,000 to it than when you add 1,001."""
    return -1001
# assert sat16(sol16())

def sat17(ls: List[str]):
    return [s + t for s in ls for t in ls if s != t] == 'berlin berger linber linger gerber gerlin'.split()
def sol17():
    """
    Find a list of strings that when you combine them in all pairwise combinations gives the six strings:
    'berlin', 'berger', 'linber', 'linger', 'gerber', 'gerlin'
    """
    seen = set()
    ans = []
    for s in 'berlin berger linber linger gerber gerlin'.split():
        t = s[:3]
        if t not in seen:
            ans.append(t)
            seen.add(t)
    return ans
# assert sat17(sol17())

def sat18(li: List[int]):
    return {i + j for i in li for j in li} == {0, 1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 34}
def sol18():
    """
    Find a list of integers whose pairwise sums make the set {0, 1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 34}.
    That is find L such that, { i + j | i, j in L } = {0, 1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 34}.
    """
    return [0, 1, 2, 3, 17]
# assert sat18(sol18())

def sat19(li: List[int]):
    return all(j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128]))
def sol19():
    """
    Find a list of integers, starting with 0 and ending with 128, such that each integer either differs from
    the previous one by one or is thrice the previous one.
    """
    return [1, 3, 4, 12, 13, 14, 42, 126, 127]
# assert sat19(sol19())

