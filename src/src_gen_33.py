from typing import List

def sat330(n: int, a=15, b=27, upper_bound=150):
    return n % a == 0 and n % b == 0 and 0 < n <= upper_bound
def sol330(a=15, b=27, upper_bound=150):
    """Find a small common multiple of two integers."""
    m, n = min(a, b), max(a, b)
    while m > 0:
        m, n = n % m, m
    return a * (b // n)
# assert sat330(sol330())

def sat331(n: int, nums=[15, 27, 102], upper_bound=5000):
    return all(n % i == 0 for i in nums) and 0 < n <= upper_bound
def sol331(nums=[15, 27, 102], upper_bound=5000):
    """Find a small common multiple of a list of integers."""
    ans = 1
    for i in nums:
        m, n = min(i, ans), max(i, ans)
        while m > 0:
            m, n = n % m, m
        ans *= (i // n)
    return ans
# assert sat331(sol331())

def sat332(n: int, b=2, target=5):
    return (b ** n) % n == target
def sol332(b=2, target=5):
    """Solve for n: b^n = target (mod n)"""
    for n in range(1, 10 ** 5):
        if pow(b, n, n) == target:
            return n
# assert sat332(sol332())

def sat333(nums: List[int], target=983):
    assert target % 9 not in [4, 5], "Hint"
    return len(nums) == 3 and sum([i ** 3 for i in nums]) == target
def sol333(target=983):
    """Given n, find integers a, b, c such that a^3 + b^3 + c^3 = n."""
    assert target % 9 not in {4, 5}
    for i in range(20):
        for j in range(i + 1):
            for k in range(-20, j + 1):
                n = i ** 3 + j ** 3 + k ** 3
                if n == target:
                    return [i, j, k]
                if n == -target:
                    return [-i, -j, -k]
# assert sat333(sol333())

def sat334(nums: List[int], n=12345):
    return len(nums) <= 4 and sum(i ** 2 for i in nums) == n
def sol334(n=12345):
    """Find four integers whose squares sum to n"""
    m = n
    squares = {i ** 2: i for i in range(int(m ** 0.5) + 2) if i ** 2 <= m}
    sums_of_squares = {i + j: [a, b] for i, a in squares.items() for j, b in squares.items()}
    for s in sums_of_squares:
        if m - s in sums_of_squares:
            return sums_of_squares[m - s] + sums_of_squares[s]
    assert False, "Should never reach here"
# assert sat334(sol334())

def sat335(i: int, n=241864633):
    return 1 < i < n and n % i == 0
def sol335(n=241864633):
    """Find a non-trivial factor of integer n"""
    if n % 2 == 0:
        return 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return i

    assert False, "problem defined for composite n only"
# assert sat335(sol335())

def sat336(n: int, g=44337, p=69337, t=38187):
    return pow(g, n, p) == t
def sol336(g=44337, p=69337, t=38187):
    """Find n such that g^n is congruent to t mod n"""
    for n in range(p):
        if pow(g, n, p) == t:
            return n
    assert False, f"unsolvable discrete log problem g={g}, t={t}, p={p}"
# assert sat336(sol336())

def sat337(li: List[int], k=5):
    def prod(nums):
        ans = 1
        for i in nums:
            ans *= i
        return ans

    return min(li) > 1 and len(li) == k and all((1 + prod(li[:i] + li[i + 1:])) % li[i] == 0 for i in range(k))
def sol337(k=5):
    """Find k positive integers such that each integer divides (the product of the rest plus 1)."""
    n = 2
    prod = 1
    ans = []
    while len(ans) < k:
        ans.append(n)
        prod *= n
        n = prod + 1
    return ans
# assert sat337(sol337())

def sat338(n: int, t=197, upper=20):
    m = n
    for i in range(t):
        if n <= 1:
            return False
        n = 3 * n + 1 if n % 2 else n // 2
    return n == 1 and m <= 2 ** upper
def sol338(t=197, upper=20):
    """
    Consider the following process. Start with an integer `n` and repeatedly applying the operation:
    * if n is even, divide n by 2,
    * if n is odd, multiply n by 3 and add 1
    Find `0 < n < upper` so that it takes exactly `t` steps to reach 1.
    """
    # Faster solution for simultaneously solving multiple problems is of course possible
    bound = t + 10
    while True:
        bound *= 2
        prev = {1}
        seen = set()
        for delay in range(t):
            seen.update(prev)
            curr = {2 * n for n in prev}
            curr.update({(n - 1) // 3 for n in prev if n % 6 == 4})
            prev = {n for n in curr if n <= bound} - seen
        if prev:
            return min(prev)
# assert sat338(sol338())

def sat339(n: int):
    return pow(2, n, n) == 3
def sol339():
    """Find n  such that 2^n mod n = 3"""
    return 4700063497
# assert sat339(sol339())

