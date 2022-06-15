from typing import List

def sat320(states: List[List[int]], n=16385):
    assert states[0] == [1] * 5 and all(len(li) == 5 for li in states) and all(i >= 0 for li in states for i in li)
    for prev, cur in zip(states, states[1:]):
        for i in range(5):
            if cur[i] != prev[i]:
                break
        assert cur[i] < prev[i]
        assert (
                cur[i + 1] - prev[i + 1] == 2 * (prev[i] - cur[i]) and cur[i + 2:] == prev[i + 2:]  # k decrements
                or
                cur[i:i + 3] == [prev[i] - 1, prev[i + 2], prev[i + 1]] and cur[i + 3:] == prev[i + 3:]  # swap
        )

    return states[-1][-1] == 2 ** n
def sol320(n=16385):
    """
    There are five boxes each having one coin initially. Two types of moves are allowed:
    * (advance) remove `k > 0` coins from box `i` and add `2k` coins to box `i + 1`
    * (swap) remove a coin from box `i` and swap the contents of boxes `i+1` and `i+2`
    Given `0 <= n <= 16385`, find a sequence of states that result in 2^n coins in the last box.
    Note that `n` can be as large as 16385 yielding 2^16385 coins (a number with 4,933 digits) in the last
    box. Encode each state as a list of the numbers of coins in the five boxes.

    Sample Input:
    `n = 2`

    Sample Output:
    `[[1, 1, 1, 1, 1], [0, 3, 1, 1, 1], [0, 1, 5, 1, 1], [0, 1, 4, 1, 1], [0, 0, 1, 4, 1], [0, 0, 0, 1, 4]]`

    The last box now has 2^2 coins. This is a sequence of two advances followed by three swaps.

    states is encoded by lists of 5 coin counts
    """
    assert n >= 1
    ans = [[1] * 5, [0, 3, 1, 1, 1], [0, 2, 3, 1, 1], [0, 2, 2, 3, 1], [0, 2, 2, 0, 7], [0, 2, 1, 7, 0],
           [0, 2, 1, 0, 14], [0, 2, 0, 14, 0], [0, 1, 14, 0, 0]]

    def exp_move():  # shifts last 3 [..., a, 0, 0] to [..., 0, 2^a, 0] for a>0
        state = ans[-1][:]
        state[2] -= 1
        state[3] += 2
        ans.append(state[:])
        while state[2]:
            state[3], state[4] = 0, 2 * state[3]
            ans.append(state[:])
            state[2:] = [state[2] - 1, state[4], 0]
            ans.append(state[:])

    exp_move()
    assert ans[-1] == [0, 1, 0, 2 ** 14, 0]
    ans.append([0, 0, 2 ** 14, 0, 0])
    if n <= 16:
        ans.append([0, 0, 0, 2 ** 15, 0])
    else:
        exp_move()
        assert ans[-1] == [0, 0, 0, 2 ** (2 ** 14), 0]
    state = ans[-1][:]
    state[-2] -= 2 ** (n - 1)
    state[-1] = 2 ** n
    ans.append(state)
    return ans
# assert sat320(sol320())

def sat321(nums: List[int], b=7, m=6):
    assert len(nums) == len(set(nums)) == m and min(nums) >= 0

    def gcd(i, j):
        r, s = max(i, j), min(i, j)
        while s >= 1:
            r, s = s, (r % s)
        return r

    for a in nums:
        nums = [(a + i + 1) ** 2 + (a + i + 1) + 1 for i in range(b)]
        assert all(any(i != j and gcd(i, j) > 1 for j in nums) for i in nums)

    return True
def sol321(b=7, m=6):
    """
    Let P(n) = n^2 + n + 1.

    Given b>=6 and m>=1, find m non-negative integers for which the set {P(a+1), P(a+2), ..., P(a+b)} has
    the property that there is no element that is relatively prime to every other element.

    Sample input:
    b = 6
    m = 2

    Sample output:
    [195, 196]
    """
    ans = []

    seen = set()
    deltas = set()

    def go(a):
        if a < 0 or a in seen or len(ans) == m:
            return
        seen.add(a)
        nums = [(a + i + 1) ** 2 + (a + i + 1) + 1 for i in range(b)]
        if all(any(i != j and gcd(i, j) > 1 for j in nums) for i in nums):
            new_deltas = [abs(a - a2) for a2 in ans if a != a2 and abs(a - a2) not in deltas]
            ans.append(a)
            for delta in new_deltas:
                for a2 in ans:
                    go(a2 + delta)
                    go(a2 - delta)
            deltas.update(new_deltas)
            for delta in sorted(deltas):
                go(a + delta)

    def gcd(i, j):
        r, s = max(i, j), min(i, j)
        while s >= 1:
            r, s = s, (r % s)
        return r

    a = 0

    while len(ans) < m:
        go(a)
        a += 1

    return ans
# assert sat321(sol321())

def sat322(indices: List[int], a0=123):
    assert a0 >= 0 and a0 % 3 == 0, "Hint: a_0 is a multiple of 3."
    s = [a0]
    for i in range(max(indices)):
        s.append(int(s[-1] ** 0.5) if int(s[-1] ** 0.5) ** 2 == s[-1] else s[-1] + 3)
    return len(indices) == len(set(indices)) == 1000 and min(indices) >= 0 and len({s[i] for i in indices}) == 1
def sol322(a0=123):
    """
    Find a repeating integer in an infinite sequence of integers, specifically the indices for which the same value
    occurs 1000 times. The sequence is defined by a starting value a_0 and each subsequent term is:
    a_{n+1} = the square root of a_n if the a_n is a perfect square, and a_n + 3 otherwise.

    For a given a_0 (that is a multiple of 3), the goal is to find 1000 indices where the a_i's are all equal.

    Sample input:
    9

    Sample output:
    [0, 3, 6, ..., 2997]

    The sequence starting with a0=9 is [9, 3, 6, 9, 3, 6, 9, ...] thus a_n at where n is a multiple of 3 are
    all equal in this case.
    """
    n = a0
    ans = []
    i = 0
    while len(ans) < 1000:
        if n == 3:  # use the fact that 3 will repeat infinitely often
            ans.append(i)
        n = int(n ** 0.5) if int(n ** 0.5) ** 2 == n else n + 3
        i += 1
    return ans
# assert sat322(sol322())

def sat323(keep: List[bool], heights=[10, 2, 14, 1, 8, 19, 16, 6, 12, 3, 17, 0, 9, 18, 5, 7, 11, 13, 15, 4]):
    n = int(len(heights) ** 0.5)
    assert sorted(heights) == list(range(n * n + n)), "hint: heights is a permutation of range(n * n + n)"
    kept = [i for i, k in zip(heights, keep) if k]
    assert len(kept) == 2 * n, "must keep 2n items"
    pi = sorted(range(2 * n), key=lambda i: kept[i])  # the sort indices
    return all(abs(pi[2 * i] - pi[2 * i + 1]) == 1 for i in range(n))
def sol323(heights=[10, 2, 14, 1, 8, 19, 16, 6, 12, 3, 17, 0, 9, 18, 5, 7, 11, 13, 15, 4]):
    """
    Given a permutation of the integers up to n(n+1) as a list, choose 2n numbers to keep (in the same order)
    so that the remaining list of numbers satisfies:
    * its largest number is next to its second largest number
    * its third largest number is next to its fourth largest number
    ...
    * its second smallest number is next to its smallest number

    Sample input:
    [4, 0, 5, 3, 1, 2]
    n = 2

    Sample output:
    [True, False, True, False, True, True]

    Keeping these indices results in the sublist [4, 5, 1, 2] where 4 and 5 are adjacent as are 1 and 2.
    """
    # Based on the judge's solution.
    n = int(len(heights) ** 0.5)
    assert sorted(heights) == list(range(n * (n + 1)))
    groups = [h // (n + 1) for h in heights]
    ans = [False] * len(heights)
    a = 0
    used_groups = set()
    while sum(ans) < 2 * n:
        group_tracker = {}
        b = a
        while groups[b] not in group_tracker or groups[b] in used_groups:
            group_tracker[groups[b]] = b
            b += 1
        ans[group_tracker[groups[b]]] = True
        ans[b] = True
        used_groups.add(groups[b])
        a = b + 1
    return ans
# assert sat323(sol323())

def sat324(li: List[int], n=18):
    assert n % 3 == 0, "Hint: n is a multiple of 3"
    return len(li) == n and all(li[(i + 2) % n] == 1 + li[(i + 1) % n] * li[i] for i in range(n))
def sol324(n=18):
    """
    Given n, find n integers such that li[i] * li[i+1] + 1 == li[i+2], for i = 0, 1, ..., n-1
    where indices >= n "wrap around". Note: only n multiples of 3 are given since this is only possible for n
    that are multiples of 3 (as proven in the IMO problem).

    Sample input:
    6

    Sample output:
    [_, _, _, _, _, _]

    (Sample output hidden because showing sample output would give away too much information.)
    """
    return [-1, -1, 2] * (n // 3)
# assert sat324(sol324())

def sat325(li: List[int], tags=[3, 0, 3, 2, 0, 1, 0, 3, 1, 1, 2, 2, 0, 2, 1, 3]):
    n = max(tags) + 1
    assert sorted(tags) == sorted(list(range(n)) * 4), "hint: each tag occurs exactly four times"
    assert len(li) == len(set(li)) and min(li) >= 0
    return sum(li) * 2 == sum(range(4 * n)) and sorted([tags[i] for i in li]) == [i // 2 for i in range(2 * n)]
def sol325(tags=[3, 0, 3, 2, 0, 1, 0, 3, 1, 1, 2, 2, 0, 2, 1, 3]):
    """
    The input tags is a list of 4n integer tags each in range(n) with each tag occurring 4 times.
    The goal is to find a subset (list) li of half the indices such that:
    * The sum of the indices equals the sum of the sum of the missing indices.
    * The tags of the chosen indices contains exactly each number in range(n) twice.

    Sample input:
    n = 3
    tags = [0, 1, 2, 0, 0, 1, 1, 1, 2, 2, 0, 2]

    Sample output:
    [0, 3, 5, 6, 8, 11]

    Note the sum of the output is 33 = (0+1+2+...+11)/2 and the selected tags are [0, 0, 1, 1, 2, 2]
    """
    n = max(tags) + 1
    pairs = {(i, 4 * n - i - 1) for i in range(2 * n)}
    by_tag = {tag: [] for tag in range(n)}
    for p in pairs:
        a, b = [tags[i] for i in p]
        by_tag[a].append(p)
        by_tag[b].append(p)
    cycles = []
    cycle = []
    while pairs:
        if not cycle:  # start new cycle
            p = pairs.pop()
            pairs.add(p)  # just to pick a tag
            tag = tags[p[0]]
            # print("Starting cycle with tag", tag)
        p = by_tag[tag].pop()
        a, b = [tags[i] for i in p]
        # print(p, a, b)
        tag = a if a != tag else b
        by_tag[tag].remove(p)
        cycle.append(p if tag == b else p[::-1])
        pairs.remove(p)
        if not by_tag[tag]:
            cycles.append(cycle)
            cycle = []

    while any(len(c) % 2 for c in cycles):
        cycle_tags = [{tags[k] for p in c for k in p} for c in cycles]
        merged = False
        for i in range(len(cycles)):
            for j in range(i):
                intersection = cycle_tags[i].intersection(cycle_tags[j])
                if intersection:
                    c = intersection.pop()
                    # print(f"Merging cycle {i} and cycle {j} at tag {c}", cycles)
                    cycle_i = cycles.pop(i)
                    for i1, p in enumerate(cycle_i):
                        if tags[p[0]] == c:
                            break
                    for j1, p in enumerate(cycles[j]):
                        if tags[p[0]] == c:
                            break
                    cycles[j][j1:j1] = cycle_i[i1:] + cycle_i[:i1]
                    merged = True
                    break
            if merged:
                break

    ans = []
    for c in cycles:
        for i, p in enumerate(c):
            if i % 2:
                ans += p

    return ans
# assert sat325(sol325())

def sat326(inds: List[int], vecs=[169, 203, 409, 50, 37, 479, 370, 133, 53, 159, 161, 367, 474, 107, 82, 447, 385]):
    return all(sum((v >> i) & 1 for i in inds) % 2 == 1 for v in vecs)
def sol326(vecs=[169, 203, 409, 50, 37, 479, 370, 133, 53, 159, 161, 367, 474, 107, 82, 447, 385]):
    """
    Parity learning: Given binary vectors in a subspace, find the secret set S of indices such that:
    $sum_{i in S} x_i = 1 (mod 2)$
    """
    # Gaussian elimination
    d = 0  # decode vectors into arrays
    m = max(vecs)
    while m:
        m >>= 1
        d += 1
    vecs = [[(n >> i) & 1 for i in range(d)] for n in vecs]
    ans = []
    pool = [[0] * (d + 1) for _ in range(d)] + [v + [1] for v in vecs]
    for i in range(d):
        pool[i][i] = 1

    for i in range(d):  # zero out bit i
        for v in pool[d:]:
            if v[i] == 1:
                break
        if v[i] == 0:
            v = pool[i]
        assert v[i] == 1  # found a vector with v[i] = 1, subtract it off from those with a 1 in the ith coordinate
        w = v[:]
        for v in pool:
            if v[i] == 1:
                for j in range(d + 1):
                    v[j] ^= w[j]

    return [i for i in range(d) if pool[i][-1]]
# assert sat326(sol326())

def sat327(inds: List[int], vecs=[26, 5, 32, 3, 15, 18, 31, 13, 24, 25, 34, 5, 15, 24, 16, 13, 0, 27, 37]):
    return sum(sum((v >> i) & 1 for i in inds) % 2 for v in vecs) >= len(vecs) * 3 / 4
def sol327(vecs=[26, 5, 32, 3, 15, 18, 31, 13, 24, 25, 34, 5, 15, 24, 16, 13, 0, 27, 37]):
    """
    Learning parity with noise: Given binary vectors, find the secret set $S$ of indices such that, for at least
    3/4 of the vectors, $$sum_{i in S} x_i = 1 (mod 2)$$
    """
    # brute force
    d = 0  # decode vectors into arrays
    m = max(vecs)
    while m:
        m >>= 1
        d += 1
    vecs = [[(n >> i) & 1 for i in range(d)] for n in vecs]

    import random
    rand = random.Random(0)
    target = (len(vecs) * 3) // 4
    max_attempts = 10 ** 5
    for _ in range(max_attempts):
        ans = [i for i in range(d) if rand.randrange(2)]
        if sum(sum(v[i] for i in ans) % 2 for v in vecs) >= len(vecs) * 3 / 4:
            return ans
# assert sat327(sol327())

def sat328(n: int, a=15482, b=23223, lower_bound=5):
    return a % n == 0 and b % n == 0 and n >= lower_bound
def sol328(a=15482, b=23223, lower_bound=5):
    """Find a large common divisor of two integers."""
    m, n = min(a, b), max(a, b)
    while m > 0:
        m, n = n % m, m
    return n
# assert sat328(sol328())

def sat329(n: int, nums=[77410, 23223, 54187], lower_bound=2):
    return all(i % n == 0 for i in nums) and n >= lower_bound
def sol329(nums=[77410, 23223, 54187], lower_bound=2):
    """Find a large common divisor of the list of integers."""
    n = 0
    for i in nums:
        m, n = min(i, n), max(i, n)
        while m > 0:
            m, n = n % m, m
    return n
# assert sat329(sol329())

