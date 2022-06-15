from typing import List

def sat80(ans: str, s="FlIp ME!"):
    return len(ans) == len(s) and all({c, d} == {d.upper(), d.lower()} for c, d in zip(ans, s))
def sol80(s="FlIp ME!"):
    """
    Flip case

    Sample input
    ---
    'cAt'

    Sample output
    ---
    'CaT'
    """
    return "".join(c.lower() if c.upper() == c else c.upper() for c in s)
# assert sat80(sol80())

def sat81(cat: str, strings=['Will', 'i', 'am', 'Now', 'here']):
    i = 0
    for s in strings:
        for c in s:
            assert cat[i] == c
            i += 1
    return i == len(cat)
def sol81(strings=['Will', 'i', 'am', 'Now', 'here']):
    """
    Concatenate a list of strings

    Sample input
    ---
    ['cat', 'dog', 'bird']

    Sample output
    ---
    'catdogbird'
    """
    return "".join(strings)
# assert sat81(sol81())

def sat82(extensions: List[str], strings=['cat', 'dog', 'shatter', 'donut', 'at', 'todo'], prefix="do"):
    i = 0
    for s in strings:
        if s.startswith(prefix):
            assert extensions[i] == s
            i += 1
    return i == len(extensions)
def sol82(strings=['cat', 'dog', 'shatter', 'donut', 'at', 'todo'], prefix="do"):
    """
    Find the strings in a list starting with a given prefix

    Sample Input:
    ['cat', 'car', 'fear', 'center'], 'ca'

    Sample Output:
    ['cat', 'car']
    """
    return [s for s in strings if s.startswith(prefix)]
# assert sat82(sol82())

def sat83(positives: List[int], nums=[2, 2342, -2, 32, -8, -5, 2342, 0, -9, 44, 11]):
    stack = positives[::-1]
    for n in nums:
        assert n <= 0 or n == stack.pop()
    return stack == []
def sol83(nums=[2, 2342, -2, 32, -8, -5, 2342, 0, -9, 44, 11]):
    """
    Find the positive integers in a list

    Sample Input:
    [-1, 3, 19, -2, 0, 44, 0, 44, 11]

    Sample Output:
    [3, 19, 44, 44, 11]
    """
    return [i for i in nums if i > 0]
# assert sat83(sol83())

def sat84(certificates: List[int], nums=[1449, 14, 21, 105, 217]):
    return all(pow(cert, n - 1, n) > 1 for cert, n in zip(certificates, nums)) and len(certificates) == len(nums)
def sol84(nums=[1449, 14, 21, 105, 217]):
    """
    Find Fermat composite certificates for a list of numbers > 1

    Sample Input:
    [1469]

    Sample Output:
    [3]  # because (3 ** 1468) % 1469 != 1
    """
    return [next(i for i in range(2, n) if pow(i, n - 1, n) > 1) for n in nums]
# assert sat84(sol84())

def sat85(root: float, coeffs=[1, 2, 3, 17]):
    return abs(sum(coeff * (root ** i) for i, coeff in enumerate(coeffs))) < 1e-4
def sol85(coeffs=[1, 2, 3, 17]):
    """
    Find a real root of an odd degree polynomial from its coefficients

    Sample Input:
    [1, 0, 8]

    Sample Output:
    -2.0  # 1*(-2.0)^3 + 8 == 0
    """
    def p(x):
        return sum(coeff * (x ** i) for i, coeff in enumerate(coeffs))

    for attempt in range(100):
        a, b = -(10 ** attempt), (10 ** attempt)
        p_a, p_b = p(a), p(b)
        while p_a * p_b <= 0:
            mid = (a + b) / 2
            p_mid = p(mid)
            if abs(p_mid) < 1e-4:
                return mid
            assert mid not in [a, b]
            if p_mid * p_a > 0:
                a, p_a = mid, p_mid
            else:
                b, p_b = mid, p_mid

    assert False, "Root finder failed on 100 attempts"
# assert sat85(sol85())

def sat86(li: List[int], orig=[1, -2, 3, 17, 8, 4, 12, 3, 18, 5, -29, 0, 0]):
    assert orig[::3] == li[::3], "Keep every third entry fixed"
    assert sorted(li) == sorted(orig), "Not even a permutation"
    assert all(li[i] <= li[i + 1] for i in range(1, len(li) - 1, 3))
    assert all(li[i] <= li[i + 2] for i in range(2, len(li) - 2, 3))
    return True
def sol86(orig=[1, -2, 3, 17, 8, 4, 12, 3, 18, 5, -29, 0, 0]):
    """
    Start with a list of integers, keep every third element in place and otherwise sort the list

    Sample Input:
    [8, 0, 7, 2, 9, 4, 1, 2, 8, 3]

    Sample Output:
    [8, 0, 2, 2, 4, 8, 1, 8, 9, 3]
    """
    n = len(orig)
    your_list = orig[::3]
    sub = orig[:]
    for i in range(int((len(sub) + 2) / 3)):
        sub.pop((2 * i))
    sub = sorted(sub)
    answ = []
    for i in range(int(n / 3)):
        answ.append(your_list[i])
        answ.append(sub[i * 2])
        answ.append(sub[i * 2 + 1])
    if n % 3 == 1:
        answ.append(your_list[-1])
    if n % 3 == 2:
        answ.append(your_list[-1])
        answ.append(sub[-1])
    return answ
# assert sat86(sol86())

def sat87(li: List[int], orig=[1, 1, 3, 2, 0, 8, 32, -4, 0]):
    for i in range(len(li) - 1):
        assert li[i] < li[i + 1]
        assert li[i] in orig
    for n in orig:
        assert n in li
    return True
def sol87(orig=[1, 1, 3, 2, 0, 8, 32, -4, 0]):
    """
    Find an increasing sequence consisting of the elements of the original list.

    Sample Input:
    [8, 0, 7, 2, 9, 4, 4, -2, 8, 3]

    Sample Output:
    [-2, 0, 2, 3, 4, 7, 8, 9]
    """
    my_list = sorted(set(orig))
    return my_list
# assert sat87(sol87())

def sat88(m: int, hello=[1, 31, 3, 2, 0, 18, 32, -4, 2, -1000, 3502145, 3502145, 21, 18, 2, 60]):
    return m in hello and not any(m < i for i in hello)
def sol88(hello=[1, 31, 3, 2, 0, 18, 32, -4, 2, -1000, 3502145, 3502145, 21, 18, 2, 60]):
    """
    Find the largest integer in a sequence

    Sample Input:
    [8, 0, 1, 4, 9, 3, 4, -2, 8, 3]

    Sample Output:
    9
    """
    return max(hello)
# assert sat88(sol88())

def sat89(li: List[List[int]], n=19723, lower=1000):
    assert len({(i, j) for i, j in li}) >= lower, "not enough 7's (ignoring duplicates)"
    return all(str(i)[j] == '7' and (i % 11 == 0 or i % 13 == 0) and 0 <= i < n and 0 <= j for i, j in li)
def sol89(n=19723, lower=1000):
    """
    Find all 7's in integers less than n that are divisible by 11 or 13

    Sample Input:
    79, 3

    Sample Output:
    [[77, 0], [77, 1], [78, 0]]
    """
    return [[i, j] for i in range(n) if (i % 11 == 0 or i % 13 == 0) for j, c in enumerate(str(i)) if c == '7']
# assert sat89(sol89())

