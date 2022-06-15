from typing import List

def sat100(x: int, nums=[132666041, 237412, 28141, -12, 11939, 912414, 17], upper=133658965):
    dev = sum(n - x for n in nums)
    return dev <= upper
def sol100(nums=[132666041, 237412, 28141, -12, 11939, 912414, 17], upper=133658965):
    """
    Find an integer that minimizes the sum of absolute deviations with respect to the given numbers.

    Sample Input:
    [3, 6, 1, 2, 5, 4, 100], upper=105

    Sample Output:
    4
    """
    return sorted(nums)[len(nums) // 2] if nums else 0
# assert sat100(sol100())

def sat101(pals: List[bool], strs=['palindrome', 'madamimadam', '', 'foo', 'eyes', '(-:-)']):
    return all(pals[i] == (s == s[::-1]) for i, s in enumerate(strs))
def sol101(strs=['palindrome', 'madamimadam', '', 'foo', 'eyes', '(-:-)']):
    """
    Test whether the given strings are palindromes

    Sample Input:
    ["aba", "no"]

    Sample Output:
    [True, False]
    """
    return [s == s[::-1] for s in strs]
# assert sat101(sol101())

def sat102(exp_poly: List[int], d=74152093423, poly=[1, 6, 3, 1, 0, 4, 4]):
    p = len(poly)
    assert p > 2 and all(p % i for i in range(2, p)), "Hint: p is a prime > 2"

    def val(coeffs, n):  # evaluate polynomial mod p
        return sum(c * pow(n, i, p) for i, c in enumerate(coeffs)) % p

    return all(val(exp_poly, n) == pow(val(poly, n), d, p) for n in range(p))
def sol102(d=74152093423, poly=[1, 6, 3, 1, 0, 4, 4]):
    """
    Fermat's little theorem implies that any polynomial can be written equivalently as a degree p-1
    polynomial (mod p).
    Given the p coefficients of a polynomial poly, compute a polynomial equivalent to poly^d (mod p).

    Sample Input:
    d=2, poly=[1, 0, 0, 1, 0]  # 1 + x^3

    Sample Output:
    [1, 0, 1, 2, 0]  # 1+ x^2 + 2x^3 because (1 + x^3)^2 = 1 + 2x^3 + x^6 and x^6 = x^2 (mod 5)
    """
    """
    Use repeated squaring to exponentiate polynomial
    """
    p = len(poly)

    def prod(poly1, poly2):  # multiply two polynomials mod p
        ans = [0] * p
        for i, a in enumerate(poly1):
            for j, b in enumerate(poly2):
                e = (i + j) % (p - 1)
                if e == 0 and i + j > 1:
                    e = p - 1
                ans[e] = (ans[e] + a * b) % p
        return ans

    ans = [1] + [0] * (p - 1)
    while d:
        if d % 2:
            ans = prod(ans, poly)
        poly = prod(poly, poly)
        d //= 2
    # for i in range(d):
    #     ans = prod(ans, poly)
    return ans
# assert sat102(sol102())

def sat103(orig: str, result="Hello, world!", shift=7):
    n = len(result)
    assert len(orig) == n
    return all(ord(orig[i]) + shift == ord(result[i]) for i in range(n))
def sol103(result="Hello, world!", shift=7):
    """
    Find a string which, when each character is shifted (ascii incremented) by shift, gives the result.

    Sample Input:
    result='very good', shift=-1

    Sample Output:
    'wfsz!hppe'
    """
    return "".join(chr(ord(c) - shift) for c in result)
# assert sat103(sol103())

def sat104(txt: str, text="Hello, world!"):
    n = 0
    for c in text:
        if c.lower() not in "aeiou":
            assert txt[n] == c
            n += 1
    assert n == len(txt)
    return True
def sol104(text="Hello, world!"):
    """
    Remove the vowels from the original string.

    Sample Input:
    "very good"

    Sample Output:
    'vry gd'
    """
    return "".join(c for c in text if c.lower() not in "aeiou")
# assert sat104(sol104())

def sat105(indexes: List[int], nums=[0, 2, 17, 4, 4213, 322, 102, 29, 15, 39, 55], thresh=100):
    j = 0
    for i, n in enumerate(nums):
        if n < thresh:
            assert indexes[j] == i
            j += 1
    assert j == len(indexes)
    return True
def sol105(nums=[0, 2, 17, 4, 4213, 322, 102, 29, 15, 39, 55], thresh=100):
    """
    Find the indexes of numbers below a given threshold

    Sample Input:
    nums=[4, 7, 11, 5], threshold=10

    Sample Output:
    [0, 1, 3]
    """
    return [i for i, n in enumerate(nums) if n < thresh]
# assert sat105(sol105())

def sat106(n: int, nums=[10, 42, 17, 9, 1315182, 184, 102, 29, 15, 39, 755]):
    return sum(nums + [-n]) == 0
def sol106(nums=[10, 42, 17, 9, 1315182, 184, 102, 29, 15, 39, 755]):
    """
    Find the number which when appended to the list makes the total 0

    Sample Input:
    [1, 2, 3]

    Sample Output:
    -6
    """
    return sum(nums)
# assert sat106(sol106())

def sat107(c: str, a="the quick brown fox jumped over the lazy dog", b="how vexingly quick daft zebras jump"):
    return (c in a) != (c in b)
def sol107(a="the quick brown fox jumped over the lazy dog", b="how vexingly quick daft zebras jump"):
    """
    Find a character in one string that is not in the other.

    Sample Input:
    'Do you like green eggs and ham?', 'I do not like green eggs and ham.'

    Sample Output:
    't'  # or .?yI
    """
    return sorted(set(a).symmetric_difference(b))[0]
# assert sat107(sol107())

def sat108(nums: List[int], n=1402):
    return nums[0] == nums[1] == 1 and all(nums[i + 2] == nums[i + 1] + nums[i] for i in range(n - 2))
def sol108(n=1402):
    """
    Find the first n Fibonacci numbers

    Sample Input:
    4

    Sample Output:
    [1, 1, 2, 3]
    """
    ans = [1, 1]
    while len(ans) < n:
        ans.append(ans[-1] + ans[-2])
    return ans
# assert sat108(sol108())

def sat109(matches: List[int], brackets="<<>><<<><>><<>>>"):
    for i in range(len(brackets)):
        j = matches[i]
        c = brackets[i]
        assert brackets[j] != c and matches[j] == i and all(i < matches[k] < j for k in range(i + 1, j))
    return len(matches) == len(brackets)
def sol109(brackets="<<>><<<><>><<>>>"):
    """
    Find the index of the matching brackets for each character in the string

    Sample Input:
    "<><>"

    Sample Output:
    [1, 0, 3, 2]
    """
    matches = [-1] * len(brackets)
    opens = []
    for i, c in enumerate(brackets):
        if c == "<":
            opens.append(i)
        else:
            assert c == ">"
            j = opens.pop()
            matches[i] = j
            matches[j] = i
    return matches
# assert sat109(sol109())

