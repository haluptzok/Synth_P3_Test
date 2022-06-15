from typing import List

def sat220(lb: List[bool], trips=[[1, 1, 0], [1, 0, 0], [0, 0, 0], [0, 1, 1], [0, 1, 1], [1, 1, 1], [1, 0, 1]]):
    return len(lb) == len(trips) and all(
        (b is True) if sum(s) >= 2 else (b is False) for b, s in zip(lb, trips))
def sol220(trips=[[1, 1, 0], [1, 0, 0], [0, 0, 0], [0, 1, 1], [0, 1, 1], [1, 1, 1], [1, 0, 1]]):
    """
    Given a list of lists of triples of integers, return True for each list with a total of at least 2 and
    False for each other list.
    """
    return [sum(s) >= 2 for s in trips]
# assert sat220(sol220())

def sat221(n: int, scores=[100, 95, 80, 70, 65, 9, 9, 9, 4, 2, 1], k=6):
    assert all(scores[i] >= scores[i + 1] for i in range(len(scores) - 1)), "Hint: scores are non-decreasing"
    return all(s >= scores[k] and s > 0 for s in scores[:n]) and all(s < scores[k] or s <= 0 for s in scores[n:])
def sol221(scores=[100, 95, 80, 70, 65, 9, 9, 9, 4, 2, 1], k=6):
    """
    Given a list of non-increasing integers and given an integer k, determine how many positive integers in the list
    are at least as large as the kth.
    """
    threshold = max(scores[k], 1)
    return sum(s >= threshold for s in scores)
# assert sat221(sol221())

def sat222(t: str, s="Problems"):
    i = 0
    for c in s.lower():
        if c in "aeiouy":
            continue
        assert t[i] == ".", f"expecting `.` at position {i}"
        i += 1
        assert t[i] == c, f"expecting `{c}`"
        i += 1
    return i == len(t)
def sol222(s="Problems"):
    """
    Given an alphabetic string s, remove all vowels (aeiouy/AEIOUY), insert a "." before each remaining letter
    (consonant), and make everything lowercase.

    Sample Input:
    s = "Problems"

    Sample Output:
    .p.r.b.l.m.s
    """
    return "".join("." + c for c in s.lower() if c not in "aeiouy")
# assert sat222(sol222())

def sat223(squares: List[List[int]], m=10, n=5, target=50):
    covered = []
    for i1, j1, i2, j2 in squares:
        assert (0 <= i1 <= i2 < m) and (0 <= j1 <= j2 < n) and (j2 - j1 + i2 - i1 == 1)
        covered += [(i1, j1), (i2, j2)]
    return len(set(covered)) == len(covered) == target
def sol223(m=10, n=5, target=50):
    """Tile an m x n checkerboard with 2 x 1 tiles. The solution is a list of fourtuples [i1, j1, i2, j2] with
    i2 == i1 and j2 == j1 + 1 or i2 == i1 + 1 and j2 == j1 with no overlap."""
    if m % 2 == 0:
        ans = [[i, j, i + 1, j] for i in range(0, m, 2) for j in range(n)]
    elif n % 2 == 0:
        ans = [[i, j, i, j + 1] for i in range(m) for j in range(0, n, 2)]
    else:
        ans = [[i, j, i + 1, j] for i in range(1, m, 2) for j in range(n)]
        ans += [[0, j, 0, j + 1] for j in range(0, n - 1, 2)]
    return ans
# assert sat223(sol223())

def sat224(n: int, ops=['x++', '--x', '--x'], target=19143212):
    for op in ops:
        if op in ["++x", "x++"]:
            n += 1
        else:
            assert op in ["--x", "x--"]
            n -= 1
    return n == target
def sol224(ops=['x++', '--x', '--x'], target=19143212):
    """
    Given a sequence of operations "++x", "x++", "--x", "x--", and a target value, find initial value so that the
    final value is the target value.

    Sample Input:
    ops = ["x++", "--x", "--x"]
    target = 12

    Sample Output:
    13
    """
    return target - ops.count("++x") - ops.count("x++") + ops.count("--x") + ops.count("x--")
# assert sat224(sol224())

def sat225(n: int, s="aaAab", t="aAaaB"):
    if n == 0:
        return s.lower() == t.lower()
    if n == 1:
        return s.lower() > t.lower()
    if n == -1:
        return s.lower() < t.lower()
    return False
def sol225(s="aaAab", t="aAaaB"):
    """Ignoring case, compare s, t lexicographically. Output 0 if they are =, -1 if s < t, 1 if s > t."""
    if s.lower() == t.lower():
        return 0
    if s.lower() > t.lower():
        return 1
    return -1
# assert sat225(sol225())

def sat226(s: str, matrix=[[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], max_moves=3):
    matrix = [m[:] for m in matrix]  # copy
    for c in s:
        if c in "01234":
            i = "01234".index(c)
            matrix[i], matrix[i + 1] = matrix[i + 1], matrix[i]
        if c in "abcde":
            j = "abcde".index(c)
            for row in matrix:
                row[j], row[j + 1] = row[j + 1], row[j]

    return len(s) <= max_moves and matrix[2][2] == 1
def sol226(matrix=[[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], max_moves=3):
    """
    We are given a 5x5 matrix with a single 1 like:

    0 0 0 0 0
    0 0 0 0 1
    0 0 0 0 0
    0 0 0 0 0
    0 0 0 0 0

    Find a (minimal) sequence of row and column swaps to move the 1 to the center. A move is a string
    in "0"-"4" indicating a row swap and "a"-"e" indicating a column swap
    """
    i = [sum(row) for row in matrix].index(1)
    j = matrix[i].index(1)
    ans = ""
    while i > 2:
        ans += str(i - 1)
        i -= 1
    while i < 2:
        ans += str(i)
        i += 1
    while j > 2:
        ans += "abcde"[j - 1]
        j -= 1
    while j < 2:
        ans += "abcde"[j]
        j += 1
    return ans
# assert sat226(sol226())

def sat227(s: str, inp="1+1+3+1+3+2+2+1+3+1+2"):
    return all(s.count(c) == inp.count(c) for c in inp + s) and all(s[i - 2] <= s[i] for i in range(2, len(s), 2))
def sol227(inp="1+1+3+1+3+2+2+1+3+1+2"):
    """Sort numbers in a sum of digits, e.g., 1+3+2+1 -> 1+1+2+3"""
    return "+".join(sorted(inp.split("+")))
# assert sat227(sol227())

def sat228(s: str, word="konjac"):
    for i in range(len(word)):
        if i == 0:
            if s[i] != word[i].upper():
                return False
        else:
            if s[i] != word[i]:
                return False
    return True
def sol228(word="konjac"):
    """Capitalize the first letter of word"""
    return word[0].upper() + word[1:]
# assert sat228(sol228())

def sat229(t: str, s="abbbcabbac", target=7):
    i = 0
    for c in t:
        while c != s[i]:
            i += 1
        i += 1
    return len(t) >= target and all(t[i] != t[i + 1] for i in range(len(t) - 1))
def sol229(s="abbbcabbac", target=7):
    """
    You are given a string consisting of a's, b's and c's, find any longest substring containing no repeated
    consecutive characters.

    Sample Input:
    `"abbbc"`

    Sample Output:
    `"abc"`
    """
    # target is ignored
    return s[:1] + "".join([b for a, b in zip(s, s[1:]) if b != a])
# assert sat229(sol229())

