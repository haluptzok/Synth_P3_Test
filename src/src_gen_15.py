from typing import List

def sat150(prod: int, nums=[17, 24, 39, 15, 11, 201, 97, 65, 18]):
    if not all(nums):
        return prod == 0
    for n in nums:
        k = abs(n % 10)
        if k == 0:
            return prod == 0
        assert prod % k == 0
        prod //= k
    return prod == 1
def sol150(nums=[17, 24, 39, 15, 11, 201, 97, 65, 18]):
    """Find the product of the units digits in the numbers

    [12, 34] => 8
    """
    prod = 1
    for n in nums:
        prod *= abs(n % 10)
    return prod
# assert sat150(sol150())

def sat151(positions: List[int], s="ThIs is A tEsT, Or *IS* iT?"):
    assert all(s[i] in "AEIOU" for i in positions)
    return all(i in positions or c not in "AEIOU" or i % 2 == 1 for i, c in enumerate(s))
def sol151(s="ThIs is A tEsT, Or *IS* iT?"):
    """Find the positions of all uppercase vowels (not counting Y) in even indices

    "EAT here NOW" => [0, 10]
    """
    return [i for i, c in enumerate(s) if i % 2 == 0 and c in "AEIOU"]
# assert sat151(sol151())

def sat152(n: int, x=329437923.5):
    return abs(n - x) <= 0.5
def sol152(x=329437923.5):
    """Round to nearest integer

    --- input ---
    3.7

    --- output ---
    4
    """
    return round(x)
# assert sat152(sol152())

def sat153(li: List[int], n=909):
    return li[0] == n and len(li) == n and all(b - a == 2 for a, b in zip(li, li[1:]))
def sol153(n=909):
    """We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even
    number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones
    than the previous pile but as few as possible. Return the number of stones in each pile.

    2 => [2, 4]
    """
    return [n + 2 * i for i in range(n)]
# assert sat153(sol153())

def sat154(splits: List[List[str]], string="Hello, world!  You look like you're on turtles."):
    words, separators = splits
    assert len(words) == len(separators) + 1
    merged = []
    for w, s in zip(words, separators + [" "]):
        assert s.count(" ") + s.count(",") == len(s) > 0
        assert w.count(" ") + w.count(",") == 0
        merged += [w, s]
    return "".join(merged[:-1]) == string
def sol154(string="Hello, world!  You look like you're on turtles."):
    """
    Split a string of words separated by commas and spaces into 2 lists: words and separators

    Sample input: "Hi there, Anna"
    Sample output: [["Hi", "there", "Anna"], [" ", ", "]]
    """
    import re
    merged = re.split(r"([ ,]+)", string)
    return [merged[::2], merged[1::2]]
# assert sat154(sol154())

def sat155(x: int, a=145, b=24126846790974):
    if x == -1:
        return all(i % 2 == 1 for i in range(a, b + 1))
    return a <= x <= b and all(i % 2 == 1 for i in range(x + 1, b + 1))
def sol155(a=145, b=24126846790974):
    """Return the biggest even number between a and b inclusive, or -1 if there is no such number

    Example input:
    a=20, b=99

    Example output:
    98
    """
    if a > b or (a == b and a % 2 == 1):
        return -1
    return b if b % 2 == 0 else b - 1
# assert sat155(sol155())

def sat156(s: str, a=-103252, b=10657):
    n = int(s, 2)
    r = range(a, b)
    if len(r) == 0:
        return n == -1
    mu = sum(r) / len(r)
    return abs(mu - n) <= min(abs(mu - n - 1), abs(mu - n + 1))
def sol156(a=-103252, b=10657):
    """Return the average of the numbers a through b rounded to nearest integer, in binary
    (or -1 if there are no such numbers)

    a=4, b=7 => '110' because the mean of 4, 5, 6 is 5 which is 110 in binary
    """
    r = range(a, b)
    if len(r) == 0:
        return "-1"
    return bin(round(sum(r) / len(r)))
# assert sat156(sol156())

def sat157(sub: List[int], nums=[17, 20, -100, 101, 423258, 19949, 0, 20174, 9351773, -11]):
    for i in range(len(sub)):
        n = sub[i]
        assert n == min(sub[i:])
        assert all(int(c) % 2 for c in str(abs(n)))  # all odd digits
        assert sub.count(n) == nums.count(n)

    for n in nums:
        if n not in sub:
            assert any(int(c) % 2 == 0 for c in str(abs(n)))

    return True
def sol157(nums=[17, 20, -100, 101, 423258, 19949, 0, 20174, 9351773, -11]):
    """Find the sublist of numbers with only odd digits in increasing order

    [17, 21, 18, 1, 4] => [1, 17, 21]
    """
    return sorted(n for n in nums if all(int(c) % 2 for c in str(abs(n))))
# assert sat157(sol157())

def sat158(backwards_digits: List[str], nums=[0, 2, 14, -2, 3, 8, 4, 5, 5, 7, 21, 101, 41, 2, 9, 6]):
    digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    li = [digits[s] for s in backwards_digits]
    for i, n in enumerate(li):
        assert n == max(li[i: i + 2])
        assert nums.count(n) == li.count(n)

    return all(n not in range(1, 10) or n in li for n in nums)
def sol158(nums=[0, 2, 14, -2, 3, 8, 4, 5, 5, 7, 21, 101, 41, 2, 9, 6]):
    """Return the single digits in nums sorted backwards and converted to English words

    [2, 3, 4, 5, 17] => ['five', 'four', 'three', 'two']
    """
    digits = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    return [digits[n] for n in sorted(nums, reverse=True) if n in digits]
# assert sat158(sol158())

def sat159(li: List[int], n=100):
    assert len(li) == n
    for i, m in enumerate(li):
        if i < 2:
            assert m == i + 1
        elif i % 2 == 1:
            assert m == li[i - 2] + i + (i + 1)
        else:
            assert m == li[i - 2] * i * (i + 1)
    return True
def sol159(n=100):
    """Output a list of n integers, where the mth entry is m! if m is even or else (1+2+...+m)

    5 => [1, 2, 6, 9, 120]
    """
    ans = []
    for i in range(n):
        if i < 2:
            m = i + 1
        elif i % 2 == 1:
            m = ans[i - 2] + i + (i + 1)
        else:
            m = ans[i - 2] * i * (i + 1)
        ans.append(m)

    return ans
# assert sat159(sol159())

