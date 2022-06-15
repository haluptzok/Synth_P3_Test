from typing import List

def sat40(coords: List[List[int]], side=10, num_points=20):
    for i1 in range(len(coords)):
        x1, y1 = coords[i1]
        assert 0 <= x1 < side and 0 <= y1 < side
        for i2 in range(i1):
            x2, y2 = coords[i2]
            for i3 in range(i2):
                x3, y3 = coords[i3]
                assert x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) != 0
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points
def sol40(side=10, num_points=20):
    """Find num_points points in an side x side grid such that no three points are collinear."""
    from itertools import combinations
    assert side <= 5 or side == 10, "Don't know how to solve other sides"

    def test(coords):
        return all(p[0] * (q[1] - r[1]) + q[0] * (r[1] - p[1]) + r[0] * (p[1] - q[1])
                   for p, q, r in combinations(coords, 3))

    if side <= 5:
        grid = [[i, j] for i in range(side) for j in range(side)]
        return next(list(coords) for coords in combinations(grid, num_points) if test(coords))

    if side == 10:
        def mirror(coords):  # rotate to all four corners
            return [[a, b] for x, y in coords for a in [x, side - 1 - x] for b in [y, side - 1 - y]]

        grid = [[i, j] for i in range(side // 2) for j in range(side // 2)]
        return next(list(mirror(coords)) for coords in combinations(grid, side // 2) if
                    test(coords) and test(mirror(coords)))
# assert sat40(sol40())

def sat41(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target
def sol41(target=80, max_stamps=4, options=[10, 32, 8]):
    """Find a selection of at most max_stamps stamps whose total worth is the target value."""
    from itertools import combinations_with_replacement
    for n in range(max_stamps + 1):
        for c in combinations_with_replacement(options, n):
            if sum(c) == target:
                return list(c)
# assert sat41(sol41())

def sat42(x: str, puz="____9_2___7__________1_8_4____2_78____4_____1____69____2_8___5__6__3_7___49______"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True
def sol42(puz="____9_2___7__________1_8_4____2_78____4_____1____69____2_8___5__6__3_7___49______"):
    """Find the unique valid solution to the Sudoku puzzle"""
    """Simple depth-first backtracking solver that branches at the square with fewest possibilities"""
    sets = [{int(c)} if c != '_' else set(range(1, 10)) for c in puz]

    groups = []
    for i in range(9):
        groups.append(list(range(9 * i, 9 * i + 9)))
        groups.append(list(range(i, i + 81, 9)))
        groups.append([9 * a + b + i + 26 * (i % 3) for a in range(3) for b in range(3)])

    inv = [[] for i in range(81)]
    for g in groups:
        for i in g:
            inv[i].append(g)

    def reduce():
        """Reduce possibilities and return False if it's clearly impossible to solve, True otherwise.
        Repeatedly applies two types of logic:
        * When an entry has a single possibility, remove that value from all 20 neighbors
        * When a row/col/square has only one entry with k as a possibility, fill in that possibility
        """
        done = False
        while not done:
            done = True
            for i in range(81):
                new = sets[i] - {k for g in inv[i] for j in g if j != i and len(sets[j]) == 1 for k in sets[j]}
                if not new:
                    return False
                if len(sets[i]) != len(new):
                    sets[i] = new
                    done = False

            for g in groups:
                for k in range(1, 10):
                    possibilities = [i for i in g if k in sets[i]]
                    if not possibilities:
                        return False
                    if len(possibilities) == 1:
                        i = possibilities[0]
                        if len(sets[i]) > 1:
                            done = False
                            sets[i] = {k}

        return True

    ans = []

    counter = 0

    def solve_helper():
        nonlocal sets, ans, counter
        counter += 1
        assert len(ans) <= 1, "Sudoku puzzle should have a unique solution"
        old_sets = sets[:]
        if reduce():
            if all(len(s) == 1 for s in sets):
                ans.append("".join(str(list(s)[0]) for s in sets))
            else:
                smallest_set = min(range(81), key=lambda i: len(sets[i]) if len(sets[i]) > 1 else 10)
                for v in sorted(sets[smallest_set]):
                    sets[smallest_set] = {v}
                    solve_helper()

        sets = old_sets

    solve_helper()
    assert ans, "No solution found"
    return ans[0]
# assert sat42(sol42())

def sat43(xy_sides: List[List[int]]):
    n = max(x + side for x, y, side in xy_sides)
    assert len({side for x, y, side in xy_sides}) == len(xy_sides) > 1
    for x, y, s in xy_sides:
        assert 0 <= y < y + s <= n and 0 <= x
        for x2, y2, s2 in xy_sides:
            assert s2 <= s or x2 >= x + s or x2 + s2 <= x or y2 >= y + s or y2 + s2 <= y

    return sum(side ** 2 for x, y, side in xy_sides) == n ** 2
def sol43():
    """
    Partition a square into smaller squares with unique side lengths. A perfect squared path has distinct sides.
    xy_sides is a List of (x, y, side)
    """
    return [[0, 0, 50], [0, 50, 29], [0, 79, 33], [29, 50, 25], [29, 75, 4], [33, 75, 37], [50, 0, 35],
            [50, 35, 15], [54, 50, 9], [54, 59, 16], [63, 50, 2], [63, 52, 7], [65, 35, 17], [70, 52, 18],
            [70, 70, 42], [82, 35, 11], [82, 46, 6], [85, 0, 27], [85, 27, 8], [88, 46, 24], [93, 27, 19]]
# assert sat43(sol43())

def sat44(n: int, lace="bbrbrbbbbbbrrrrrrrbrrrrbbbrbrrbbbrbrrrbrrbrrbrbbrrrrrbrbbbrrrbbbrbbrbbbrbrbb"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")
def sol44(lace="bbrbrbbbbbbrrrrrrrbrrrrbbbrbrrbbbrbrrrbrrbrrbrbbrrrrrbrbbbrrrbbbrbbrbbbrbrbb"):
    """
    Find a split dividing the given red/blue necklace in half at n so that each piece has an equal number of
    reds and blues.
    """
    if lace == "":
        return 0
    return next(n for n in range(len(lace) // 2) if lace[n: n + len(lace) // 2].count("r") == len(lace) // 4)
# assert sat44(sol44())

def sat45(n: int):
    s = str(n * n)
    for i in "0123456789":
        assert s.count(i) == 1
    return True
def sol45():
    """Find an integer whose square has all digits 0-9 once."""
    for n in range(10 ** 5):
        if sorted([int(s) for s in str(n * n)]) == list(range(10)):
            return n
# assert sat45(sol45())

def sat46(nums: List[int]):
    return [sorted([int(s) for s in str(n * n)]) for n in set(nums)] == [list(range(10))] * 174
def sol46():
    """Find all 174 integers whose 10-digit square has all digits 0-9 just once."""
    return [i for i in range(-10 ** 5, 10 ** 5) if sorted([int(s) for s in str(i * i)]) == list(range(10))]
# assert sat46(sol46())

def sat47(expr: str, nums=[3, 7, 3, 7]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""
    for i in range(len(expr)):
        if i == 0 or expr[i - 1] in "+*-/(":
            assert expr[i] in "123456789(", "Expr cannot contain **, //, or unary -"
        assert expr[i] in "1234567890()+-*/", "Expr can only contain `0123456789()+-*/`"
        digits += expr[i] if expr[i] in "0123456789" else " "
    assert sorted(int(s) for s in digits.split()) == sorted(nums), "Each number must occur exactly once"
    return abs(eval(expr) - 24.0) < 1e-6
def sol47(nums=[3, 7, 3, 7]):
    """Find a formula with two 3's and two 7's and + - * / (and parentheses) that evaluates to 24."""
    def helper(pairs):
        if len(pairs) == 2:
            (x, s), (y, t) = pairs
            ans = {
                x + y: f"{s}+{t}",
                x - y: f"{s}-({t})",
                y - x: f"{t}-({s})",
                x * y: f"({s})*({t})"
            }
            if y != 0:
                ans[x / y] = f"({s})/({t})"
            if x != 0:
                ans[y / x] = f"({t})/({s})"
            return ans
        ans = {y: t
               for i in range(len(pairs))
               for x_s in helper(pairs[:i] + pairs[i + 1:]).items()
               for y, t in helper([x_s, pairs[i]]).items()}
        if len(pairs) == 3:
            return ans
        ans.update({z: u
                    for i in range(1, 4)
                    for x_s in helper([pairs[0], pairs[i]]).items()
                    for y_t in helper(pairs[1:i] + pairs[i + 1:]).items()
                    for z, u in helper([x_s, y_t]).items()
                    })
        return ans

    derivations = helper([(n, str(n)) for n in nums])
    for x in derivations:
        if abs(x - 24.0) < 1e-6:
            return derivations[x]
# assert sat47(sol47())

def sat48(s: str):
    return set(s) <= set("18-+*/") and s.count("8") == 2 and s.count("1") == 1 and eval(s) == 63
def sol48():
    """Find a formula using two 8s and two 1's and -+*/ that evaluates to 1."""
    return "8*8-1"
# assert sat48(sol48())

def sat49(s: str):
    return set(s) <= set("18-+*/") and s.count("8") == 3 and s.count("1") == 1 and eval(s) == 63
def sol49():
    """Find an expression using two 8s and two 1's and -+*/ that evaluates to 1."""
    return "8*8-1**8"
# assert sat49(sol49())

