from typing import List

def sat190(x: float, str_nums=['1,3', '-11', '17.5', '-11', '2', '2.2', '2,2', '4', '-18,18', '99.09']):
    found = False
    for s in str_nums:
        y = float(s.replace(",", "."))
        assert y <= x
        if y == x:
            found = True
    return found
def sol190(str_nums=['1,3', '-11', '17.5', '-11', '2', '2.2', '2,2', '4', '-18,18', '99.09']):
    """Find the largest number where commas or periods are decimal points

    ["99,9", "100"] => 100.0
    """
    return max(float(s.replace(",", ".")) for s in str_nums)
# assert sat190(sol190())

def sat191(summands: List[int], n=1234567890):
    return sum(summands) == n and min(summands) > 0 and len(summands) == 4 and all(s % 2 == 0 for s in summands)
def sol191(n=1234567890):
    """Find four positive even integers whose sum is n

    100 => [22, 24, 26, 28]"""
    return [2] * 3 + [n - 6]
# assert sat191(sol191())

def sat192(nums: List[int], super_factorials=[1, 2, 1]):
    for i, sf in enumerate(super_factorials):
        n = nums[i]
        for j in range(n, 0, -1):
            k = j ** (n - j + 1)
            assert sf % k == 0, f"{i} {sf} {j} {n}"
            sf //= k
        assert sf == 1
    return True
def sol192(super_factorials=[1, 2, 1]):
    """The super-factorial of n is n! (n-1)! (n-2)! ... 1!. Invert a given list of super-factorials.

    [1, 2, 2, 12] => [1, 2, 2, 3]
    """
    queue = set(super_factorials)
    cache = {}
    n = 1
    fact = 1
    s_fact = 1
    while queue:
        fact *= n
        s_fact *= fact
        if s_fact in queue:
            queue.remove(s_fact)
            cache[s_fact] = n
        n += 1
    return [cache[sf] for sf in super_factorials]
# assert sat192(sol192())

def sat193(orig: str, target="-Hello,_world!__This_is-so-easy!-"):
    assert "_" not in orig and "-" not in orig
    new = ""
    space_count = 0
    for c in orig:
        if c == " ":
            space_count += 1
        else:
            new += ("-" if space_count > 2 else "_" * space_count)
            new += c
            space_count = 0
    new += ("-" if space_count > 2 else "_" * space_count)
    return new == target
def sol193(target="-Hello,_world!__This_is-so-easy!-"):
    """Find a string such that, when three or more spaces are compacted to a '-' and one or two spaces are
    replaced by underscores, leads to the target.

    "_o-k__?-" => "  o        k  ?     "
    """
    return target.replace("-", " " * 3).replace("_", " ")
# assert sat193(sol193())

def sat194(valids: List[str], filenames=['cat.txt', '!jog.dll', '31F9.html', 'Is this okay?.txt', '.exe', '']):
    assert len(valids) == len(filenames)
    for v, f in zip(valids, filenames):
        n_digits = sum(c.isdigit() for c in f)
        if v == "Yes":
            prefix, ext = f.split(".")
            assert ext in ["txt", "dll", "exe"] and prefix[0].isalpha() and n_digits < 4
        else:
            assert v == "No"
            assert f.split(".")[1:] not in [['txt'], ['dll'], ['exe']] or not f[0].isalpha() or n_digits > 3
    return True
def sol194(filenames=['cat.txt', '!jog.dll', '31F9.html', 'Is this okay?.txt', '.exe', '']):
    """Return a list of Yes/No strings that determine whether candidate filename is valid. A valid filename
    should end in .txt, .exe, or .dll, and should have at most three digits, no additional periods

    ["train.jpg", "doc10234.txt", "3eadme.txt"] = ["No", "No", "Yes"]
    """
    return ["Yes" if
            f.split(".")[1:] in [['txt'], ['dll'], ['exe']] and f[0].isalpha() and sum(c.isdigit() for c in f) < 4
            else "No"
            for f in filenames]
# assert sat194(sol194())

def sat195(lst: List[int], tot=1125181293221):
    return sum(n ** 2 if n % 3 == 0 else n ** 3 if n % 4 == 0 else n for n in lst) == tot
def sol195(tot=1125181293221):
    """Find a list of integers such that tot is the sum of (n^2 if 3 | n, else n^3 if 4 | n, else n)"""
    residue = (tot - 1) % 12
    return [1] * residue + [tot - residue]
# assert sat195(sol195())

def sat196(primes: str, s="This is a test of whether you would want to do such strange puzzles"):

    def is_prime(n):
        return n > 1 and all(n % j for j in range(2, int(n ** 0.5) + 1))

    prime_words = primes.split()
    i = 0
    for word in s.split():
        if is_prime(len(word)):
            assert prime_words[i] == word
            i += 1

    return i == len(prime_words)
def sol196(s="This is a test of whether you would want to do such strange puzzles"):
    """Find the string consisting of all the words whose lengths are prime numbers

    "A bird in the hand is worth two in the bush" => "in the is worth two in the"
    """
    def is_prime(n):
        return n > 1 and all(n % j for j in range(2, int(n ** 0.5) + 1))

    return " ".join(w for w in s.split() if is_prime(len(w)))
# assert sat196(sol196())

def sat197(z: str, x="-8142432/763083", y="66/-13474", max_len=18):
    [[a, b], [c, d], [u, v]] = [[int(n) for n in s.split("/")] for s in [x, y, z]]
    return a * c * v == b * d * u and len(z) <= max_len
def sol197(x="-8142432/763083", y="66/-13474", max_len=18):
    """Write x * y as the shortest equivalent fraction using at most max_len chars

    x="-2/3", y="-3/8", max_len=3 => "1/4"
    """
    [[a, b], [c, d]] = [[int(n) for n in s.split("/")] for s in [x, y]]
    num, den = a * c, b * d
    if num < 0 and den < 0:
        num, den = -num, -den
    if num == 0:
        return "0/1"

    def gcd(a, b):
        a, b = min(a, b), max(a, b)
        if b % a == 0:
            return a
        return gcd(b % a, a)

    d = gcd(abs(num), abs(den))
    return f'{num // d}/{den // d}'
# assert sat197(sol197())

def sat198(ordered: List[int], nums=[1, 0, -1, -100, 10, 14, 235251, 11, 10000, 2000001, -155]):
    digit_sums = [sum(int(c) for c in str(n) if c != "-") for n in ordered]
    return sorted(ordered) == sorted(nums) and digit_sums == sorted(digit_sums)
def sol198(nums=[1, 0, -1, -100, 10, 14, 235251, 11, 10000, 2000001, -155]):
    """Sort the numbers by the sum of their digits

    [17, 21, 0] => [0, 17, 21]
    """
    return sorted(nums, key=lambda n: sum(int(c) for c in str(n) if c != "-"))
# assert sat198(sol198())

def sat199(odds: List[int], nums=[204, 109, 203, 17, 45, 11, 21, 99, 909, 16, -33, 3, 17]):
    assert all(o > 10 and odds.count(o) == nums.count(o) and int(str(o)[i]) % 2 for o in odds for i in [-1, 0])
    return all(n in odds or n <= 10 or int(str(n)[0]) % 2 == 0 or int(str(n)[-1]) % 2 == 0 for n in nums)
def sol199(nums=[204, 109, 203, 17, 45, 11, 21, 99, 909, 16, -33, 3, 17]):
    """Find the numbers that are greater than 10 and have odd first and last digits

    [73, 4, 72] => [73]
    """
    return [n for n in nums if n > 10 and (int(str(n)[0]) * int(str(n)[-1])) % 2]
# assert sat199(sol199())

