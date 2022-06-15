from typing import List

def sat140(indices: List[List[int]], uneven=[[1, 3, 2, 32, 17], [17, 2, 48, 17], [], [9, 35, 4], [3, 17]], target=17):
    for i, j in indices:
        assert uneven[i][j] == target
    for i, row in enumerate(uneven):
        for j, n in enumerate(row):
            assert n != target or [i, j] in indices
    return True
def sol140(uneven=[[1, 3, 2, 32, 17], [17, 2, 48, 17], [], [9, 35, 4], [3, 17]], target=17):
    """Find the indices of all occurrences of target in the uneven matrix
    Sample input:
    uneven=[[2, 3, 2], [], [9, 2]], target=2

    Sample output:
    [[0, 0], [0, 2], [2, 1]]
    """
    return [[i, j] for i, row in enumerate(uneven) for j, n in enumerate(row) if n == target]
# assert sat140(sol140())

def sat141(up_down: List[int], nums=[17, 2, 3, 523, 18, -2, 0, 2, -1]):
    assert all(up_down.count(i) == nums.count(i) for i in set(up_down + nums)), "not a reordering"
    increasing_sign = 1 if ((nums[0] + nums[-1]) % 2 == 1) else -1
    return all((up_down[i + 1] - up_down[i]) * increasing_sign >= 0 for i in range(len(up_down) - 1))
def sol141(nums=[17, 2, 3, 523, 18, -2, 0, 2, -1]):
    """Reorder nums in increasing/decreasing order based on whether the first plus last element is even/odd

    Sample input:
    [1, 7, 4]

    Sample output:
    [1, 4, 7] # because 1 + 4 is odd

    Sample input:
    [1, 7, 5]

    Sample output:
    [8, 5, 1] # because 1 + 5 is even
    """
    return sorted(nums, reverse=(False if (nums[0] + nums[-1]) % 2 else True))
# assert sat141(sol141())

def sat142(encrypted: str, orig="Hello, world!"):
    assert len(encrypted) == len(orig)
    return all(chr(ord(a) - 2 * 2) == b for a, b in zip(encrypted, orig))
def sol142(orig="Hello, world!"):
    """Apply a substitution cypher in which each character is advanced by two multiplied by two places.

    'substitution cypher' => 'wyfwxmxyxmsr$g}tliv'
    """
    return "".join(chr(ord(b) + 2 * 2) for b in orig)
# assert sat142(sol142())

def sat143(n: int, nums=[17, -1023589211, -293485382500, 31, -293485382500, 105762, 94328103589]):
    assert n in nums
    return len({i for i in nums if i <= n}) == 2
def sol143(nums=[17, -1023589211, -293485382500, 31, -293485382500, 105762, 94328103589]):
    """Find the second smallest unique number in the list nums.

    Sample input:
    [2, 5, 2, 7, 9]

    Sample output:
    5
    """
    return sorted(set(nums))[1]
# assert sat143(sol143())

def sat144(boring: List[str], text="This is not boring. I am boring! I am sooo tired."):
    sentences = text.replace("!", ".").replace("?", ".").split(".")
    boring_and_exciting = boring + [s for s in sentences if s.split()[:1] != ["I"]]
    return sorted(boring_and_exciting) == sorted(sentences)
def sol144(text="This is not boring. I am boring! I am sooo tired."):
    """A bored sentence starts with the word "I". Find all bored sentences in s. Sentence delimiters are '.!?'

    --- Example input ---
    'I wrote this. You read it? I think I am so cool. In another time, I would be lame.'

    --- Example output ---
    ['I wrote this', ' I think I am so cool']

    """
    return [s for s in text.replace("!", ".").replace("?", ".").split(".") if s.split()[:1] == ["I"]]
# assert sat144(sol144())

def sat145(zero_sums: List[bool], trips=[[1253532, -3920635, 332], [-24, 18, 6], [0, 5, -5], [1, 1, 1], [-20, 17, 4]]):
    return len(zero_sums) == len(trips) and all(z == ((a + b + c) == 0) for z, (a, b, c) in zip(zero_sums, trips))
def sol145(trips=[[1253532, -3920635, 332], [-24, 18, 6], [0, 5, -5], [1, 1, 1], [-20, 17, 4]]):
    """Determine which triples sum to zero

    --- Example input ---
    [1, 2, 4, -3, 5]

    --- Example output ---
    [0, 1, 3]
    """
    return [sum(t) == 0 for t in trips]
# assert sat145(sol145())

def sat146(s: str, target="Hello, world!"):
    subs = {ord(c): ord(c) + 2 for c in "aeiouAEIOU"}
    return s.swapcase() == target.translate(subs)
def sol146(target="Hello, world!"):
    """Find string s that, when case is flipped gives target where vowels are replaced by chars two later.
    --- Example input ---
    'THIS is a TEST'

    --- Example output ---
    'thks KS C tgst'
    """
    subs = {ord(c): ord(c) + 2 for c in "aeiouAEIOU"}
    return target.translate(subs).swapcase()
# assert sat146(sol146())

def sat147(ans: List[int], nums=[23, 17, 201, 14, 10473, 43225, 421, 423, 11, 10, 2022, 342157]):
    i, digit_sum = ans
    n = nums[i]

    def is_prime(n):
        return n > 1 and all(n % j for j in range(2, int(n ** 0.5) + 1))

    return is_prime(n) and all(m <= n for m in nums if is_prime(m)) and digit_sum == sum(int(c) for c in str(n))
def sol147(nums=[23, 17, 201, 14, 10473, 43225, 421, 423, 11, 10, 2022, 342157]):
    """Find the index of the largest prime in the list and the sum of its digits

    --- Example input ---
    [2, 4, 7, 19, 21]

    --- Example output ---
    [3, 10]
    """
    def is_prime(n):
        return n > 1 and all(n % j for j in range(2, int(n ** 0.5) + 1))

    n, i = max((n, i) for i, n in enumerate(nums) if is_prime(n))
    return [i, sum(int(c) for c in str(n))]
# assert sat147(sol147())

def sat148(different: str, d={'cat': 'CAT', 'tree': 'T', 'pick me': 'not', 'OK': 'red', 'blah': 'blah', 'z': 'Z'}):
    return different in d and all(k.islower() != different.islower() for k in d if k != different)
def sol148(d={'cat': 'CAT', 'tree': 'T', 'pick me': 'not', 'OK': 'red', 'blah': 'blah', 'z': 'Z'}):
    """Find the dictionary key whose case is different than all other keys

    --- Example input ---
    {"red": "", "GREEN": "", "blue": "orange"}

    --- Example output ---
    "GREEN"
    """
    for different in d:
        if all(k.islower() != different.islower() for k in d if k != different):
            return different
# assert sat148(sol148())

def sat149(primes: List[int], n=1234):
    assert all(1 < p for p in primes) and all(p % q for p in primes for q in primes if q < p)
    return len({i for p in primes for i in range(p, n, p)}) == max(n - 2, 0)
def sol149(n=1234):
    """Find all primes up to n

    --- Example input ---
    9

    --- Example output ---
    [2, 3, 5, 7]
    """
    primes = []
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            primes.append(i)
            candidates.difference_update(range(i, n, i))
    return primes
# assert sat149(sol149())

