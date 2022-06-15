from typing import List

def sat200(trips: List[List[int]], a=[1, 0, -17, 42, 321, 36, 429, 35, 10, 923, 35, 18, 0, 17, 24, 32, 8], count=221):
    assert len({tuple(t) for t in trips}) >= count
    return all(0 <= i < j < k and (a[i] + a[j] + a[k]) % 3 == 0 for i, j, k in trips)
def sol200(a=[1, 0, -17, 42, 321, 36, 429, 35, 10, 923, 35, 18, 0, 17, 24, 32, 8], count=221):
    """Find all triples of increasing indices where the sum of the numbers is divisible by three

    a=[1, 2, 4, 8, 14, 10], count=2 => [[0, 2, 5], [1, 3, 4]] = > because 1 + 4 + 10, 2 + 8 + 14 are divisible by 3
    """
    n = len(a)
    return [[i, j, k] for k in range(2, n) for j in range(k) for i in range(j) if (a[i] + a[j] + a[k]) % 3 == 0]
# assert sat200(sol200())

def sat201(planets_between: List[str], a="Mars", b="Neptune"):
    assert " " not in "".join(planets_between)
    return " ".join([a] + planets_between + [b]) in "Venus Earth Mars Jupiter Saturn Uranus Neptune Pluto"
def sol201(a="Mars", b="Neptune"):
    """Find all planets between the two given planets

    a="Jupiter", b="Pluto" => ["Saturn" "Uranus" "Neptune"]
    """
    planets = "Venus Earth Mars Jupiter Saturn Uranus Neptune Pluto".split()
    return planets[planets.index(a) + 1:planets.index(b)]
# assert sat201(sol201())

def sat202(evens: List[str], words=['The', 'worm', 'ate', 'a', 'bird', 'imagine', 'that', '!', 'Absurd', '!!']):
    lens = [len(w) for w in evens]
    assert all(lens[i] % 2 == 0 and lens[i] == max(lens[:i + 1]) and w in words for i, w in enumerate(evens))
    return all((len(w) % 2 == 1 or w in evens) for w in words)
def sol202(words=['The', 'worm', 'ate', 'a', 'bird', 'imagine', 'that', '!', 'Absurd', '!!']):
    """Find the even-length words and sort them by length.

    ["soup", "not", "splendid"] => ["soup", "splendid"]
    """
    return sorted([w for w in words if len(w) % 2 == 0], key=lambda w: (len(w), w))
# assert sat202(sol202())

def sat203(neighbors: List[int], nums=[14, 7, 11, 13, 7, 4, 19, 2, 55, 13, 31, 14, 2, 9, -7, 0, 88, 13, 13]):

    def prime(m):
        return all(m % i for i in range(2, m - 1))

    goods = set()
    for i, n in enumerate(nums):
        if (i > 0 and prime(nums[i - 1])) or (i < len(nums) - 1 and prime(nums[i + 1])):
            goods.add(n)

    return set(neighbors) == goods and all(n == min(neighbors[i:]) for i, n in enumerate(neighbors))
def sol203(nums=[14, 7, 11, 13, 7, 4, 19, 2, 55, 13, 31, 14, 2, 9, -7, 0, 88, 13, 13]):
    """Find a list of all numbers that are adjacent to a prime number in the list, sorted without duplicates

    [2, 17, 16, 0, 6, 4, 5] => [2, 4, 16, 17]"""
    def prime(m):
        return all(m % i for i in range(2, m - 1))

    return sorted({
        n for i, n in enumerate(nums)
        if (i > 0 and prime(nums[i - 1])) or (i < len(nums) - 1 and prime(nums[i + 1]))
    })
# assert sat203(sol203())

def sat204(tot: int, xs=[123.0, 872322.0, 542.2, -127.5, 18214.0, 3732.4, 12832.4, 23523800.0]):
    for x in xs:
        if x.is_integer() and x > 0 and x % 2 == 0:
            tot -= int(x) ** 2

    return tot == 0
def sol204(xs=[123.0, 872322.0, 542.2, -127.5, 18214.0, 3732.4, 12832.4, 23523800.0]):
    """Find the sum of the squares of the positive even integers

    [2.0, 3.0, 2.5, 4.0] => 20
    """
    return sum(int(x) ** 2 for x in xs if x.is_integer() and x > 0 and x % 2 == 0)
# assert sat204(sol204())

def sat205(b: List[int], a=[1, 2, 3, 0, 4, 17, 2, 4, 5, 9, 8, 4], c=[1, 2, 3, 4, 0, 16, 2, 3, 5, 9, 8, 4]):
    return len(b) == len(a) and all(i + j == k for i, j, k in zip(a, b, c))
def sol205(a=[1, 2, 3, 0, 4, 17, 2, 4, 5, 9, 8, 4], c=[1, 2, 3, 4, 0, 16, 2, 3, 5, 9, 8, 4]):
    """Find an array that when added to vector a gives array vector c

    [1, 2, 3], [4, 17, 5] => [3, 15, 2]
    """
    return [k - i for i, k in zip(a, c)]
# assert sat205(sol205())

def sat206(s: str, class_name="TestClass", extensions=['extEnd', 'LOL', 'SuPeRbLy', 'v9ACLQWTEW', 'PickMe', 'AI']):
    assert s.startswith(class_name + ".")
    ext = s[len(class_name) + 1:]

    def case_delta(x: str):
        tot = 0
        for c in x:
            if c.isupper():
                tot += 1
            elif c.islower():
                tot -= 1
        return tot

    return ext in extensions and case_delta(ext) == max([case_delta(x) for x in extensions])
def sol206(class_name="TestClass", extensions=['extEnd', 'LOL', 'SuPeRbLy', 'v9ACLQWTEW', 'PickMe', 'AI']):
    """Find the class_name.extension for the extension that has the largest #capitals - #lowercase letters"""
    def case_delta(x: str):
        tot = 0
        for c in x:
            if c.isupper():
                tot += 1
            elif c.islower():
                tot -= 1
        return tot

    return class_name + "." + max(extensions, key=case_delta)
# assert sat206(sol206())

def sat207(r: str, s="light star", t="I love to look at the starlight!"):
    return r in t and len(r) == len(s) and r in s + s
def sol207(s="light star", t="I love to look at the starlight!"):
    """Find a rotation of string s that is a substring of t

    Input Example:
    s="test", t="I love lattes"

    Output Example:
    "ttes"
    """
    return next(s[i:] + s[:i] for i in range(len(s)) if s[i:] + s[:i] in t)
# assert sat207(sol207())

def sat208(n: int, evens=17, odds=3):
    for c in str(n):
        if int(c) % 2 == 0:
            evens -= 1
        else:
            odds -= 1
    return evens == 0 and odds == 0
def sol208(evens=17, odds=3):
    """Find an integer n >= 0 with the given number of even and odd digits.

    evens=3, odds=4 => 2381695"""
    return int("2" * evens + "1" * odds)
# assert sat208(sol208())

def sat209(roman: str, n=2414):
    key = {1000: 'm', 900: 'cm', 500: 'd', 400: 'cd',
           100: 'c', 90: 'xc', 50: 'l', 40: 'xl',
           10: 'x', 9: 'ix', 5: 'v', 4: 'iv',
           1: 'i'}
    m = 0
    for base in [1000, 100, 10, 1]:
        for mul in [9, 4, 5, 1, 1, 1]:  # up to three 1's, move on after 9 or 4
            val = base * mul
            if val in key and roman.startswith(key[val]):
                m += val
                roman = roman[len(key[val]):]
                if mul == 9 or mul == 4:  # 9 or 4 can't be followed by anything else
                    break
    return m == n
def sol209(n=2414):
    """Convert integer 0 < n < 4000 to roman numerals, and make it lowercase

    11 => "xi"
    """
    units = dict(m=1000, cm=900, d=500, cd=400, c=100, xc=90, l=50, xl=40, x=10, ix=9, v=5, iv=4, i=1)
    roman = ""
    for s, i in units.items():
        while n >= i:
            roman += s
            n -= i
    return roman
# assert sat209(sol209())

