from typing import List

def sat250(indexes: List[int], target=[1, 3, 4, 2, 5, 6, 7, 13, 12, 11, 9, 10, 8]):
    for i in range(1, len(target) + 1):
        if target[indexes[i - 1] - 1] != i:
            return False
    return True
def sol250(target=[1, 3, 4, 2, 5, 6, 7, 13, 12, 11, 9, 10, 8]):
    """Given a list of integers representing a permutation, invert the permutation."""
    return [1, 4, 2, 3, 5, 6, 7, 13, 11, 12, 10, 9, 8]
assert sat250(sol250())

def sat251(s: str, n=7012):
    return int(str(5 ** n)[:-2] + s) == 5 ** n
def sol251(n=7012):
    """What are the last two digits of 5^n?"""
    return ("1" if n == 0 else "5" if n == 1 else "25")
assert sat251(sol251())

def sat252(states: List[str], start="424", combo="778", target_len=12):
    assert all(len(s) == len(start) for s in states) and all(c in "0123456789" for s in states for c in s)
    for a, b in zip([start] + states, states + [combo]):
        assert sum(i != j for i, j in zip(a, b)) == 1
        assert all(abs(int(i) - int(j)) in {0, 1, 9} for i, j in zip(a, b))

    return len(states) <= target_len
def sol252(start="424", combo="778", target_len=12):
    """
    Shortest Combination Lock Path

    Given a starting a final lock position, find the (minimal) intermediate states, where each transition
    involves increasing or decreasing a single digit (mod 10).

    Example:
    start = "012"
    combo = "329"
    output: ['112', '212', '312', '322', '321', '320']
    """
    n = len(start)
    ans = []
    a, b = [[int(c) for c in x] for x in [start, combo]]
    for i in range(n):
        while a[i] != b[i]:
            a[i] = (a[i] - 1 if (a[i] - b[i]) % 10 < 5 else a[i] + 1) % 10
            if a != b:
                ans.append("".join(str(i) for i in a))
    return ans
assert sat252(sol252())

def sat253(states: List[str], start="424", combo="778", target_len=12):
    return all(sum((int(a[i]) - int(b[i])) ** 2 % 10 for i in range(len(start))) == 1
               for a, b in zip([start] + states, states[:target_len] + [combo]))
def sol253(start="424", combo="778", target_len=12):
    """Figure out what this does only from the code"""
    n = len(start)
    ans = []
    a, b = [[int(c) for c in x] for x in [start, combo]]
    for i in range(n):
        while a[i] != b[i]:
            a[i] = (a[i] - 1 if (a[i] - b[i]) % 10 < 5 else a[i] + 1) % 10
            if a != b:
                ans.append("".join(str(i) for i in a))
    return ans
assert sat253(sol253())

def sat254(s: str, perm="qwertyuiopasdfghjklzxcvbnm", target="hello are you there?"):
    return "".join((perm[(perm.index(c) + 1) % len(perm)] if c in perm else c) for c in s) == target
def sol254(perm="qwertyuiopasdfghjklzxcvbnm", target="hello are you there?"):
    """Find a string that, when a given permutation of characters is applied, has a given result."""
    return "".join((perm[(perm.index(c) - 1) % len(perm)] if c in perm else c) for c in target)
assert sat254(sol254())

def sat255(lists: List[List[int]], items=[5, 4, 9, 4, 5, 5, 5, 1, 5, 5], length=4):
    a, b = lists
    assert len(a) == len(b) == length
    assert len(set(a)) == len(a)
    assert len(set(b)) == 1
    for i in a + b:
        assert (a + b).count(i) <= items.count(i)
    return True
def sol255(items=[5, 4, 9, 4, 5, 5, 5, 1, 5, 5], length=4):
    """
    Given a list of integers and a target length, create of the given length such that:
        * The first list must be all different numbers.
        * The second must be all the same number.
        * The two lists together comprise a sublist of all the list items
    """
    from collections import Counter
    [[a, count]] = Counter(items).most_common(1)
    assert count >= length
    seen = {a}
    dedup = [i for i in items if i not in seen and not seen.add(i)]
    return [(dedup + [a])[:length], [a] * length]
assert sat255(sol255())

def sat256(seq: List[int], n=10000, length=5017):
    return all(i in [1, 2] for i in seq) and sum(seq) == n and len(seq) == length
def sol256(n=10000, length=5017):
    """Find a sequence of 1's and 2's of a given length that that adds up to n"""
    return [2] * (n - length) + [1] * (2 * length - n)
assert sat256(sol256())

def sat257(start: int, k=3, upper=6, seq=[17, 1, 2, 65, 18, 91, -30, 100, 3, 1, 2]):
    return 0 <= start <= len(seq) - k and sum(seq[start:start + k]) <= upper
def sol257(k=3, upper=6, seq=[17, 1, 2, 65, 18, 91, -30, 100, 3, 1, 2]):
    """Find a sequence of k consecutive indices whose sum is minimal"""
    return min(range(len(seq) - k + 1), key=lambda start: sum(seq[start:start + k]))
assert sat257(sol257())

def sat258(start: int, k=3, lower=150, seq=[3, 1, 2, 65, 18, 91, -30, 100, 0, 19, 52]):
    return 0 <= start <= len(seq) - k and sum(seq[start:start + k]) >= lower
def sol258(k=3, lower=150, seq=[3, 1, 2, 65, 18, 91, -30, 100, 0, 19, 52]):
    """Find a sequence of k consecutive indices whose sum is maximal"""
    return max(range(len(seq) - k + 1), key=lambda start: sum(seq[start:start + k]))
assert sat258(sol258())

def sat259(start: int, k=3, lower=100000, seq=[91, 1, 2, 64, 18, 91, -30, 100, 3, 65, 18]):
    prod = 1
    for i in range(start, start + k):
        prod *= seq[i]
    return prod >= lower
def sol259(k=3, lower=100000, seq=[91, 1, 2, 64, 18, 91, -30, 100, 3, 65, 18]):
    """Find a sequence of k consecutive indices whose product is maximal, possibly looping around"""
    def prod(start):
        ans = 1
        for i in range(start, start + k):
            ans *= seq[i]
        return ans

    return max(range(-len(seq), len(seq) - k + 1), key=prod)
assert sat259(sol259())

