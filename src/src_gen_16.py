from typing import List

def sat160(pals: List[int], n=1099, count=49):
    return all(0 <= i <= n and str(i) == str(i)[::-1] and i % 2 == 0 for i in pals) and len(set(pals)) >= count
def sol160(n=1099, count=49):
    """Find all even palindromes up to n

    3 => [0, 2]
    """
    return [i for i in range(0, n + 1, 2) if str(i) == str(i)[::-1]]
# assert sat160(sol160())

def sat161(pos: List[int], nums=[-804, 9124, -945, 2410, 0, 21, -123]):
    for n in pos + nums:
        s = str(n)
        if int(s[:2]) + sum(int(c) for c in s[2:]) <= 0:
            assert n not in pos
        else:
            assert pos.count(n) == nums.count(n)
    return True
def sol161(nums=[-804, 9124, -945, 2410, 0, 21, -123]):
    """Filter for the numbers in nums whose sum of digits is > 0, where the first digit can be negative.

    [12, -7, -102, -100] => [12, -102]
    """
    def bad(n):
        s = str(n)
        return int(s[:2]) + sum(int(c) for c in s[2:]) <= 0

    return [n for n in nums if not bad(n)]
# assert sat161(sol161())

def sat162(original: List[int], arr=[2, 3, -1, -1, 0, 1, 1]):
    assert str(original)[1:-1] in str(sorted(original) * 2), "Not ring sorted"
    return any(original == arr[:i] + arr[i + 1:] for i in range(len(arr) + 1))
def sol162(arr=[2, 3, -1, -1, 0, 1, 1]):
    """
    An array is ring-sorted if it is a "rotation" of a non-decreasing list.
    Remove at most one element from arr to make it ring-sorted.

    [1, 2, 3, -1, 6, 0] => [1, 2, 3, -1, 0]
    """
    def sat162(near):
        order_violations = 0
        erasures = 0
        for i, n in enumerate(near):
            if n < near[i - 1]:  # -1 when i =0 gives last element
                order_violations += 1
            while n != arr[i + erasures]:
                erasures += 1
        return order_violations <= 1 and erasures <= 1

    candidates = [arr] + [arr[:i] + arr[i + 1:] for i in range(len(arr))]
    return next(near for near in candidates if sat162(near))
# assert sat162(sol162())

def sat163(swaps: List[List[int]], nums1=[1, 3, 2, 4, 5, 8, 7, 11], nums2=[0, 7, 0, 8, 19, 4, 41, 43, 42]):
    copy1 = nums1[:]
    copy2 = nums2[:]
    for i, j in swaps:
        copy1[i], copy2[j] = copy2[j], copy1[i]
    return all(n % 2 == 0 for n in copy1)
def sol163(nums1=[1, 3, 2, 4, 5, 8, 7, 11], nums2=[0, 7, 0, 8, 19, 4, 41, 43, 42]):
    """
    Find a sequence of swaps (indices into two lists) such that, after making those swaps, all numbers in the
    first list are even

    [1, 3, 4] [2, 4, 5] => [0, 1]
    """
    odds = [i for i, n in enumerate(nums1) if n % 2 == 1]
    evens = [i for i, n in enumerate(nums2) if n % 2 == 0]
    return [[i, j] for i, j in zip(odds, evens)]
# assert sat163(sol163())

def sat164(s: str, counts={'a': 4, 'b': 17, 'd': 101, 'e': 0, 'f': 12}):
    chars = s.split()
    for c in chars:
        assert chars.count(c) == counts[c]
    return len(chars) == sum(counts.values())
def sol164(counts={'a': 4, 'b': 17, 'd': 101, 'e': 0, 'f': 12}):
    """Find a string consisting of space-separated characters with given counts

    {"f": 1, "o": 2} => "oof"
    """
    return " ".join(c for c, i in counts.items() for _ in range(i))
# assert sat164(sol164())

def sat165(strings: List[str], a="this is a test", b="cat"):
    s, is_palindrome = strings
    i = 0
    for c in a:
        if c not in b:
            assert s[i] == c
            i += 1
    assert i == len(s)
    return is_palindrome == str(s == s[::-1])
def sol165(a="this is a test", b="cat"):
    """
    Return a pair of a strings where the first string is the same as a with all the characters of b removed,
    and the second string is 'True' if this string is a palindrome otherwise 'False'.

    a="madam, I'm adam." b = "Yes, we're here." => ['madamImadam', 'True']
    """
    s = "".join(c for c in a if c not in b)
    return [s, str(s == s[::-1])]
# assert sat165(sol165())

def sat166(answers: List[str], lst=['234515', '21503', '2506236943']):
    if len(answers) != len(lst):
        return False
    for a, s in zip(answers, lst):
        if "t" in a:
            return False
        num_odds = sum(int(i) % 2 for i in s)
        if a.replace(str(num_odds), "t") != "this is a test":
            return False
    return True
def sol166(lst=['234515', '21503', '2506236943']):
    """For each string in lst, count the number of odd digits. Find a string with no t's such that replacing
    this number by t gives the string 'this is a test'

    ["123", "2"] => ["2his is a 2es2", "0his a 0es0"]
    """
    return ["this is a test".replace("t", str(sum(c in "13579" for c in s))) for s in lst]
# assert sat166(sol166())

def sat167(start_end: List[int], base=7, p=50741, upper=-4897754):
    start, end = start_end
    return sum(pow(base, i, p) - p // 2 for i in range(start, end)) <= upper
def sol167(base=7, p=50741, upper=-4897754):
    """Find the start and end of the smallest-sum subarray of [(base^i mod p) - p/2 for i=start,..., end]

    base=3, p=7, upper =-3 => [0, 3]
    # because -3 is the sum of the elements [0:3] of [-2, 0, -1, 3, 1, 2, -2, 0, -1, 3 ...
    """
    tot = 0
    best_tot = 0
    best_end = 0
    best_start = 0
    largest_cumulative_sum = 0
    largest_cumulative_sum_index = 0

    n = 1

    for i in range(p + 1):
        if tot > largest_cumulative_sum:
            largest_cumulative_sum = tot
            largest_cumulative_sum_index = i
        if tot - largest_cumulative_sum < best_tot:
            best_tot = tot - largest_cumulative_sum
            best_start = largest_cumulative_sum_index
            best_end = i

        tot += (n - p // 2)
        n = (n * base) % p

    return [best_start, best_end]
# assert sat167(sol167())

def sat168(wells: List[List[List[int]]], grid=[[1, 1, 0, 1, 1], [0, 0, 0, 0, 0], [1, 1, 0, 0, 1]], capacity=2):
    grid2 = [[0 for _ in row] for row in grid]
    for group in wells:
        assert len(group) <= capacity
        for i, j in group:
            assert grid2[i][j] == 0
            grid2[i][j] = 1
    assert sum(len(group) != capacity for group in wells) <= 1  # at most one under-capacity group
    return grid2 == grid
def sol168(grid=[[1, 1, 0, 1, 1], [0, 0, 0, 0, 0], [1, 1, 0, 0, 1]], capacity=2):
    """Given a grid, partition the 1's into groups of capacity [x, y] pairs, with at most one incomplete group"""
    ans = []
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 1:
                if not ans or len(ans[-1]) == capacity:
                    ans.append([])
                ans[-1].append([i, j])
    return ans
# assert sat168(sol168())

def sat169(ordered: List[int], arr=[4, 2, 3, -1, 15, 2, 6, 9, 5, 16, 1048576]):
    if sorted(ordered) != sorted(arr):
        return False  # not even a permutation
    return all(bin(a).count("1") <= bin(b).count("1") for a, b in zip(ordered, ordered[1:]))
def sol169(arr=[4, 2, 3, -1, 15, 2, 6, 9, 5, 16, 1048576]):
    """Sort the numbers in arr based on the number of 1's in their binary representation.

    [1, 2, 3, 4, 6] => [1, 2, 4, 3, 6]
    """
    return sorted(arr, key=lambda n: bin(n).count("1"))
# assert sat169(sol169())

