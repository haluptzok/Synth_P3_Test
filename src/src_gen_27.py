from typing import List

def sat270(x: List[int], a=7, s=5, e=200):
    return x[0] == a and x[-1] <= e and (x[-1] + s > e) and all([x[i] + s == x[i + 1] for i in range(len(x) - 1)])
def sol270(a=7, s=5, e=200):
    """Create a list that is a subrange of an arithmetic sequence."""
    return list(range(a, e + 1, s))
assert sat270(sol270())

def sat271(x: List[int], a=8, r=2, l=50):
    return x[0] == a and len(x) == l and all([x[i] * r == x[i + 1] for i in range(len(x) - 1)])
def sol271(a=8, r=2, l=50):
    """Create a list that is a subrange of an gemoetric sequence."""
    return [a * r ** i for i in range(l)]
assert sat271(sol271())

def sat272(e: List[int], a=2, b=-1, c=1, d=2021):
    x = e[0] / e[1]
    return abs(a * x + b - c * x - d) < 10 ** -5
def sol272(a=2, b=-1, c=1, d=2021):
    """
    Find the intersection of two lines.
    Solution should be a list of the (x,y) coordinates.
    Accuracy of fifth decimal digit is required.
    """
    return [d - b, a - c]
assert sat272(sol272())

def sat273(x: int, a=324554, b=1345345):
    if a < 50:
        return x + a == b
    else:
        return x - 2 * a == b
def sol273(a=324554, b=1345345):
    """Satisfy a simple if statement"""
    if a < 50:
        return b - a
    else:
        return b + 2 * a
assert sat273(sol273())

def sat274(x: int, a=9384594, b=1343663):
    if x > 0 and a > 50:
        return x - a == b
    else:
        return x + a == b
def sol274(a=9384594, b=1343663):
    """Satisfy a simple if statement with an and clause"""
    if a > 50 and b > a:
        return b + a
    else:
        return b - a
assert sat274(sol274())

def sat275(x: int, a=253532, b=1230200):
    if x > 0 or a > 50:
        return x - a == b
    else:
        return x + a == b
def sol275(a=253532, b=1230200):
    """Satisfy a simple if statement with an or clause"""
    if a > 50 or b > a:
        return b + a
    else:
        return b - a
assert sat275(sol275())

def sat276(x: int, a=4, b=54368639):
    if a == 1:
        return x % 2 == 0
    elif a == -1:
        return x % 2 == 1
    else:
        return x + a == b
def sol276(a=4, b=54368639):
    """Satisfy a simple if statement with multiple cases"""
    if a == 1:
        x = 0
    elif a == -1:
        x = 1
    else:
        x = b - a
    return x
assert sat276(sol276())

def sat277(x: List[int], n=5, s=19):
    return len(x) == n and sum(x) == s and all([a > 0 for a in x])
def sol277(n=5, s=19):
    """Find a list of n non-negative integers that sum up to s"""
    x = [1] * n
    x[0] = s - n + 1
    return x
assert sat277(sol277())

def sat278(x: List[int], n=4, s=2021):
    return len(x) == n and sum(x) == s and len(set(x)) == n
def sol278(n=4, s=2021):
    """Construct a list of n distinct integers that sum up to s"""
    a = 1
    x = []
    while len(x) < n - 1:
        x.append(a)
        a = -a
        if a in x:
            a += 1

    if s - sum(x) in x:
        x = [i for i in range(n - 1)]

    x = x + [s - sum(x)]
    return x
assert sat278(sol278())

def sat279(x: str, s=['a', 'b', 'c', 'd', 'e', 'f'], n=4):
    return len(x) == n and all([x[i] == s[i] for i in range(n)])
def sol279(s=['a', 'b', 'c', 'd', 'e', 'f'], n=4):
    """Concatenate the list of characters in s"""
    return ''.join([s[i] for i in range(n)])
assert sat279(sol279())

