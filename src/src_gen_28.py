from typing import List

def sat280(x: List[int], t=677, a=43, e=125, s=10):
    non_zero = [z for z in x if z != 0]
    return t == sum([x[i] for i in range(a, e, s)]) and len(set(non_zero)) == len(non_zero) and all(
        [x[i] != 0 for i in range(a, e, s)])
def sol280(t=677, a=43, e=125, s=10):
    """Sum values of sublist by range specifications"""
    x = [0] * e
    for i in range(a, e, s):
        x[i] = i
    correction = t - sum(x) + x[i]
    if correction in x:
        x[correction] = -1 * correction
        x[i] = 3 * correction
    else:
        x[i] = correction
    return x
# assert sat280(sol280())

def sat281(x: List[int], t=50, n=10):
    assert all([v > 0 for v in x])
    s = 0
    i = 0
    for v in sorted(x):
        s += v
        if s > t:
            return i == n
        i += 1
    return i == n
def sol281(t=50, n=10):
    """Find how many values have cumulative sum less than target"""
    return [1] * n + [t]
# assert sat281(sol281())

def sat282(s: str, s1="a", s2="b", count1=50, count2=30):
    return s.count(s1) == count1 and s.count(s2) == count2 and s[:10] == s[-10:]
def sol282(s1="a", s2="b", count1=50, count2=30):
    """
    Find a string that has count1 occurrences of s1 and count2 occurrences of s2 and starts and ends with
    the same 10 characters
    """
    if s1 == s2:
        ans = (s1 + "?") * count1
    elif s1.count(s2):
        ans = (s1 + "?") * count1
        ans += (s2 + "?") * (count2 - ans.count(s2))
    else:
        ans = (s2 + "?") * count2
        ans += (s1 + "?") * (count1 - ans.count(s1))
    return "?" * 10 + ans + "?" * 10
# assert sat282(sol282())

def sat283(s: str, substrings=['foo', 'bar', 'baz', 'oddball']):
    return all(sub in s[i::len(substrings)] for i, sub in enumerate(substrings))
def sol283(substrings=['foo', 'bar', 'baz', 'oddball']):
    """
    Find a string that contains each string in substrings alternating, e.g., 'cdaotg' for 'cat' and 'dog'
    """
    m = max(len(s) for s in substrings)
    return "".join([(s[i] if i < len(s) else " ") for i in range(m) for s in substrings])
# assert sat283(sol283())

def sat284(s: str, substrings=['foo', 'bar', 'baz']):
    return all(sub in s and sub[::-1] in s for sub in substrings)
def sol284(substrings=['foo', 'bar', 'baz']):
    """
    Find a string that contains all the substrings reversed and forward
    """
    return "".join(substrings + [s[::-1] for s in substrings])
# assert sat284(sol284())

def sat285(ls: List[str], n=100, a="bar", b="foo"):
    return len(ls) == len(set(ls)) == n and ls[0] == a and ls[-1] == b and ls == sorted(ls)
def sol285(n=100, a="bar", b="foo"):
    """
    Find a list of n strings, in alphabetical order, starting with a and ending with b.
    """
    return sorted([a] + [a + chr(0) + str(i) for i in range(n - 2)] + [b])
# assert sat285(sol285())

def sat286(s: str, strings=['cat', 'dog', 'bird', 'fly', 'moose']):
    return s in strings and sum(t > s for t in strings) == 1
def sol286(strings=['cat', 'dog', 'bird', 'fly', 'moose']):
    """Find the alphabetically second to last last string in a list."""
    return sorted(strings)[-2]
# assert sat286(sol286())

def sat287(s: str, strings=['cat', 'dog', 'bird', 'fly', 'moose']):
    return s[::-1] in strings and sum(t < s[::-1] for t in strings) == 1
def sol287(strings=['cat', 'dog', 'bird', 'fly', 'moose']):
    """Find the reversed version of the alphabetically second string in a list."""
    return sorted(strings)[1][::-1]
# assert sat287(sol287())

def sat288(s: str, target="foobarbazwow", length=6):
    return target[(len(target) - length) // 2:(len(target) + length) // 2] == s
def sol288(target="foobarbazwow", length=6):
    """Find a substring of the given length centered within the target string."""
    return target[(len(target) - length) // 2:(len(target) + length) // 2]
# assert sat288(sol288())

def sat289(substring: str, string="moooboooofasd", count=2):
    return string.count(substring) == count
def sol289(string="moooboooofasd", count=2):
    """Find a substring with a certain count in a given string"""
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            substring = string[i:j]
            c = string.count(substring)
            if c == count:
                return substring
            if c < count:
                break
    assert False
# assert sat289(sol289())

