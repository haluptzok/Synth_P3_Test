from typing import List

def sat210(triples: List[List[int]], n=920, m=799):
    for a, b, c in triples:
        if not (a * a + b * b == c * c and 0 < a < b < c <= n):
            return False
    return triples == sorted(triples) and len(triples) >= m
def sol210(n=920, m=799):
    """Find m Pythagorean triples a^2 + b^2 == c^2 for integers 0 < a < b < c <= n, in sorted order

    (n=6, m=1) => [[3, 4, 5]]
    """
    return [[a, b, int((a * a + b * b) ** 0.5)]
            for a in range(3, int(n / (2 ** 0.5)))
            for b in range(a + 1, int((n * n - a * a) ** 0.5) + 1)
            if ((a * a + b * b) ** 0.5).is_integer()]
# assert sat210(sol210())

def sat211(s: str, pool=['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']):
    assert s in pool
    n = len(set(s))
    for p in pool:
        assert len(set(p)) <= n
    return True
def sol211(pool=['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']):
    """Select a string from the pool with the most unique characters

    ["woooow", "cow"] => "cow"
    """
    return max(pool, key=lambda x: len(set(x)))
# assert sat211(sol211())

def sat212(results: List[List[int]], stats=[[2, 3, 18], [4, 9, 2], [2, 5, 7], [3, 8, 12], [4, 9, 106]]):
    assert len(results) == len(stats)
    for (tot, remaining), (eaten, need, stock) in zip(results, stats):
        assert tot - eaten == min(need, stock)
        assert stock < need and remaining == 0 or stock >= need and remaining + need == stock
    return True
def sol212(stats=[[2, 3, 18], [4, 9, 2], [2, 5, 7], [3, 8, 12], [4, 9, 106]]):
    """For each triple of eaten, need, stock return a pair of total appetite and remaining

    [[2, 5, 6], [3, 9, 22]] => [[7, 1], [12, 13]]
    """
    results = []
    for (eaten, need, stock) in stats:
        results.append([eaten + min(need, stock), max(0, stock - need)])
    return results
# assert sat212(sol212())

def sat213(ops: List[str], target=2021, nums=[4, 6, 2, 1, 1, 3, 9]):
    assert len(ops) == len(set(ops)) and set(ops) == {"**", "*", "+", "-", "//", "%"}
    expr = str(nums[0])
    for n, op in zip(nums[1:], ops):
        expr += op + str(n)
    return eval(expr) == target
def sol213(target=2021, nums=[4, 6, 2, 1, 1, 3, 9]):
    """Find a permutation of the operators +-*/^% which when inserted between nums evaluates to target

    target=3, nums=[7, 2, 3, 4, 5, 1, 6] => ["+", "*", "**", "%", "//", "-"]
                                            # because 7 + 2 * 3 ** 4 % 5 // 1 - 6 == 3
    """
    from itertools import permutations
    for ops in permutations(["**", "*", "+", "-", "//", "%"]):
        expr = str(nums[0])
        for n, op in zip(nums[1:], ops):
            expr += op + str(n)
        try:
            if eval(expr) == target:
                return list(ops)
        except (ZeroDivisionError, SyntaxError):
            pass
    assert False
# assert sat213(sol213())

def sat214(rev: List[str], strs=['cat', 'u8u', '12532', '', '191', '4tUn8', 'ewrWQTEW', 'i', 'IoU']):
    assert len(rev) == len(strs)
    return all(r.swapcase() == s != r or r[::-1] == s == s.swapcase() for r, s in zip(rev, strs))
def sol214(strs=['cat', 'u8u', '12532', '', '191', '4tUn8', 'ewrWQTEW', 'i', 'IoU']):
    """Reverse the case of all strings. For those strings which contain no letters, reverse the strings.

    ["Test", "!@#"] => ["tEST", "#@!"]
    """
    return [s.swapcase() if s.swapcase() != s else s[::-1] for s in strs]
# assert sat214(sol214())

def sat215(positions: List[List[int]]):

    table = [[(i * 429436219 + j * 100239120) % 63491564 for j in range(13)] for i in range(64)]

    def zobrist(pos):
        h = 0
        for i in range(64):
            if pos[i]:
                h ^= table[i][pos[i]]
        return h

    a, b = positions
    return zobrist(a) == zobrist(b) and a != b
def sol215():
    """Find a collision for the given Zobrist chess board hash: https://en.wikipedia.org/wiki/Zobrist_hashing

    Each of the two positions should be encoded as a list of 64 integers 0-12"""
    hashes = {}
    table = [[(i * 429436219 + j * 100239120) % 63491564 for j in range(13)] for i in range(64)]

    def zobrist(pos):
        h = 0
        for i in range(64):
            if pos[i]:
                h ^= table[i][pos[i]]
        return h

    for i in range(1, 100000000):
        pos = [(i * 42 + ((i + 1) * j * 12589) % 54321) % 13 for j in range(64)]  # pseudo-random board
        h = zobrist(pos)
        if h in hashes:
            return [pos, hashes[h]]
        else:
            hashes[h] = pos
# assert sat215(sol215())

def sat216(ab: List[int], s="3298832990329923299432996329983300033002"):
    return abs(ab[0] - ab[1]) > 4 and s == "".join(str(i) for i in range(min(ab), max(ab) + 1) if i % 2 == 0)
def sol216(s="3298832990329923299432996329983300033002"):
    """Find integers [a, b] that are at least 5 apart and such that concatenating the even numbers
    between them gives the string s

    "32343638" => [31, 38]
    """
    for i in range(1, len(s)):
        n = int(s[:i])
        n -= (n + 1) % 2  # make n odd
        m = n + 1  # next even
        t = ""
        while len(t) < len(s):
            t += str(m)
            m += 2
        if s == t:
            return [n, m - 1]

    assert False
# assert sat216(sol216())

def sat217(b: bool, n=10):
    i = 0
    while i <= n:
        if i + i == n:
            return b == True
        i += 1
    return b == False
def sol217(n=10):
    """Determine if n can be evenly divided into two equal numbers. (Easy)"""
    return n % 2 == 0
# assert sat217(sol217())

def sat218(s: str, word="antidisestablishmentarianism", max_len=10):
    if len(word) <= max_len:
        return word == s
    return int(s[1:-1]) == len(word[1:-1]) and word[0] == s[0] and word[-1] == s[-1]
def sol218(word="antidisestablishmentarianism", max_len=10):
    """
    Abbreviate strings longer than a given length by replacing everything but the first and last characters by
    an integer indicating how many characters there were in between them.
    """
    if len(word) <= max_len:
        return word
    return f"{word[0]}{len(word) - 2}{word[-1]}"
# assert sat218(sol218())

def sat219(corners: List[List[int]], m=10, n=9, a=5, target=4):
    covered = {(i + x, j + y) for i, j in corners for x in range(a) for y in range(a)}
    assert len(covered) == len(corners) * a * a, "Double coverage"
    return len(corners) <= target and covered.issuperset({(x, y) for x in range(m) for y in range(n)})
def sol219(m=10, n=9, a=5, target=4):
    """Find a minimal list of corner locations for a×a tiles that covers [0, m] × [0, n] and does not double-cover
    squares.

    Sample Input:
    m = 10
    n = 9
    a = 5
    target = 4

    Sample Output:
    [[0, 0], [0, 5], [5, 0], [5, 5]]
    """
    return [[x, y] for x in range(0, m, a) for y in range(0, n, a)]
# assert sat219(sol219())

