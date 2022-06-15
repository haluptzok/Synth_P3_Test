from typing import List

def sat70(beats: List[int], score="o o o| o| .| .| .| o| o| o o o| .|"):
    return " ".join({1: '.|', 2: 'o|', 4: 'o'}[b] for b in beats) == score
def sol70(score="o o o| o| .| .| .| o| o| o o o| .|"):
    """
    Parse a string of notes to beats, 'o'=4, 'o|'=2, '.|'=1

    Example input:
    'o o .| o|'

    Example output:
    [4, 4, 1, 2]
    """
    mapping = {'.|': 1, 'o|': 2, 'o': 4}
    return [mapping[note] for note in score.split()]
# assert sat70(sol70())

def sat71(ans: List[int], s="Bananannanaannanaanananananana", sub="anan", count=7):
    return all(sub == s[i:i + len(sub)] and i >= 0 for i in ans) and len(set(ans)) >= count
def sol71(s="Bananannanaannanaanananananana", sub="anan", count=7):
    """
    Find occurrences of a substring in a parent string *including overlaps*

    Sample Input:
    'helllo', 'll'

    Sample Output:
    [2, 3]
    """
    ans = []
    for i in range(len(s) + 1):
        if s[i:i + len(sub)] == sub:
            ans.append(i)
    return ans
# assert sat71(sol71())

def sat72(ans: str, s="six one four three two nine eight"):
    nums = 'zero one two three four five six seven eight nine'.split()
    return [nums.index(x) for x in ans.split(" ")] == sorted([nums.index(x) for x in s.split(" ")])
def sol72(s="six one four three two nine eight"):
    """
    Sort numbers based on strings

    Sample input
    ---
    "six one four"

    Sample output
    ---
    "one four six"
    """
    nums = 'zero one two three four five six seven eight nine'.split()
    arr = [nums.index(x) for x in s.split()]
    arr.sort()
    ans = " ".join([nums[i] for i in arr])
    return ans
# assert sat72(sol72())

def sat73(inds: List[int], nums=[0.31, 21.3, 5.0, 9.0, 11.0, 5.01, 17.2]):
    a, b = inds
    assert a != b and a >= 0 and b >= 0
    for i in range(len(nums)):
        for j in range(i):
            assert abs(nums[i] - nums[j]) >= abs(nums[b] - nums[a])
    return True
def sol73(nums=[0.31, 21.3, 5.0, 9.0, 11.0, 5.01, 17.2]):
    """
    Given a list of numbers, find the indices of the closest pair.

    Sample Input:
    [1.2, 5.25, 0.89, 21.0, 5.23]

    Sample Output:
    [4, 1]
    """
    best = [0, 1]
    best_score = abs(nums[1] - nums[0])
    for i in range(len(nums)):
        for j in range(i):
            score = abs(nums[i] - nums[j])
            if score < best_score:
                best_score = score
                best = [i, j]
    return best
# assert sat73(sol73())

def sat74(ans: List[float], nums=[13.0, 17.0, 17.0, 15.5, 2.94]):
    assert min(ans) == 0.0 and max(ans) == 1.0
    a = min(nums)
    b = max(nums)
    for i in range(len(nums)):
        x = a + (b - a) * ans[i]
        assert abs(nums[i] - x) < 1e-6
    return True
def sol74(nums=[13.0, 17.0, 17.0, 15.5, 2.94]):
    """
    Rescale and shift numbers so that they cover the range [0, 1]

    Sample input
    ---
    [18.5, 17.0, 18.0, 19.0, 18.0]

    Sample output
    ---
    [0.75, 0.0, 0.5, 1.0, 0.5]
    """
    nums = nums.copy()

    a = min(nums)
    b = max(nums)
    if b - a == 0:
        return [0.0] + [1.0] * (len(nums) - 1)
    for i in range(len(nums)):
        nums[i] = (nums[i] - a) / (b - a)
    return nums
# assert sat74(sol74())

def sat75(candidates: List[str], int_indices=[2, 4, 7, 9, 101]):
    for i in int_indices:
        int(candidates[i])
    for i, s in enumerate(candidates):
        if i not in int_indices:
            try:
                int(s)
                return False
            except ValueError:
                pass
    return True
def sol75(int_indices=[2, 4, 7, 9, 101]):
    """
    Find a list of strings where the only valid integers are at the given indices

    Sample input
    ---
    [2, 4, 5]

    Sample output
    ---
    ["cat", "2.7", "2", "", "3", "-17", "free"]
    """
    if not int_indices:
        return []
    ans = [""] * (1 + max(abs(i) for i in int_indices))
    for i in int_indices:
        ans[i] = "17"
    return ans
# assert sat75(sol75())

def sat76(lengths: List[int], strs=['pneumonoultramicroscopicsilicovolcanoconiosis', ' ', 'foo', '2.5']):
    for length, s in zip(lengths, strs):
        try:
            s[length]
            return False
        except IndexError:
            s[length - 1]
    return len(lengths) == len(strs)
def sol76(strs=['pneumonoultramicroscopicsilicovolcanoconiosis', ' ', 'foo', '2.5']):
    """
    Find the lengths of a list of non-empty strings

    Sample input
    ---
    ["foo", "bars"]

    Sample output
    ---
    [3, 4]
    """
    return [len(s) for s in strs]
# assert sat76(sol76())

def sat77(d: int, n=123456):
    return n % d == 0 and d < n and all(n % e for e in range(d + 1, n))
def sol77(n=123456):
    """
    Find the largest integer divisor of a number n that is less than n

    Sample input
    ---
    1000

    Sample output
    ---
    500
    """
    return next(d for d in range(n - 1, 0, -1) if n % d == 0)
# assert sat77(sol77())

def sat78(factors: List[int], n=123456, num_factors=8):
    assert len(factors) == num_factors
    prod = 1
    for d in factors:
        prod *= d
        assert d > 1
    return prod == n
def sol78(n=123456, num_factors=8):
    """
    Factor number n into a given number of non-trivial factors

    Sample input
    ---
    1000, 6

    Sample output
    ---
    [2, 2, 2, 5, 5, 5]
    """
    if num_factors == 0:
        return []
    if num_factors == 1:
        return [n]
    ans = []
    for d in range(2, n):
        while n % d == 0:
            n //= d
            ans.append(d)
            if len(ans) == num_factors - 1:
                ans.append(n)
                return ans
    assert False
# assert sat78(sol78())

def sat79(ans: List[int], li=[2, 19, 2, 53, 1, 1, 2, 44, 17, 0, 19, 31]):
    return set(ans) == set(li) and all(li.index(ans[i]) < li.index(ans[i + 1]) for i in range(len(ans) - 1))
def sol79(li=[2, 19, 2, 53, 1, 1, 2, 44, 17, 0, 19, 31]):
    """
    Remove duplicates from a list of integers, preserving order

    Sample input
    ---
    [1, 3, 2, 9, 2, 1, 55]

    Sample output
    ---
    [1, 3, 2, 9, 55]
    """
    seen = set()
    ans = []
    for n in li:
        if n not in seen:
            ans.append(n)
            seen.add(n)
    return ans
# assert sat79(sol79())

