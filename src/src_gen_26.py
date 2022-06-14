from typing import List

def sat260(nums: List[int], tot=12345, n=5):
    return len(nums) == len(set(nums)) == n and sum(nums) == tot and all(i >= i % 2 > 0 for i in nums)
def sol260(tot=12345, n=5):
    """Find n distinct positive odd integers that sum to tot"""
    return list(range(1, 2 * n - 1, 2)) + [tot - sum(range(1, 2 * n - 1, 2))]
assert sat260(sol260())

def sat261(rotations: List[int], target="wonderful", upper=69):
    s = "abcdefghijklmnopqrstuvwxyz"
    assert len(rotations) == len(target)
    for r, c in zip(rotations, target):
        s = s[r:] + s[:r]
        assert s[0] == c

    return sum(abs(r) for r in rotations) <= upper
def sol261(target="wonderful", upper=69):
    """
    We begin with the string `"a...z"`

    An `r`-rotation of a string means shifting it to the right (positive) or left (negative) by `r` characters and
    cycling around. Given a target string of length n, find the n rotations that put the consecutive characters
    of that string at the beginning of the r-rotation, with minimal sum of absolute values of the `r`'s.

    For example if the string was `'dad'`, the minimal rotations would be `[3, -3, 3]` with a total of `9`.
    """
    s = "abcdefghijklmnopqrstuvwxyz"
    ans = []
    for c in target:
        i = s.index(c)
        r = min([i, i - len(s)], key=abs)
        ans.append(r)
        s = s[r:] + s[:r]
        assert s[0] == c
    return ans
assert sat261(sol261())

def sat262(bills: List[int], denominations=[1, 25, 35, 84], n=980, max_len=14):
    return sum(bills) == n and all(b in denominations for b in bills) and len(bills) <= max_len
def sol262(denominations=[1, 25, 35, 84], n=980, max_len=14):
    """
    Find the shortest sequence (length <= max_len) that sum to n, where each number is in denominations
    """
    """
    This solution uses dynamic programming, I believe it could be further sped up without having to count
    all the way up to denominations.
    """
    denominations = sorted(set(denominations)) # remove duplicates
    seqs = [[0 for _ in denominations] +[0]]  # vectors
    for i in range(1, n + 1):
        _, j, k = min((seqs[i - k][-1], j, k) for j, k in enumerate(denominations) if k <= i)
        s = seqs[i - k]
        seqs.append([*s[:j], s[j] + 1, *s[j + 1:-1], s[-1] + 1])

    return [k for k, count in zip(denominations, seqs[-1]) for _ in range(count)]
assert sat262(sol262())

def sat263(sides: List[int], options=[2, 512, 1024], n=340282366920938463463374607431768211456, max_dim=13):
    prod = 1
    for b in sides:
        prod *= b
    return prod == n and set(sides) <= set(options) and len(sides) <= max_dim
def sol263(options=[2, 512, 1024], n=340282366920938463463374607431768211456, max_dim=13):
    """
    Find the side lengths of a box in fewest dimensions (dimension <= max_dim) whose volume is n,
     where each side length is in options
    """
    options = sorted(set(options))
    base = options[0]
    logs = []
    for i in options + [n]:
        j = 1
        log = 0
        while j < i:
            log +=1
            j *= base
        assert j == i, "All numbers must be a power of the smallest number"
        logs.append(log)
    denominations, n = logs[:-1], logs[-1]

    seqs = [[0 for _ in denominations] +[0]]  # vectors
    for i in range(1, n + 1):
        _, j, k = min((seqs[i - k][-1], j, k) for j, k in enumerate(denominations) if k <= i)
        s = seqs[i - k]
        seqs.append([*s[:j], s[j] + 1, *s[j + 1:-1], s[-1] + 1])

    return [base ** k for k, count in zip(denominations, seqs[-1]) for _ in range(count)]
assert sat263(sol263())

def sat264(x: float, coeffs=[2.5, 1.3, -0.5]):
    a, b, c = coeffs
    return abs(a * x ** 2 + b * x + c) < 1e-6
def sol264(coeffs=[2.5, 1.3, -0.5]):
    """
    Find any (real) solution to:  a x^2 + b x + c where coeffs = [a, b, c].
    For example, since x^2 - 3x + 2 has a root at 1, sat(x = 1., coeffs = [1., -3., 2.]) is True.
    """
    a, b, c = coeffs
    if a == 0:
        ans = -c / b if b != 0 else 0.0
    else:
        ans = ((-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a))
    return ans
assert sat264(sol264())

def sat265(roots: List[float], coeffs=[1.3, -0.5]):
    b, c = coeffs
    r1, r2 = roots
    return abs(r1 + r2 + b) + abs(r1 * r2 - c) < 1e-6
def sol265(coeffs=[1.3, -0.5]):
    """Find all (real) solutions to: x^2 + b x + c (i.e., factor into roots), here coeffs = [b, c]"""
    b, c = coeffs
    delta = (b ** 2 - 4 * c) ** 0.5
    return [(-b + delta) / 2, (-b - delta) / 2]
assert sat265(sol265())

def sat266(x: float, coeffs=[2.0, 1.0, 0.0, 8.0]):
    return abs(sum(c * x ** (3 - i) for i, c in enumerate(coeffs))) < 1e-6
def sol266(coeffs=[2.0, 1.0, 0.0, 8.0]):
    """
    Find any (real) solution to: a x^3 + b x^2 + c x + d where coeffs = [a, b, c, d]
    For example, since (x-1)(x-2)(x-3) = x^3 - 6x^2 + 11x - 6, sat(x = 1., coeffs = [-6., 11., -6.]) is True.
    """
    a2, a1, a0 = [c / coeffs[0] for c in coeffs[1:]]
    p = (3 * a1 - a2 ** 2) / 3
    q = (9 * a1 * a2 - 27 * a0 - 2 * a2 ** 3) / 27
    delta = (q ** 2 + 4 * p ** 3 / 27) ** 0.5
    omega = (-(-1) ** (1 / 3))
    for cube in [(q + delta) / 2, (q - delta) / 2]:
        c = cube ** (1 / 3)
        for w in [c, c * omega, c * omega.conjugate()]:
            if w != 0:
                x = complex(w - p / (3 * w) - a2 / 3).real
                if abs(sum(c * x ** (3 - i) for i, c in enumerate(coeffs))) < 1e-6:
                    return x
assert sat266(sol266())

def sat267(roots: List[float], coeffs=[1.0, -2.0, -1.0]):
    r1, r2, r3 = roots
    a, b, c = coeffs
    return abs(r1 + r2 + r3 + a) + abs(r1 * r2 + r1 * r3 + r2 * r3 - b) + abs(r1 * r2 * r3 + c) < 1e-6
def sol267(coeffs=[1.0, -2.0, -1.0]):
    """Find all 3 distinct real roots of x^3 + a x^2 + b x + c, i.e., factor into (x-r1)(x-r2)(x-r3).
    coeffs = [a, b, c]. For example, since (x-1)(x-2)(x-3) = x^3 - 6x^2 + 11x - 6,
    sat(roots = [1., 2., 3.], coeffs = [-6., 11., -6.]) is True.
    """
    a, b, c = coeffs
    p = (3 * b - a ** 2) / 3
    q = (9 * b * a - 27 * c - 2 * a ** 3) / 27
    delta = (q ** 2 + 4 * p ** 3 / 27) ** 0.5
    omega = (-(-1) ** (1 / 3))
    ans = []
    for cube in [(q + delta) / 2, (q - delta) / 2]:
        v = cube ** (1 / 3)
        for w in [v, v * omega, v * omega.conjugate()]:
            if w != 0.0:
                x = complex(w - p / (3 * w) - a / 3).real
                if abs(x ** 3 + a * x ** 2 + b * x + c) < 1e-4:
                    if not ans or min(abs(z - x) for z in ans) > 1e-6:
                        ans.append(x)
    if len(ans) == 3:
        return ans
assert sat267(sol267())

def sat268(x: str, s=679):
    return s == sum([int(d) for d in x])
def sol268(s=679):
    """Find a number that its digits sum to a specific value."""
    return int(s / 9) * '9' + str(s % 9)
assert sat268(sol268())

def sat269(z: float, v=9, d=0.0001):
    return int(z * 1 / d % 10) == v
def sol269(v=9, d=0.0001):
    """Create a float with a specific decimal."""
    return v * d
assert sat269(sol269())

