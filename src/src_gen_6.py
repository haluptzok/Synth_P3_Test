from typing import List

def sat60(containers: List[str], strings=['cat', 'dog', 'shatter', 'bear', 'at', 'ta'], substring="at"):
    i = 0
    for s in strings:
        if substring in s:
            assert containers[i] == s
            i += 1
    return i == len(containers)
def sol60(strings=['cat', 'dog', 'shatter', 'bear', 'at', 'ta'], substring="at"):
    """
    Find the strings in a list containing a given substring

    Sample Input:
    ['cat', 'dog', 'bear'], 'a'

    Sample Output:
    ['cat', 'bear']
    """
    return [s for s in strings if substring in s]
# assert sat60(sol60())

def sat61(nums: List[int], tot=14, prod=99):
    assert sum(nums) == tot
    p = 1
    for n in nums:
        p *= n
    return p == prod
def sol61(tot=14, prod=99):
    """
    Find a list of numbers with a given sum and a given product.

    Sample Input:
    12, 32

    Sample Output:
    [2, 8, 2]
    """
    ans = [prod]
    while sum(ans) > tot:
        ans += [-1, -1]
    ans += [1] * (tot - sum(ans))
    return ans
# assert sat61(sol61())

def sat62(maxes: List[int], nums=[1, 4, 3, -6, 19]):
    assert len(maxes) == len(nums)
    for i in range(len(nums)):
        if i > 0:
            assert maxes[i] == max(maxes[i - 1], nums[i])
        else:
            assert maxes[0] == nums[0]
    return True
def sol62(nums=[1, 4, 3, -6, 19]):
    """
    Find a list whose ith element is the maximum of the first i elements of the input list.

    Sample Input:
    [2, 8, 2]

    Sample Output:
    [2, 8, 8]
    """
    return [max(nums[:i]) for i in range(1, len(nums) + 1)]
# assert sat62(sol62())

def sat63(ans: str, s="so easy", length=20):
    return ans == ans[::-1] and len(ans) == length and s in ans
def sol63(s="so easy", length=20):
    """
    Find a palindrome of a given length containing a given string.

    Sample Input:
    "abba", 6

    Sample Output:
    "cabbac"
    """
    ls = list(s)
    for i in range(length - len(s) + 1):
        arr = ['x'] * length
        arr[i:i + len(s)] = ls
        a = length - i - 1
        b = length - (i + len(s)) - 1
        if b == -1:
            b = None
        arr[a:b:-1] = ls
        if arr == arr[::-1]:
            ans = "".join(arr)
            if s in ans:
                return ans
    assert False, "shouldn't reach here"
# assert sat63(sol63())

def sat64(str_num: str, nums=['100011101100001', '100101100101110']):
    a, b = nums
    return int(str_num, 2) == int(a, 2) ^ int(b, 2)
def sol64(nums=['100011101100001', '100101100101110']):
    """
    Find a the XOR of two given strings interpreted as binary numbers.

    Sample Input:
    "0001", "1011"

    Sample Output:
    "1010"
    """
    a, b = nums
    ans = int(a, 2) ^ int(b, 2)
    return format(ans, "b")
# assert sat64(sol64())

def sat65(ans: str, words=['these', 'are', 'some', 'pretty', 'long', 'words']):
    return ans in words and all(len(ans) >= len(w) for w in words)
def sol65(words=['these', 'are', 'some', 'pretty', 'long', 'words']):
    """
    Find the longest of a list of strings

    Sample Input:
    ["cat", "dog", "sheep", "chimp"]

    Sample Output:
    "sheep"
    """
    return max(words, key=len)
# assert sat65(sol65())

def sat66(ans: List[int], m=200004931, n=66679984):
    gcd, a, b = ans
    return m % gcd == n % gcd == 0 and a * m + b * n == gcd and gcd > 0
def sol66(m=200004931, n=66679984):
    """
    Find the greatest common divisor of two integers m, n and a certificate a, b such that m*a + n*b = gcd

    Sample Input:
    20, 30

    Sample Output:
    10, -1, 1
    """
    """
    Derivation of solution below
    Recursive solution guarantees a * (big % small) + b * small == gcd
    Let d = big // small so (big % small) == big - small * d
    gives a * (big - small * d) + b * small == gcd
    or equivalently (b - a * d) * small + a * big == gcd
    """

    def gcd_cert(small, big):
        """Returns gcd, a, b, such that small * a + big * b == gcd"""
        assert 0 < small <= big
        if big % small == 0:
            return [small, 1, 0]
        gcd, a, b = gcd_cert(big % small, small)
        return [gcd, b - a * (big // small), a]

    if m < n:
        return gcd_cert(m, n)
    gcd, a, b = gcd_cert(n, m)
    return [gcd, b, a]
# assert sat66(sol66())

def sat67(prefixes: List[str], s="donesezichethofalij"):
    return all(s.startswith(p) for p in prefixes) and len(set(prefixes)) > len(s)
def sol67(s="donesezichethofalij"):
    """
    Find all prefixes of a given string

    Sample Input:
    "aabcd"

    Sample Output:
    ["", "a", "aa", "aab", "aabc", "aabcd"]
    """
    return [s[:i] for i in range(len(s) + 1)]
# assert sat67(sol67())

def sat68(ans: str, n=15):
    return [int(i) for i in ans.split(' ')] == list(range(n + 1))
def sol68(n=15):
    """
    Find a string consisting of the non-negative integers up to n inclusive

    Sample Input:
    4

    Sample Output:
    '0 1 2 3 4'
    """
    return ' '.join(str(i) for i in range(n + 1))
# assert sat68(sol68())

def sat69(ans: List[str], s="The quick brown fox jumps over the lazy dog!", n=28):
    assert all(ans.count(c.lower()) == 1 for c in s)
    assert all(c == c.lower() for c in ans)
    assert all(c in s.lower() for c in ans)
    return True
def sol69(s="The quick brown fox jumps over the lazy dog!", n=28):
    """
    Find the set of distinct characters in a string, ignoring case

    Sample Input:
    'HELlo', 4

    Sample Output:
    ['h', 'e', 'l', 'o']
    """
    return list(set(s.lower()))
# assert sat69(sol69())

