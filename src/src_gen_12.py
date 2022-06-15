from typing import List

def sat120(bananas: int, bowl="5024 apples and 12189 oranges", total=12491241):
    bowl += f" and {bananas} bananas"
    return sum([int(s) for s in bowl.split() if s.isdigit()]) == total
def sol120(bowl="5024 apples and 12189 oranges", total=12491241):
    """
    Determine how many bananas are necessary to reach a certain total amount of fruit

    bowl="3 apples and 4 oranges", total=12 => 5
    """
    apples, oranges = [int(s) for s in bowl.split() if s.isdigit()]
    return total - apples - oranges
# assert sat120(sol120())

def sat121(val_index: List[int], nums=[125123, 422323, 141, 5325, 812152, 9, 42145, 5313, 421, 812152]):
    if val_index == []:
        return all(n % 2 == 1 for n in nums)
    v, i = val_index
    assert v % 2 == 0 and nums[i] == v
    return all(n > v or n % 2 == 1 for n in nums[:i]) and all(n >= v or n % 2 == 1 for n in nums[i:])
def sol121(nums=[125123, 422323, 141, 5325, 812152, 9, 42145, 5313, 421, 812152]):
    """
    Given an array of nums representing a branch on a binary tree, find the minimum even value and its index.
    In the case of a tie, return the smallest index. If there are no even numbers, the answer is [].

    Sample Input:
    [1, 7, 4, 6, 10, 11, 14]

    Sample Output:
    [4, 2]
    """
    if any(n % 2 == 0 for n in nums):
        return min([v, i] for i, v in enumerate(nums) if v % 2 == 0)
    else:
        return []
# assert sat121(sol121())

def sat122(h: int, seq=[3, 1, 4, 17, 5, 17, 2, 1, 41, 32, 2, 5, 5, 5, 5]):
    for i in seq:
        assert not (i > 0 and i > h and seq.count(i) >= i)
    return h == -1 or seq.count(h) >= h > 0
def sol122(seq=[3, 1, 4, 17, 5, 17, 2, 1, 41, 32, 2, 5, 5, 5, 5]):
    """
    Find the h-index, the largest positive number h such that that h occurs in the sequence at least h times.
    h = -1 if there is no such positive number.

    Sample Input:
    [1, 2, 2, 3, 3, 3, 4, 4]

    Sample Output:
    3
    """
    return max([-1] + [i for i in seq if i > 0 and seq.count(i) >= i])
# assert sat122(sol122())

def sat123(strange: List[int], li=[30, 12, 42, 717, 45, 317, 200, -1, 491, 32, 15]):
    assert sorted(strange) == sorted(li), "Must be a permutation"
    return all(n == (min, max)[i % 2](strange[i:]) for i, n in enumerate(strange))
def sol123(li=[30, 12, 42, 717, 45, 317, 200, -1, 491, 32, 15]):
    """
    Find the following strange sort of li: the first element is the smallest, the second is the largest of the
    remaining, the third is the smallest of the remaining, the fourth is the smallest of the remaining, etc.

    Sample Input:
    [1, 2, 7, 3, 4, 5, 6]

    Sample Output:
    [1, 7, 2, 6, 3, 5, 4]
    """
    s = sorted(li)
    i = 0
    j = len(li) - 1
    ans = []
    while i <= j:
        if len(ans) % 2:
            ans.append(s[j])
            j -= 1
        else:
            ans.append(s[i])
            i += 1
    return ans
# assert sat123(sol123())

def sat124(coords: List[List[float]], sides=[8.9, 10.8, 17.0]):
    assert len(coords) == 3
    sides2 = [((x - x2) ** 2 + (y - y2) ** 2) ** 0.5 for i, (x, y) in enumerate(coords) for x2, y2 in coords[:i]]
    return all(abs(a - b) < 1e-6 for a, b in zip(sorted(sides), sorted(sides2)))
def sol124(sides=[8.9, 10.8, 17.0]):
    """
    Find the coordinates of a triangle with the given side lengths

    Sample Input:
    [3.0, 4.0, 5.0

    Sample Output:
    [[0.0, 0.0], [3.0, 0.0], [0.0, 4.0]]
    """
    a, b, c = sorted(sides)

    s = sum(sides) / 2  # semi-perimeter
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Heron's formula

    y = 2 * area / a  # height
    x = (c ** 2 - y ** 2) ** 0.5
    return [[0.0, 0.0], [a, 0.0], [x, y]]
# assert sat124(sol124())

def sat125(problem: int, weights=[1, 2, 5, 2, 1, 17], max_weight=100):
    if problem == -1:
        return sum(weights) > max_weight
    return weights[problem] != weights[- 1 - problem]
def sol125(weights=[1, 2, 5, 2, 1, 17], max_weight=100):
    """
    An object will "fly" if its weights are a palindrome and sum to <= max_weight. The given object won't fly.
    You have to determine why. Find index where the weights aren't a palindrome or -1 if weights are too big.

    weights=[77, 40], max_weight=100 => -1

    weights=[1,2,3], max_weight=50   => 0 # because 1 != 3
    """
    if sum(weights) > max_weight:
        return -1
    return next(i for i, w in enumerate(weights) if weights[-i - 1] != weights[i])
# assert sat125(sol125())

def sat126(pal: str, s="palindromordinals"):
    assert pal == pal[::-1] and len(pal) == len(s)
    return sum(a != b for a, b in zip(pal, s)) == sum(a != b for a, b in zip(s, s[::-1])) // 2
def sol126(s="palindromordinals"):
    """
    Find the closest palindrome

    Sample Input:
    "cat"

    Sample Output:
    "tat"
    """
    n = len(s)
    return s[:(n + 1) // 2] + s[:n // 2][::-1]
# assert sat126(sol126())

def sat127(li: List[str], lists=[['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]):
    width = sum(len(s) for s in li)
    for li2 in lists:
        assert width <= sum(len(s) for s in li2)
    return li in lists
def sol127(lists=[['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]):
    """
    Find the list that has fewer total characters (including repetitions)

    Sample Input:
    [["sh", "ort"], ["longest"]]

    Sample Output:
    [["sh", "ort"]
    """
    return min(lists, key=lambda x: sum(len(i) for i in x))
# assert sat127(sol127())

def sat128(factors: List[List[int]]):
    primes = set(range(2, 1000))
    for n in range(2, 1000):
        if n in primes:
            primes.difference_update(range(2 * n, 1000, n))
    assert all(p in primes for f in factors for p in f), "all factors must be prime"
    nums = {p * q * r for p, q, r in factors}
    return max(nums) < 1000 and len(nums) == 247
def sol128():
    """
    Find all 247 integers <= 1000 that are the product of exactly three primes.
    Each integer should represented as the list of its three prime factors.
    [[2, 2, 2], [2, 2, 3],  [2, 2, 5], ...
    """
    primes = set(range(2, 1000))
    for n in range(2, 1000):
        if n in primes:
            primes.difference_update(range(2 * n, 1000, n))
    return [[p, q, r] for p in primes for q in primes if p <= q for r in primes if q <= r and p * q * r < 1000]
# assert sat128(sol128())

def sat129(x: int, a=3, n=1290070078170102666248196035845070394933441741644993085810116441344597492642263849):
    return a ** x == n
def sol129(a=3, n=1290070078170102666248196035845070394933441741644993085810116441344597492642263849):
    """Find an integer exponent x such that a^x = n
    Sample Input:
    a=2, n=1024

    Sample Output:
    x = 10
    """
    m = 1
    x = 0
    while m != n:
        x += 1
        m *= a
    return x
# assert sat129(sol129())

