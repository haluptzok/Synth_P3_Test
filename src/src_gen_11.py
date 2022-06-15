from typing import List

def sat110(direction: str, nums=[2, 4, 17, 29, 31, 1000, 416629]):
    if direction == "increasing":
        return all(nums[i] < nums[i + 1] for i in range(len(nums) - 1))
    if direction == "decreasing":
        return all(nums[i + 1] < nums[i] for i in range(len(nums) - 1))
def sol110(nums=[2, 4, 17, 29, 31, 1000, 416629]):
    """
    Determine the direction ('increasing' or 'decreasing') of monotonic sequence nums

    Sample Input:
    [1, 2, 5]

    Sample Output:
    "increasing"
    """
    return "increasing" if len(nums) > 1 and nums[1] > nums[0] else "decreasing"
# assert sat110(sol110())

def sat111(common: List[int], a=[2, 416629, 2, 4, 17, 29, 31, 1000], b=[31, 2, 4, 17, 29, 41205]):
    return all((i in common) == (i in a and i in b) for i in a + b + common)
def sol111(a=[2, 416629, 2, 4, 17, 29, 31, 1000], b=[31, 2, 4, 17, 29, 41205]):
    """
    Find numbers common to a and b

    Sample Input:
    [1, 2, 3], [3, 4, 5]

    Sample Output:
    [3]
    """
    return sorted(set(a).intersection(set(b)))
# assert sat111(sol111())

def sat112(p: int, n=101076):

    def is_prime(m):
        return all(m % i for i in range(2, m - 1))

    return is_prime(p) and n % p == 0 and p > 0 and all(n % i or not is_prime(i) for i in range(p + 1, n))
def sol112(n=101076):
    """
    Find the largest prime factor of n.

    Sample Input:
    125

    Sample Output:
    5
    """
    def is_prime(m):
        return all(m % i for i in range(2, m - 1))

    return next(n // i for i in range(1, n) if n % i == 0 and is_prime(n // i))
# assert sat112(sol112())

def sat113(sums: List[int], n=104):
    return all(sums[i + 1] - sums[i] == i for i in range(n)) and sums[0] == 0
def sol113(n=104):
    """
    Find the sums of the integers from 1 to n

    Sample Input:
    3

    Sample Output:
    [0, 1, 3, 6]
    """
    ans = [0]
    for i in range(n):
        ans.append(ans[-1] + i)
    return ans
# assert sat113(sol113())

def sat114(matches: List[int], parens="((())()(()()))(())"):
    for i, (j, c) in enumerate(zip(matches, parens)):
        assert parens[j] != c and matches[j] == i and all(i < matches[k] < j for k in range(i + 1, j))
    return len(matches) == len(parens)
def sol114(parens="((())()(()()))(())"):
    """
    Find the index of the matching parentheses for each character in the string

    Sample Input:
    "()((()))"

    Sample Output:
    [1, 0, 7, 6, 5, 4, 3, 2]
    """
    matches = [-1] * len(parens)
    opens = []
    for i, c in enumerate(parens):
        if c == "(":
            opens.append(i)
        else:
            assert c == ")"
            j = opens.pop()
            matches[i] = j
            matches[j] = i
    return matches
# assert sat114(sol114())

def sat115(derivative: List[int], poly=[2, 1, 0, 4, 19, 231, 0, 5]):

    def val(poly, x):
        return sum(coeff * (x ** i) for i, coeff in enumerate(poly))

    return all(abs(val(poly, x + 1e-8) - val(poly, x) - 1e-8 * val(derivative, x)) < 1e-4 for x in range(len(poly)))
def sol115(poly=[2, 1, 0, 4, 19, 231, 0, 5]):
    """
    Find the derivative of the given polynomial, with coefficients in order of increasing degree

    Sample Input:
    [3, 4, 1] # 3 + 4x + x^2

    Sample Output:
    [2, 4]   # 4 + 2x^2
    """
    return [i * poly[i] for i in range(1, len(poly))]
# assert sat115(sol115())

def sat116(init: List[int], target=124156):
    a, b, c = init
    for i in range(16):
        a, b, c = b, c, (a + b + c)
    return a == target
def sol116(target=124156):
    """
    Define a triple-Fibonacci sequence to be a sequence such that each number is the sum of the previous
    three. Given a target number, find an initial triple such that the 17th number in the sequence is the
    given target number.

    Sample Input:
    0

    Sample Output:
    [0, 0, 0]
    """
    nums = [target, 0, 0]
    for i in range(16):
        x = nums[-1] - sum(nums[:-1])  # x is such that x + nums[:3] == nums[3]
        nums = [x] + nums[:-1]
    return nums
# assert sat116(sol116())

def sat117(vowels: List[str], texts=['Hello, world!', 'Goodbye, world!']):
    for v, t in zip(vowels, texts):
        i = 0
        for j, c in enumerate(t):
            if c.lower() in "aeiou" or c.lower() == 'y' and j == len(t) - 1:
                assert v[i] == c
                i += 1
        assert i == len(v)
    return len(vowels) == len(texts)
def sol117(texts=['Hello, world!', 'Goodbye, world!']):
    """
    Find the vowels from each of the original texts (y counts as a vowel at the end of the word)

    Sample Input:
    ["You can do it!", "CAT"]

    Sample Output:
    ["ouaoi", "A"]
    """
    return ["".join(c for c in text if c.lower() in "aeiou") + (text[-1] if text[-1].lower() == "y" else "")
            for text in texts]
# assert sat117(sol117())

def sat118(shifted: str, n=124582369835, shift=3):
    if shift > len(str(n)):
        return n == int(shifted[::-1])
    return n == int(shifted[-shift:] + shifted[:-shift])
def sol118(n=124582369835, shift=3):
    """
    Shift the decimal digits n places to the left, wrapping the extra digits around. If shift > the number of
    digits of n, reverse the string.

    n=12345 shift=2 => '34512'
    """
    s = str(n)
    if shift > len(s):
        return s[::-1]
    return s[shift:] + s[:shift]
# assert sat118(sol118())

def sat119(tot: int, s="Add ME uP AND YOU WILL GET A BIG NUMBER!"):
    for c in s:
        if c.isupper():
            tot -= ord(c)
    return tot == 0
def sol119(s="Add ME uP AND YOU WILL GET A BIG NUMBER!"):
    """
    Compute the sum of the ASCII values of the upper-case characters in the string.

    Sample Input:
    ARt

    Sample Output:
    147 # = 65 + 82
    """
    return sum(ord(c) for c in s if c.isupper())
# assert sat119(sol119())

