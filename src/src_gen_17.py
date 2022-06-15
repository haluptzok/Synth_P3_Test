from typing import List

def sat170(words: List[str], s="This is not a very hard puzzle", n=3):
    i = 0
    for w in s.split():
        num_consonants = 0
        for c in w.lower():
            if c not in "aeiou":
                num_consonants += 1
        if num_consonants == n:
            if words[i] != w:
                return False
            i += 1
    return i == len(words)
def sol170(s="This is not a very hard puzzle", n=3):
    """Find all words in the string with n consonants

    Sample input:
    s="An eye for an I", n=1
    Sample output:
    ["An", "eye", "an"]
    """
    return [w for w in s.split() if sum(c.lower() not in "aeiou" for c in w) == n]
# assert sat170(sol170())

def sat171(ham: str, s="Any vowel is OK"):
    vows = "aeiou"
    cons = "bcdfghjklmnpqrstvwxz"
    return ham in s and ham[0].lower() in cons and ham[1].lower() in vows and ham[2].lower() in cons
def sol171(s="Any vowel is OK"):
    """Find any vowel sandwich, a string consisting of a vowel between two consonants, contained in s

    "sandwhich" => "hic"
    """
    vows = "aeiou"
    cons = "bcdfghjklmnpqrstvwxz"
    return next(s[i - 1:i + 2] for i in range(1, len(s) - 1)
                if s[i].lower() in vows and s[i - 1].lower() in cons and s[i + 1].lower() in cons)
# assert sat171(sol171())

def sat172(perm: str, s="))(  )()()() )))(( ))))((( )))))(((( ))))))))((((((( ))))))((((( )))))))(((((( )))))))))(((((((  (((((((((("):
    assert sorted(perm.split()) == sorted(s.split()), "Must be a permutation of the space-delimited 'groups'"
    return all(perm[:i].count("(") >= perm[:i].count(")") for i in range(len(perm)))
def sol172(s="))(  )()()() )))(( ))))((( )))))(((( ))))))))((((((( ))))))((((( )))))))(((((( )))))))))(((((((  (((((((((("):
    """The string s consists of groups of parentheses separated by spaces.
    Permute the groups such that the parentheses match.

    "( ) )(" => "( )( )"
    """
    assert all(c in "( )" for c in s)
    parts = s.split()

    def min_depth(part):
        """Returns the lowest depth <= 0"""
        ans = 0
        depth = 0
        for c in part:
            if c == ")":
                depth -= 1
                ans = min(ans, depth)
            else:
                depth += 1
        return ans

    def greedy_reorder(subs):
        """Reorder a bunch of parentheses substrings so as to maintain # ('s > # )'s """
        queue = subs[:]
        subs[:] = []
        height = 0
        while queue:
            best = max([s for s in queue if min_depth(s) + height >= 0], key=lambda s: s.count("(") - s.count(")"))
            height += best.count("(") - best.count(")")
            subs.append(best)
            queue.remove(best)

    lefts = [s for s in parts if s.count("(") >= s.count(")")]

    greedy_reorder(lefts)

    def mirror(sub):
        return "".join(")" if c == "(" else "(" for c in sub[::-1])

    rights = [mirror(s) for s in parts if s.count("(") < s.count(")")]  # mirror temporarily for reordering

    greedy_reorder(rights)
    return " ".join(lefts + [mirror(s) for s in rights[::-1]])
# assert sat172(sol172())

def sat173(biggest: List[int], k=7, nums=[31, 1, 2, -10, -2, 4, 17, 18, 20, 14, 20, 21, 18, 0]):
    if len(biggest) != k:
        return False
    smallest = nums[:]
    for n in biggest:
        smallest.remove(n)
    return k == 0 or k == len(nums) or max(smallest) <= min(biggest)
def sol173(k=7, nums=[31, 1, 2, -10, -2, 4, 17, 18, 20, 14, 20, 21, 18, 0]):
    """Find the largest k numbers

    k=2, [1, 2, 3, 4, 5, 5, 3, 5, 2] => [5, 5]
    """
    return sorted(nums, reverse=True)[:k]
# assert sat173(sol173())

def sat174(tot: int, nums=[18, 42152, 125023521, -1221873620123, 17, 19]):
    for i in nums[::2]:
        if i % 2 == 1:
            tot -= i
    return tot == 0
def sol174(nums=[18, 42152, 125023521, -1221873620123, 17, 19]):
    """Find the sum of the odd elements that are at even indices

    [0, 1, 2, 3, 5, 6] => 5
    """
    return sum(i for i in nums[::2] if i % 2 == 1)
# assert sat174(sol174())

def sat175(tot: int, k=5, nums=[1252, 125273523, 0, 42, 100, 214532, 2, 0, 11, 14]):
    for n in nums[:k]:
        if len(str(abs(n))) > 2:
            tot -= n
    return tot == 0
def sol175(k=5, nums=[1252, 125273523, 0, 42, 100, 214532, 2, 0, 11, 14]):
    """Find the sum of the numbers among the first k with more than 2 digits

    k=3, nums=[2, 102, 12, 1000] => 102
    """
    return sum(n for n in nums[:k] if len(str(abs(n))) > 2)
# assert sat175(sol175())

def sat176(odds: List[int], n=1243272912731):
    num_odds = 0
    while True:
        if n % 2 == 1:
            num_odds += 1
            if n not in odds:
                return False
        if n <= 1:
            return num_odds == len(odds)
        n = (3 * n + 1) if n % 2 == 1 else n // 2
def sol176(n=1243272912731):
    """Find the odd numbers in the collatz sequence starting at n

    3 => [3, 5, 1]  # because the Collatz sequence starting with 3 is [3, 10, 5, 16, 8, 4, 2, 1]
    """
    ans = []
    while True:
        if n % 2 == 1:
            ans.append(n)
        if n <= 1:
            return ans
        n = (3 * n + 1) if n % 2 == 1 else n // 2
# assert sat176(sol176())

def sat177(s: str, target=-2075):
    assert all(c in "0123457689-" for c in s) and s[2] == s[5] == "-"
    m, d, y = [int(n) for n in s.split("-")]
    assert m in range(1, 13)
    assert d in range(1, 32)
    if m in [4, 6, 9, 11]:
        assert d <= 30
    if m == 2:
        assert d <= 29
    return m - d - y == target
def sol177(target=-2075):
    """Find a valid date mm-dd-yyyy such that the date, viewed as a mathematical expression, evaluates to target

    -2029 => "10-18-2021" # because 10-18-2021 == -2029
    """
    if target >= -30:
        return "12-01-" + str(11 - target).zfill(4)
    return "01-31-" + str(-30 - target).zfill(4)
# assert sat177(sol177())

def sat178(lst: List[str], s="Hello, world!"):
    if " " in s:
        return " ".join(lst) == s
    if "," in s:
        return ",".join(lst) == s
    return "".join(lst) == "".join(c for c in s if c.islower() and ord(c) % 2 == 0)
def sol178(s="Hello, world!"):
    """Split s into strings if there is a space in s, otherwise split on commas if there is a comma, otherwise
    return the list of lowercase letters with odd order (order of a = 0, b = 1, etc.)

    "a b c" => ["a", "b", "c"]
    "a,b" => ["a", "b"]
    """
    if " " in s:
        return s.split(" ")
    if "," in s:
        return s.split(",")
    return [c for c in s if c.islower() and ord(c) % 2 == 0]
# assert sat178(sol178())

def sat179(violation: List[int], nums=[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 17, 17, 18, 19, 20, 22, 24]):
    if not violation:
        return all(nums[i] < nums[i + 1] for i in range(len(nums) - 1))
    i, j = violation
    return 0 <= i < j and nums[i] >= nums[j]
def sol179(nums=[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 17, 17, 18, 19, 20, 22, 24]):
    """
    Find the indices of two entries that show that the list is not in increasing order.
    If there are no violations (they are increasing), return an empty list.

    [1,2,3,0,4,5,6] => [1, 3]
    """
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            return [i, i + 1]
    return []
# assert sat179(sol179())

