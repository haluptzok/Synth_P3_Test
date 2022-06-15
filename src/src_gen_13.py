from typing import List

def sat130(x: int, n=42714774173606970182754018064350848294149432972747296768):
    return x ** 3 == n
def sol130(n=42714774173606970182754018064350848294149432972747296768):
    """Find an integer that when cubed is n

    Sample Input:
    21

    Sample Output:
    3
    """
    # Using Newton's method
    m = abs(n)
    x = round(abs(n) ** (1 / 3))
    while x ** 3 != m:
        x += (m - x ** 3) // (3 * x ** 2)
    return -x if n < 0 else x
# assert sat130(sol130())

def sat131(primes: List[bool], n="A4D4455214122CE192CCBE3"):
    return all(primes[i] == (c in "2357BD") for i, c in enumerate(n))
def sol131(n="A4D4455214122CE192CCBE3"):
    """Determine which characters of a hexidecimal correspond to prime numbers

    Sample Input:
    "123ABCD"

    Sample Output:
    [False, True, True, False, True, False True]
    """
    return [c in "2357BD" for c in n]
# assert sat131(sol131())

def sat132(b: str, n=5324680297138495285):
    assert b[:4] == b[-4:] == 'bits'
    inside = b[4:-4]
    assert all(c in "01" for c in inside)
    assert inside[0] == "1" or len(inside) == 1
    m = 0
    for c in inside:
        m = 2 * m + int(c)
    return m == n
def sol132(n=5324680297138495285):
    """Write n base 2 followed and preceded by 'bits'
    Sample Input:
    2

    Sample Output:
    bits10bits
    """
    s = bin(n)[2:]
    return f'bits{s}bits'
# assert sat132(sol132())

def sat133(indices: List[int], s="I am an unhappy string!"):
    i, j = indices
    return s[i] == s[j] and 0 <= i < j < i + 3
def sol133(s="I am an unhappy string!"):
    """A string is happy if every three consecutive characters are distinct. Find two indices making s unhappy.
    Sample Input:
    "street"

    Sample Output:
    [3, 4]
    """
    for i in range(len(s) - 2):
        if s[i] == s[i + 1]:
            return [i, i + 1]
        if s[i] == s[i + 2]:
            return [i, i + 2]
# assert sat133(sol133())

def sat134(grades: List[str], gpas=[2.8, 3.1, 4.0, 2.2, 3.1, 2.5, 0.9]):
    assert len(grades) == len(gpas)
    letters = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'F']
    scores = [4.0, 3.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]
    for grade, gpa in zip(grades, gpas):
        i = letters.index(grade)
        assert gpa >= scores[i]
        assert i == 0 or gpa <= scores[i - 1]
    return True
def sol134(gpas=[2.8, 3.1, 4.0, 2.2, 3.1, 2.5, 0.9]):
    """
    Convert GPAs to letter grades according to the following table:
    4.0: A+
    3.7: A
    3.4: A-
    3.0: B+
    2.7: B
    2.4: B-
    2.0: C+
    1.7: C
    1.4: C-
    below: F

    Sample input: [4.0, 3.5, 3.8]
    Sample output: ['A+', 'A-', 'A']
    """
    letters = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'F']
    scores = [4.0, 3.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]
    ans = []
    for gpa in gpas:
        i = 0
        while gpa < scores[i]:
            i += 1
        ans.append(letters[i])
    return ans
# assert sat134(sol134())

def sat135(factor: str, s="catscatcatscatcatscat"):
    return len(factor) < len(s) and s == factor * (len(s) // len(factor))
def sol135(s="catscatcatscatcatscat"):
    """Find a string which when repeated more than once gives s
    Sample Input:
    "haha"

    Sample Output:
    "ha"
    """
    n = len(s)
    return next(s[:i] for i in range(1, len(s)) if s == s[:i] * (n // i))
# assert sat135(sol135())

def sat136(nums: List[int], n=5):
    count = 18 * (10 ** (n - 2)) if n > 1 else 1
    strs = {str(n) for n in nums}
    return len(strs) == count and all(s.startswith("1") or s.endswith("1") and len(s) == n for s in strs)
def sol136(n=5):
    """Find all n-digit integers that start or end with 1

    1 => [1]"""
    ans = []
    for i in range(10 ** (n - 1), 10 ** n):
        assert len(str(i)) == n
        if str(i).startswith("1") or str(i).endswith("1"):
            ans.append(i)
    return ans
# assert sat136(sol136())

def sat137(n: int, b=107, s=25):
    n_str = bin(n)[2:]  # n in binary
    return len(n_str) == b and sum(int(i) for i in n_str) == s
def sol137(b=107, s=25):
    """Find an b-bit integer with a bit-sum of s

    b=3, s=2 => 5 # 5 is 101 in binary
    """
    return int("1" * s + "0" * (b - s), 2)
# assert sat137(sol137())

def sat138(even_odd_sum: int, nums=[2341, 125146894, 12521, -12451293476325, 535284623934, 132974693614350]):
    for i in nums[1::2]:
        if i % 2 == 0:
            even_odd_sum -= i
    return even_odd_sum == 0
def sol138(nums=[2341, 125146894, 12521, -12451293476325, 535284623934, 132974693614350]):
    """Find the sum of the even elements that are at odd indices

    [1, 2, 8, 3, 9, 4] => 6
    """
    return sum(i for i in nums[1::2] if i % 2 == 0)
# assert sat138(sol138())

def sat139(s: str, orig="Hello world!!!"):
    for a, b in zip(s.split(' '), orig.split(' ')):
        for i in range(len(a) - 1):
            assert a[i] <= a[i + 1], "characters must s-words be in increasing order"
        assert len(a) == len(b) and all(a.count(c) == b.count(c) for c in b), "must have same chars"
    return len(s) == len(orig)
def sol139(orig="Hello world!!!"):
    """Create a new string by taking s, and word by word rearranging its characters in ascii order
    Sample input:
    'maltos wow'

    Sample output:
    'almost oww'
    """
    return " ".join("".join(sorted(w)) for w in orig.split(' '))
# assert sat139(sol139())

