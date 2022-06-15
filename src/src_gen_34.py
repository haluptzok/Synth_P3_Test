from typing import List

def sat340(n: int, year_len=365):
    prob = 1.0
    for i in range(n):
        prob *= (year_len - i) / year_len
    return (prob - 0.5) ** 2 <= 1/year_len
def sol340(year_len=365):
    """Find n such that the probability of two people having the same birthday in a group of n is near 1/2."""
    n = 1
    distinct_prob = 1.0
    best = (0.5, 1)  # (difference between probability and 1/2, n)
    while distinct_prob > 0.5:
        distinct_prob *= (year_len - n) / year_len
        n += 1
        best = min(best, (abs(0.5 - distinct_prob), n))

    return best[1]
# assert sat340(sol340())

def sat341(n: int, year_len=365):
    import random
    random.seed(0)
    K = 1000  # number of samples
    prob = sum(len({random.randrange(year_len) for i in range(n)}) < n for j in range(K)) / K
    return (prob - 0.5) ** 2 <= year_len
def sol341(year_len=365):
    """Find n such that the probability of two people having the same birthday in a group of n is near 1/2."""
    n = 1
    distinct_prob = 1.0
    best = (0.5, 1)  # (difference between probability and 1/2, n)
    while distinct_prob > 0.5:
        distinct_prob *= (year_len - n) / year_len
        n += 1
        best = min(best, (abs(0.5 - distinct_prob), n))

    return best[1]
# assert sat341(sol341())

def sat342(counts: List[int], target_prob=0.5):
    m, n = counts  # m = num 1's, n = num -1's
    probs = [1.0] + [0.0] * n  # probs[n] is probability for current m, starting with m = 1
    for i in range(2, m + 1):  # compute probs using dynamic programming for m = i
        old_probs = probs
        probs = [1.0] + [0.0] * n
        for j in range(1, min(n + 1, i)):
            probs[j] = (
                    j / (i + j) * probs[j - 1]  # last element is a -1 so use probs
                    +
                    i / (i + j) * old_probs[j]  # last element is a 1 so use old_probs, m = i - 1
            )
    return abs(probs[n] - target_prob) < 1e-6
def sol342(target_prob=0.5):
    """
    Suppose a list of m 1's and n -1's are permuted at random.
    What is the probability that all of the cumulative sums are positive?
    The goal is to find counts = [m, n] that make the probability of the ballot problem close to target_prob.
    """
    for m in range(1, 10000):
        n = round(m * (1 - target_prob) / (1 + target_prob))
        if abs(target_prob - (m - n) / (m + n)) < 1e-6:
            return [m, n]
# assert sat342(sol342())

def sat343(counts: List[int], p=0.5, target_prob=0.0625):
    from itertools import product
    a, b = counts
    n = a + b
    prob = (p ** a) * ((1-p) ** b)
    tot = sum([prob for sample in product([0, 1], repeat=n) if sum(sample) == a])
    return abs(tot - target_prob) < 1e-6
def sol343(p=0.5, target_prob=0.0625):
    """Find counts = [a, b] so that the probability of  a H's and b T's among a + b coin flips is ~ target_prob."""
    probs = [1.0]
    q = 1 - p
    while len(probs) < 20:
        probs = [(p * a + q * b) for a, b in zip([0] + probs, probs + [0])]
        answers = [i for i, p in enumerate(probs) if abs(p - target_prob) < 1e-6]
        if answers:
            return [answers[0], len(probs) - 1 - answers[0]]
# assert sat343(sol343())

def sat344(p_stop: float, steps=10, target_prob=0.5):
    prob = sum(p_stop*(1-p_stop)**t for t in range(steps))
    return abs(prob - target_prob) < 1e-6
def sol344(steps=10, target_prob=0.5):
    """
    Find p_stop so that the probability of stopping in steps or fewer time steps is the given target_prob if you
    stop each step with probability p_stop
    """
    return 1 - (1 - target_prob) ** (1.0/steps)
# assert sat344(sol344())

def sat345(s: str):
    return s[::-1] + 'world' == 'Hello world'
def sol345():
    """Find a string that when reversed and concatenated onto 'world' gives 'Hello world'."""
    return ' olleH'
# assert sat345(sol345())

def sat346(st: str, a="world", b="Hello world"):
    return st + a == b
def sol346(a="world", b="Hello world"):
    """Solve simple string addition problem."""
    return b[:len(b) - len(a)]
# assert sat346(sol346())

def sat347(s: str, dups=2021):
    return len(set(s)) == len(s) - dups
def sol347(dups=2021):
    """Find a string with dups duplicate chars"""
    return "a" * (dups + 1)
# assert sat347(sol347())

def sat348(s: str, target="foofoofoofoo", n=2):
    return s * n == target
def sol348(target="foofoofoofoo", n=2):
    """Find a string which when repeated n times gives target"""
    if n == 0:
        return ''
    return target[:len(target) // n]
# assert sat348(sol348())

def sat349(n: int, target="foofoofoofoo", s="foofoo"):
    return s * n == target
def sol349(target="foofoofoofoo", s="foofoo"):
    """Find n such that s repeated n times gives target"""
    if len(s) == 0:
        return 1
    return len(target) // len(s)
# assert sat349(sol349())

