from typing import List

def sat180(interval2: List[int], interval1=[32157, 93210127]):
    intersection_width = min(interval1[1], interval2[1]) - max(interval1[0], interval2[0])
    return intersection_width > 1 and all(intersection_width % i for i in range(2, intersection_width))
def sol180(interval1=[32157, 93210127]):
    """Find an interval whose intersection with a given interval has a width that is a prime integer.

    [7, 100] => [0, 10]  # because 10-7=3 is prime
    """
    a, b = interval1
    assert b - a >= 2
    return [a, a + 2]
assert sat180(sol180())

def sat181(n: int, arr=[1, 7, -20052, 14, -3, -11, 1025235, 14]):
    tot = 0

    for i in arr:
        if tot >= 0:
            tot += abs(i)
        else:
            tot -= abs(i)
        if i < 0:
            tot = -tot
        elif i == 0:
            tot = 0
            break

    return n == tot
def sol181(arr=[1, 7, -20052, 14, -3, -11, 1025235, 14]):
    """Find the sum of the magnitudes of the elements in the array with a sign that is equal to the product of
    the signs of the entries.

    [1, -2, 3] => -6  # negative because there is one negative
    """
    tot = sum(abs(i) for i in arr)
    if all(arr):
        return tot if sum(i < 0 for i in arr) % 2 == 0 else -tot
    return 0
assert sat181(sol181())

def sat182(path: List[int], k=10, edges=[[2, 4], [3], [4, 1], [4], [0]]):

    def check(prefix):
        for i, j in zip(path, prefix):
            if i != j:
                return i < j
        return len(prefix) >= k or all(check(prefix + [i]) for i in edges[prefix[-1]])

    return all(path[i] in edges[path[i - 1]] for i in range(1, k)) and all(check([i]) for i in range(len(edges)))
def sol182(k=10, edges=[[2, 4], [3], [4, 1], [4], [0]]):
    """Find the lexicographically smallest path of length k in graph with given edge matrix (and no dead ends)

    k=3, edges=[[1,3], [0, 3], [2], [3]] => [0, 1, 0] # because 0-1 and 1-0 are edges
    """
    path = []
    while len(path) < k:
        path.append(min(edges[path[-1]]) if path else 0)
    return path
assert sat182(sol182())

def sat183(seq: List[int], length=181):
    return all(seq[n] == (seq[n - 1] + seq[n - 2] + seq[n + 1] if n % 2 else 1 + n // 2) for n in range(length))
def sol183(length=181):
    """Find a sequence where seq[n] == 1 + n / 2 for even n, and
    seq[n] == seq[n - 1] + seq[n - 2] + seq[n + 1] for odd n < length."""
    seq = []
    while len(seq) <= length:
        n = len(seq)
        if n % 2 == 0:
            seq.append(1 + n // 2)
        else:
            seq.append(sum(seq[-2:]) + (1 + (n + 1) // 2))
    return seq + [0]  # appending 0 at the end makes it easier so that seq[n-2] == 0 for n == 1
assert sat183(sol183())

def sat184(prod: int, n=14235764939971075543215213):

    for c in str(n):
        i = int(c)
        if i % 2 == 1:
            assert prod % i == 0
            prod //= i
    return prod == any(int(c) % 2 for c in str(n))
def sol184(n=14235764939971075543215213):
    """Return the product of the odd digits in n, or 0 if there aren't any

    12345 => 15
    """
    if any(int(c) % 2 for c in str(n)):
        prod = 1
        for c in str(n):
            if int(c) % 2 == 1:
                prod *= int(c)
        return prod
    return 0
assert sat184(sol184())

def sat185(valid: str, s="]]]]]]]]]]]]]]]]][][][][]]]]]]]]]]][[[][[][[[[[][][][]][[[[[[[[[[[[[[[[[["):
    assert valid in s
    depths = [0]
    for c in valid:
        if c == "[":
            depths.append(depths[-1] + 1)
        elif c == "]":
            depths.append(depths[-1] - 1)
    return depths[-1] == 0 and min(depths) == 0 and max(depths) > 1
def sol185(s="]]]]]]]]]]]]]]]]][][][][]]]]]]]]]]][[[][[][[[[[][][][]][[[[[[[[[[[[[[[[[["):
    """Find a valid substring of s that contains matching brackets, at least one of which is nested

    "]][][[]]]" => "[][[]]"
    """
    left = []
    nested = False
    for i, c in enumerate(s):
        if c == "[":
            if len(left) == 2:
                left = [left[1], i]
                nested = False
            else:
                left.append(i)
        elif c == "]":
            if not left:
                continue
            if len(left) == 1 and nested:
                return s[left[0]:i + 1]
            elif len(left) == 2:
                nested = True
            left.pop()
    assert False
assert sat185(sol185())

def sat186(running_squares: List[int], x=[201.1, 301.4, -18.1, 1244122.0, 10101.0101, 10000000.0]):
    for i, v in enumerate(x):
        ceiling = int(v) + (v > 0 and not v.is_integer())
        square = ceiling ** 2
        if running_squares[i] != square + (i > 0 and running_squares[i - 1]):
            return False

    return len(running_squares) == len(x)
def sol186(x=[201.1, 301.4, -18.1, 1244122.0, 10101.0101, 10000000.0]):
    """Round each float in x up to the next integer and return the running total of the integer squares

    [2.4, 3.7, 0.1] => [9, 25, 26]
    """
    from math import ceil
    running_squares = []
    tot = 0
    for v in x:
        tot += ceil(v) ** 2
        running_squares.append(tot)
    return running_squares
assert sat186(sol186())

def sat187(y: List[bool], x=['Hello, world!', 'cat', '', 'a test', 'test a', 'i e', 'o', 'I O U', 'You and I']):
    assert len(x) == len(y)
    for s, b in zip(x, y):
        if len(s.split(" ")[-1]) == 1:
            assert b == s[-1].isalpha()
        else:
            assert not b
    return True
def sol187(x=['Hello, world!', 'cat', '', 'a test', 'test a', 'i e', 'o', 'I O U', 'You and I']):
    """Determine, for each string in x, whether the last character is an isolated letter

    ["a b c", "abc"] => [True, False]
    """
    return [len(s.split(" ")[-1]) == 1 and s[-1].isalpha() for s in x]
assert sat187(sol187())

def sat188(drop_indexes: List[int], nums=[2, -1, 14, 8, 9, 9, 8, 4, 2, 4, 3, -100, 1000, 18, 4, -2, -3, -3, 1, 0]):
    d = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            assert drop_indexes[d] == i
            d += 1
    return d == len(drop_indexes)
def sol188(nums=[2, -1, 14, 8, 9, 9, 8, 4, 2, 4, 3, -100, 1000, 18, 4, -2, -3, -3, 1, 0]):
    """Find the indices for which the nums array drops.

    [1,2,3,0,2,4,1] => [3,6]
    """
    return [i for i in range(1, len(nums)) if nums[i] < nums[i - 1]]
assert sat188(sol188())

def sat189(extremes: List[int], nums=[-10, -4, 100, -40, 2, 2, 3, 17, -50, -25, 18, 41, 9, 11, 15]):
    neg, pos = extremes
    if neg == 0:
        assert nums == [] or min(nums) >= 0
    else:
        assert neg < 0 and neg in nums and all(n >= 0 or n <= neg for n in nums)
    if pos == 0:
        assert nums == [] or max(nums) <= 0
    else:
        assert pos > 0 and pos in nums and all(n <= 0 or n >= pos for n in nums)
    return True
def sol189(nums=[-10, -4, 100, -40, 2, 2, 3, 17, -50, -25, 18, 41, 9, 11, 15]):
    """Find the largest negative ans smallest positive numbers (or 0 if none)

    [-2, -4, 14, 50] => [-2, 14]
    [3, 22] => [0, 3]
    """
    pos = [n for n in nums if n > 0]
    neg = [n for n in nums if n < 0]
    return [max(neg) if neg else 0, min(pos) if pos else 0]
assert sat189(sol189())

