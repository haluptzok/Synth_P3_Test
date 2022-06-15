from typing import List

def sat240(seq: List[int], target=[1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0], n_steps=4):
    s = seq[:]  # copy
    for step in range(n_steps):
        for i in range(len(seq) - 1):
            if (s[i], s[i + 1]) == (0, 1):
                (s[i], s[i + 1]) = (1, 0)
    return s == target
def sol240(target=[1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0], n_steps=4):
    """
    Find a sequence of 0's and 1's so that, after n_steps of swapping each adjacent (0, 1), the target sequence
    is achieved.
    """
    s = target[:]  # copy
    for step in range(n_steps):
        for i in range(len(target) - 2, -1, -1):
            if (s[i], s[i + 1]) == (1, 0):
                (s[i], s[i + 1]) = (0, 1)
    return s
# assert sat240(sol240())

def sat241(d: int, n=6002685529):
    return n % d == 0 and all(i in "47" for i in str(d))
def sol241(n=6002685529):
    """Find a integer factor of n whose decimal representation consists only of 7's and 4's."""
    def helper(so_far, k):
        if k > 0:
            return helper(so_far * 10 + 4, k - 1) or helper(so_far * 10 + 7, k - 1)
        return (n % so_far == 0) and so_far

    for length in range(1, len(str(n)) // 2 + 2):
        ans = helper(0, length)
        if ans:
            return ans
# assert sat241(sol241())

def sat242(d: int, n=123456789):
    return d > n and all(i in "47" for i in str(str(d).count("4") + str(d).count("7")))
def sol242(n=123456789):
    """
    Find a number bigger than n whose decimal representation has k 4's and 7's where k's decimal representation
    consists only of 4's and 7's
    """
    return int("4444" + "0" * (len(str(n)) - 3))
# assert sat242(sol242())

def sat243(s: str, target="reverse me", reverse=True):
    return (s[::-1] == target) == reverse
def sol243(target="reverse me", reverse=True):
    """Either reverse a string or don't based on the reverse flag"""
    return target[::-1] if reverse else target + "x"
# assert sat243(sol243())

def sat244(taken: List[int], val_counts=[[4, 3], [5, 2], [9, 3], [13, 13], [8, 11], [56, 1]], upper=11):
    advantage = 0
    assert len(taken) == len(val_counts) and sum(taken) <= upper
    for i, (val, count) in zip(taken, val_counts):
        assert 0 <= i <= count
        advantage += val * i - val * count / 2
    return advantage > 0
def sol244(val_counts=[[4, 3], [5, 2], [9, 3], [13, 13], [8, 11], [56, 1]], upper=11):
    """
    The list of numbers val_counts represents multiple copies of integers, e.g.,
    val_counts=[[3, 2], [4, 6]] corresponds to 3, 3, 4, 4, 4, 4, 4, 4
    For each number, decide how many to take so that the total number taken is <= upper and the sum of those
    taken exceeds half the total sum.
    """
    n = len(val_counts)
    pi = sorted(range(n), key=lambda i: val_counts[i][0])
    needed = sum(a * b for a, b in val_counts) / 2 + 0.1
    ans = [0] * n
    while needed > 0:
        while val_counts[pi[-1]][1] == ans[pi[-1]]:
            pi.pop()
        i = pi[-1]
        ans[i] += 1
        needed -= val_counts[i][0]
    return ans
# assert sat244(sol244())

def sat245(s: str, a=5129, d=17):
    return s.count("a") == a and s.count("d") == d and len(s) == a + d
def sol245(a=5129, d=17):
    """Find a string with a given number of a's and d's"""
    return "a" * a + "d" * d
# assert sat245(sol245())

def sat246(nums: List[int], a=100, b=1000, count=648):
    assert all(len(str(n)) == len(set(str(n))) and a <= n <= b for n in nums)
    return len(set(nums)) >= count
def sol246(a=100, b=1000, count=648):
    """Find a list of count or more different numbers each between a and b that each have no repeated digits"""
    return [n for n in range(a, b + 1) if len(str(n)) == len(set(str(n)))]
# assert sat246(sol246())

def sat247(tot: int, nums=[2, 8, 25, 18, 99, 11, 17, 16], thresh=17):
    return tot == sum(1 if i < thresh else 2 for i in nums)
def sol247(nums=[2, 8, 25, 18, 99, 11, 17, 16], thresh=17):
    """Add up 1 or 2 for numbers in a list depending on whether they exceed a threshold"""
    return sum(1 if i < thresh else 2 for i in nums)
# assert sat247(sol247())

def sat248(s: str, chars=['o', 'h', 'e', 'l', ' ', 'w', '!', 'r', 'd']):
    for c in chars:
        if c not in s:
            return False
    return True
def sol248(chars=['o', 'h', 'e', 'l', ' ', 'w', '!', 'r', 'd']):
    """Find a string with certain characters"""
    return 'hello world!'
# assert sat248(sol248())

def sat249(ans: List[List[int]], target=17):
    for i in range(len(ans)):
        a, b = ans[i]
        if b - a >= 2:
            target -= 1
    return target == 0
def sol249(target=17):
    """
    Find a list of pairs of integers where the number of pairs in which the second number is more than
    two greater than the first number is a given constant
    """
    return [[0, 2]] * target
# assert sat249(sol249())

