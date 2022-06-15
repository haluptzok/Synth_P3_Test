from typing import List

def sat90(li: List[int], orig=[1, 6, 3, 41, 19, 4, 12, 3, 18, 5, -29, 0, 19521]):
    return orig[1::2] == li[1::2] and li[::2] == sorted(orig[::2])
def sol90(orig=[1, 6, 3, 41, 19, 4, 12, 3, 18, 5, -29, 0, 19521]):
    """
    Start with a list of integers, keep every other element in place and otherwise sort the list

    Sample Input:
    [8, 0, 7, 2, 9, 4, 1, 2, 8, 3]

    Sample Output:
    [1, 0, 2, 2, 4, 8, 8, 8, 9, 3]
    """
    n = len(orig)
    odds = orig[1::2]
    evens = sorted(orig[::2])
    ans = []
    for i in range(len(evens)):
        ans.append(evens[i])
        if i < len(odds):
            ans.append(odds[i])
    return ans
# assert sat90(sol90())

def sat91(s: str, target="Hello world"):

    def cycle3(trip):
        return trip if len(trip) != 3 else trip[2] + trip[:2]

    return target == "".join(cycle3(s[i: i + 3]) for i in range(0, len(s), 3))
def sol91(target="Hello world"):
    """
    Given a target string, find a string s such that when each group of three consecutive characters is cycled
    forward one character, you achieve the target string.

    Sample Input:
    "This is a test"

    Sample Output:
    'hiT is aste st'
    """
    def un_cycle3(trip):
        return trip if len(trip) != 3 else trip[1:3] + trip[0]

    return "".join(un_cycle3(target[i: i + 3]) for i in range(0, len(target), 3))
# assert sat91(sol91())

def sat92(n: int, lower=123456):
    assert any((i ** 0.5).is_integer() for i in [5 * n * n - 4, 5 * n * n + 4]), "n must be a Fibonacci number"
    assert all(n % i for i in range(2, int(n ** 0.5) + 1)), "n must be prime"
    return n > lower
def sol92(lower=123456):
    """
    Find a prime Fibonacci number bigger than a certain threshold, using Ira Gessel's test for Fibonacci numbers.

    Sample Input:
    10

    Sample Output:
    11
    """
    m, n = 2, 3
    while True:
        m, n = n, (m + n)
        if n > lower and all(n % i for i in range(2, int(n ** 0.5) + 1)):
            return n
# assert sat92(sol92())

def sat93(inds: List[int], nums=[12, 6, 41, 15, -10452, 18242, 10440, 6, 6, 6, 6]):
    return len(inds) == 3 and sum(nums[i] for i in inds) == 0
def sol93(nums=[12, 6, 41, 15, -10452, 18242, 10440, 6, 6, 6, 6]):
    """
    Find the indices of three numbers that sum to 0 in a list.

    --- Example input ---
    [1, 2, 4, -3, 5]

    --- Example output ---
    [0, 1, 3]
    """
    # \tilde{O}(n^2) algorithm
    inv = {n: i for i, n in enumerate(nums)}  # note that later duplicates will override earlier entries
    for i, n in enumerate(nums):
        if inv[n] == i:
            del inv[n]
        if any((-m - n) in inv for m in nums[:i]):  # found solution!
            j, m = next((j, m) for j, m in enumerate(nums) if (-m - n) in inv)
            k = inv[-m - n]
            return sorted([i, j, k])
# assert sat93(sol93())

def sat94(count: int, n=981):
    for i in range(n):
        for j in range(n):
            count -= 1
    return count == 0
def sol94(n=981):
    """
    Given n cars traveling East and n cars traveling West on a road, how many passings will there be?
    A passing is when one car passes another. The East-bound cars all begin further West than the West-bound cars.

    --Sample input--
    2

    --Sample output--
    4
    """
    return n ** 2
# assert sat94(sol94())

def sat95(new_list: List[int], old_list=[321, 12, 532, 129, 9, -12, 4, 56, 90, 0]):
    return [i - 1 for i in new_list] == old_list
def sol95(old_list=[321, 12, 532, 129, 9, -12, 4, 56, 90, 0]):
    """
    Decrement each element of new_list by 1 and check that it's old_list

    Sample Input:
    [17, 15, 99]

    Sample Output:
    [18, 16, 100]
    """
    return [i + 1 for i in old_list]
# assert sat95(sol95())

def sat96(inds: List[int], nums=[12, -10452, 18242, 10440, 81, 241, 525, -18242, 91, 20]):
    a, b = inds
    return nums[a] + nums[b] == 0 and a >= 0 and b >= 0
def sol96(nums=[12, -10452, 18242, 10440, 81, 241, 525, -18242, 91, 20]):
    """
    Find the indices of two numbers that sum to 0 in a list.

    Sample Input:
    [1, -4, -4, 7, -3]

    Sample Output:
    [1, 2]
    """
    s = set(nums)
    for i in s:
        if -i in s:
            return [nums.index(i), nums.index(-i)]
# assert sat96(sol96())

def sat97(s: str, n=142, base=7):
    return int(s, base) == n
def sol97(n=142, base=7):
    """
    Write n in the given base as a string

    Sample Input:
    n=23, base=12

    Sample Output:
    '1A'
    """
    assert 2 <= base <= 10
    ans = ""
    while n:
        ans = str(n % base) + ans
        n //= base
    return ans or "0"
# assert sat97(sol97())

def sat98(height: int, area=1319098728582, base=45126):
    return base * height == 2 * area
def sol98(area=1319098728582, base=45126):
    """
    Find the height of a triangle given the area and base. It is guaranteed that the answer is an integer.

    Sample Input:
    area = 6, base = 3

    Sample Output:
    4
    """
    return (2 * area) // base
# assert sat98(sol98())

def sat99(init: List[int], target=2021):
    a, b, c, d = init
    for i in range(99):
        a, b, c, d = b, c, d, (a + b + c + d)
    return a == target
def sol99(target=2021):
    """
    Define a four-wise Fibonacci sequence to be a sequence such that each number is the sum of the previous
    four. Given a target number, find an initial four numbers such that the 100th number in the sequence is the
    given target number.

    Sample Input:
    0

    Sample Output:
    [0, 0, 0, 0]
    """
    nums = [target, 0, 0, 0]
    for i in range(99):
        x = nums[3] - sum(nums[:3])  # x is such that x + nums[:3] == nums[3]
        nums = [x] + nums[:3]
    return nums
# assert sat99(sol99())

