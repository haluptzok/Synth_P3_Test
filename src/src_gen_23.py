from typing import List

def sat230(n: int, s="0000101111111000010", k=5):
    return s[n:n + k] == s[n] * k
def sol230(s="0000101111111000010", k=5):
    """
    You are given a string consisting of 0's and 1's. Find an index after which the subsequent k characters are
    all 0's or all 1's.

    Sample Input:
    s = 0000111111100000, k = 5

    Sample Output:
    4
    (or 5 or 6 or 11)
    """
    return s.index("0" * k if "0" * k in s else "1" * k)
# assert sat230(sol230())

def sat231(delta: List[int], nums=[[1, 2, 3], [9, -2, 8], [17, 2, 50]]):
    return all(sum(vec[i] for vec in nums) + delta[i] == 0 for i in range(3))
def sol231(nums=[[1, 2, 3], [9, -2, 8], [17, 2, 50]]):
    """Find the missing triple of integers to make them all add up to 0 coordinatewise"""
    return [-sum(vec[i] for vec in nums) for i in range(3)]
# assert sat231(sol231())

def sat232(n: int, a=17, b=100, c=20):
    return n + a == sum([b * i for i in range(c)])
def sol232(a=17, b=100, c=20):
    """Find n such that n + a == b * (the sum of the first c integers)"""
    return -a + sum([b * i for i in range(c)])
# assert sat232(sol232())

def sat233(n: int, v=17, w=100):
    for i in range(n):
        assert v <= w
        v *= 3
        w *= 2
    return v > w
def sol233(v=17, w=100):
    """Find the smallest n such that if v is tripled n times and w is doubled n times, v exceeds w."""
    i = 0
    while v <= w:
        v *= 3
        w *= 2
        i += 1
    return i
# assert sat233(sol233())

def sat234(res: int, m=1234578987654321, n=4):
    for i in range(n):
        m = (m - 1 if m % 10 else m // 10)
    return res == m
def sol234(m=1234578987654321, n=4):
    """
    Find the result of applying the following operation to integer m, n times: if the last digit is zero, remove
    the zero, otherwise subtract 1.
    """
    for i in range(n):
        m = (m - 1 if m % 10 else m // 10)
    return m
# assert sat234(sol234())

def sat235(li: List[int], n=149432, upper=14943):
    return len(li) <= upper and all(abs(a - b) <= 10 for a, b in zip([1] + li, li + [n]))
def sol235(n=149432, upper=14943):
    """
    Find a the shortest sequence of integers going from 1 to n where each difference is at most 10.
    Do not include 1 or n in the sequence.
    """
    m = 1
    ans = []
    while True:
        m = min(n, m + 10)
        if m >= n:
            return ans
        ans.append(m)
# assert sat235(sol235())

def sat236(n: int, pairs=[[3, 0], [17, 1], [9254359, 19], [123, 9254359], [0, 123]]):
    assert sum(p - m for p, m in pairs) == 0, "oo"
    tot = 0
    success = False
    for p, m in pairs:
        tot -= m
        tot += p
        assert tot <= n
        if tot == n:
            success = True
    return success
def sol236(pairs=[[3, 0], [17, 1], [9254359, 19], [123, 9254359], [0, 123]]):
    """
    Given a sequence of integer pairs, p_i, m_i, where sum p_i-m_i = 0, find the maximum value, over t, of
    p_{t+1} + sum_{i=1}^t p_i - m_i
    """
    tot = 0
    n = 0
    for p, m in pairs:
        tot += p - m
        if tot > n:
            n = tot
    return n
# assert sat236(sol236())

def sat237(s_case: str, s="CanYouTellIfItHASmoreCAPITALS"):
    caps = 0
    for c in s:
        if c != c.lower():
            caps += 1
    return s_case == (s.upper() if caps > len(s) // 2 else s.lower())
def sol237(s="CanYouTellIfItHASmoreCAPITALS"):
    """
    Given a word, replace it either with an upper-case or lower-case depending on whether or not it has more
    capitals or lower-case letters. If it has strictly more capitals, use upper-case, otherwise, use lower-case.
    """
    caps = 0
    for c in s:
        if c != c.lower():
            caps += 1
    return (s.upper() if caps > len(s) // 2 else s.lower())  # duh, just take sat and return the answer checked for
# assert sat237(sol237())

def sat238(inds: List[int], string="Sssuubbstrissiingg"):
    return inds == sorted(inds) and "".join(string[i] for i in inds) == "substring"
def sol238(string="Sssuubbstrissiingg"):
    """Find increasing indices to make the substring "substring"""
    target = "substring"
    j = 0
    ans = []
    for i in range(len(string)):
        while string[i] == target[j]:
            ans.append(i)
            j += 1
            if j == len(target):
                return ans
# assert sat238(sol238())

def sat239(inds: List[int], string="enlightenment"):
    return inds == sorted(inds) and "".join(string[i] for i in inds) == "intelligent"
def sol239(string="enlightenment"):
    """Find increasing indices to make the substring "intelligent" (with a surprise twist)"""
    target = "intelligent"
    j = 0
    ans = []
    for i in range(-len(string), len(string)):
        while string[i] == target[j]:
            ans.append(i)
            j += 1
            if j == len(target):
                return ans
# assert sat239(sol239())

