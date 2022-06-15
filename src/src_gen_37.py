from typing import List

def sat370(li: List[int], i=29, index=10412):
    return li.index(i) == index
def sol370(i=29, index=10412):
    """Find a list that contains i first at index index"""
    return [i - 1] * index + [i]
# assert sat370(sol370())

def sat371(s: str, a=['cat', 'dot', 'bird'], b=['tree', 'fly', 'dot']):
    return s in a and s in b
def sol371(a=['cat', 'dot', 'bird'], b=['tree', 'fly', 'dot']):
    """Find an item that is in both lists a and b"""
    return next(s for s in b if s in a)
# assert sat371(sol371())

def sat372(x: int, a=93252338):
    return -x == a
def sol372(a=93252338):
    """Solve a unary negation problem"""
    return - a
# assert sat372(sol372())

def sat373(x: int, a=1073258, b=72352549):
    return a + x == b
def sol373(a=1073258, b=72352549):
    """Solve a sum problem"""
    return b - a
# assert sat373(sol373())

def sat374(x: int, a=-382, b=14546310):
    return x - a == b
def sol374(a=-382, b=14546310):
    """Solve a subtraction problem"""
    return a + b
# assert sat374(sol374())

def sat375(x: int, a=8665464, b=-93206):
    return a - x == b
def sol375(a=8665464, b=-93206):
    """Solve a subtraction problem"""
    return a - b
# assert sat375(sol375())

def sat376(n: int, a=14302, b=5):
    return b * n + (a % b) == a
def sol376(a=14302, b=5):
    """Solve a multiplication problem"""
    return a // b
# assert sat376(sol376())

def sat377(n: int, a=3, b=23463462):
    return b // n == a
def sol377(a=3, b=23463462):
    """Solve a division problem"""
    if a == 0:
        return 2 * b
    for n in [b // a, b // a - 1, b // a + 1]:
        if b // n == a:
            return n
# assert sat377(sol377())

def sat378(n: int, a=345346363, b=10):
    return n // b == a
def sol378(a=345346363, b=10):
    """Find n that when divided by b is a"""
    return a * b
# assert sat378(sol378())

def sat379(x: int, a=10201202001):
    return x ** 2 == a
def sol379(a=10201202001):
    """Compute an integer that when squared equals perfect-square a."""
    return int(a ** 0.5)
# assert sat379(sol379())

