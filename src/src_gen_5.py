from typing import List

def sat50(moves: List[List[int]], capacities=[8, 5, 3], init=[8, 0, 0], goal=[4, 4, 0]):
    state = init.copy()

    for [i, j] in moves:
        assert min(i, j) >= 0, "Indices must be non-negative"
        assert i != j, "Cannot pour from same state to itself"
        n = min(capacities[j], state[i] + state[j])
        state[i], state[j] = state[i] + state[j] - n, n

    return state == goal
def sol50(capacities=[8, 5, 3], init=[8, 0, 0], goal=[4, 4, 0]):
    """
    Given an initial state of water quantities in jugs and jug capacities, find a sequence of moves (pouring
    one jug into another until it is full or the first is empty) to reaches the given goal state.
    moves is list of [from, to] pairs
    """
    from collections import deque
    num_jugs = len(capacities)
    start = tuple(init)
    target = tuple(goal)
    trails = {start: ([], start)}
    queue = deque([tuple(init)])
    while target not in trails:
        state = queue.popleft()
        for i in range(num_jugs):
            for j in range(num_jugs):
                if i != j:
                    n = min(capacities[j], state[i] + state[j])
                    new_state = list(state)
                    new_state[i], new_state[j] = state[i] + state[j] - n, n
                    new_state = tuple(new_state)
                    if new_state not in trails:
                        queue.append(new_state)
                        trails[new_state] = ([i, j], state)
    ans = []
    state = target
    while state != start:
        move, state = trails[state]
        ans.append(move)
    return ans[::-1]
# assert sat50(sol50())

def sat51(li: List[int], words=['SEND', 'MORE', 'MONEY']):
    assert len(li) == len(words) and all(i > 0 and len(str(i)) == len(w) for i, w in zip(li, words))
    assert len({c for w in words for c in w}) == len({(d, c) for i, w in zip(li, words) for d, c in zip(str(i), w)})
    return sum(li[:-1]) == li[-1]
def sol51(words=['SEND', 'MORE', 'MONEY']):
    """
    Find a list of integers corresponding to the given list of strings substituting a different digit for each
    character, so that the last string corresponds to the sum of the previous numbers.
    """
    pi = list(range(10))  # permutation
    letters = []
    order = {}
    steps = []
    tens = 1
    for col in range(1, 1 + max(len(w) for w in words)):
        for w in words:
            is_tot = (w is words[-1])
            if len(w) >= col:
                c = w[-col]
                if c in order:
                    if is_tot:
                        kind = "check"
                    else:
                        kind = "seen"
                else:
                    if is_tot:
                        kind = "derive"
                    else:
                        kind = "add"
                    order[c] = len(letters)
                    letters.append(c)
                steps.append((kind, order[c], tens))
        tens *= 10

    inits = [any(w[0] == c for w in words) for c in letters]

    def helper(pos, delta):  # on success, returns True and pi has the correct values
        if pos == len(steps):
            return delta == 0

        kind, i, tens = steps[pos]

        if kind == "seen":
            return helper(pos + 1, delta + tens * pi[i])

        if kind == "add":
            for j in range(i, 10):
                if pi[j] != 0 or not inits[i]:  # not adding a leading 0
                    pi[i], pi[j] = pi[j], pi[i]
                    if helper(pos + 1, delta + tens * pi[i]):
                        return True
                    pi[i], pi[j] = pi[j], pi[i]
            return False
        if kind == "check":
            delta -= tens * pi[i]
            return (delta % (10 * tens)) == 0 and helper(pos + 1, delta)

        assert kind == "derive"
        digit = (delta % (10 * tens)) // tens
        if digit == 0 and inits[i]:
            return False  # would be a leading 0
        j = pi.index(digit)
        if j < i:
            return False  # already used
        pi[i], pi[j] = pi[j], pi[i]
        if helper(pos + 1, delta - tens * digit):
            return True
        pi[i], pi[j] = pi[j], pi[i]
        return False

    assert helper(0, 0)
    return [int("".join(str(pi[order[c]]) for c in w)) for w in words]
# assert sat51(sol51())

def sat52(moves: List[int], start=[[5, 0, 2, 3], [1, 9, 6, 7], [4, 14, 8, 11], [12, 13, 10, 15]]):

    locs = {i: [x, y] for y, row in enumerate(start) for x, i in enumerate(row)}  # locations, 0 stands for blank
    for i in moves:
        assert abs(locs[0][0] - locs[i][0]) + abs(locs[0][1] - locs[i][1]) == 1
        locs[0], locs[i] = locs[i], locs[0]
    return all(locs[i] == [i % len(start[0]), i // len(start)] for i in locs)
def sol52(start=[[5, 0, 2, 3], [1, 9, 6, 7], [4, 14, 8, 11], [12, 13, 10, 15]]):
    """
    In this puzzle, you are given a board like:
    1 2 5
    3 4 0
    6 7 8

    and your goal is to transform it to:
    0 1 2
    3 4 5
    6 7 8

    by a sequence of swaps with the 0 square (0 indicates blank). The starting configuration is given by a 2d list
    of lists and the answer is represented by a list of integers indicating which number you swap with 0. In the
    above example, an answer would be [1, 2, 5]
    """
    from collections import defaultdict
    import math
    d = len(start)
    N = d * d
    assert all(len(row) == d for row in start)

    def get_state(
            li):  # state is an integer with 4 bits for each slot and the last 4 bits indicate where the blank is
        ans = 0
        for i in li[::-1] + [li.index(0)]:
            ans = (ans << 4) + i
        return ans

    start = get_state([i for row in start for i in row])
    target = get_state(list(range(N)))

    def h(state):  # manhattan distance
        ans = 0
        for i in range(N):
            state = (state >> 4)
            n = state & 15
            if n != 0:
                ans += abs(i % d - n % d) + abs(i // d - n // d)
        return ans

    g = defaultdict(lambda: math.inf)
    g[start] = 0  # shortest p ath lengths
    f = {start: h(start)}  # f[s] = g[s] + h(s)
    backtrack = {}

    todo = {start}
    import heapq
    heap = [(f[start], start)]

    neighbors = [[i for i in [b - 1, b + 1, b + d, b - d] if i in range(N) and (b // d == i // d or b % d == i % d)]
                 for b in range(N)]

    def next_state(s, blank, i):
        assert blank == (s & 15)
        v = (s >> (4 * i + 4)) & 15
        return s + (i - blank) + (v << (4 * blank + 4)) - (v << (4 * i + 4))

    while todo:
        (dist, s) = heapq.heappop(heap)
        if f[s] < dist:
            continue
        if s == target:
            # compute path
            ans = []
            while s != start:
                s, i = backtrack[s]
                ans.append((s >> (4 * i + 4)) & 15)
            return ans[::-1]

        todo.remove(s)

        blank = s & 15
        score = g[s] + 1
        for i in neighbors[blank]:
            s2 = next_state(s, blank, i)

            if score < g[s2]:
                # paths[s2] = paths[s] + [s[i]]
                g[s2] = score
                backtrack[s2] = (s, i)
                score2 = score + h(s2)
                f[s2] = score2
                todo.add(s2)
                heapq.heappush(heap, (score2, s2))
# assert sat52(sol52())

def sat53(pair: List[float], nums=[0.17, 21.3, 5.0, 9.0, 11.0, 4.99, 17.0, 17.0, 12.4, 6.8]):
    a, b = pair
    assert a in nums and b in nums and a != b
    return abs(a - b) == min(x - y for x in nums for y in nums if x > y)
def sol53(nums=[0.17, 21.3, 5.0, 9.0, 11.0, 4.99, 17.0, 17.0, 12.4, 6.8]):
    """
    Given a list of numbers, find the two closest distinct numbers in the list.

    Sample Input:
    [1.2, 5.23, 0.89, 21.0, 5.28, 1.2]

    Sample Output:
    [5.23, 5.28]
    """
    s = sorted(set(nums))
    return min([[a, b] for a, b in zip(s, s[1:])], key=lambda x: x[1] - x[0])
# assert sat53(sol53())

def sat54(ls: List[str], combined="() (()) ((() () ())) (() )"):
    for s in ls:
        assert s.count("(") == s.count(")")
        assert all(s[:i].count("(") > s[:i].count(")") for i in range(1, len(s)))  # s is not further divisible
    return ''.join(ls) == combined.replace(' ', '')
def sol54(combined="() (()) ((() () ())) (() )"):
    """
    Given a string consisting of whitespace and groups of matched parentheses, split it
    into groups of perfectly matched parentheses without any whitespace.

    Sample Input:
    '( ()) ((()()())) (()) ()'

    Sample Output:
    ['(())', '((()()()))', '(())', '()']
    """
    cur = ''
    ans = []
    depth = 0
    for c in combined.replace(' ', ''):
        cur += c
        if c == '(':
            depth += 1
        else:
            assert c == ')'
            depth -= 1
            if depth == 0:
                ans.append(cur)
                cur = ''
    return ans
# assert sat54(sol54())

def sat55(x: float, v=523.12892):
    return 0 <= x < 1 and (v - x).is_integer()
def sol55(v=523.12892):
    """
    Given a floating point number, find its fractional part.

    Sample Input:
    4.175

    Sample Output:
    0.175
    """
    return v % 1.0
# assert sat55(sol55())

def sat56(firsts: List[int], balances=[[2, 7, -2, 4, 3, -15, 10, -45, 3], [3, 4, -17, -1], [100, -100, -101], [-1]]):
    for i, bals in enumerate(balances):
        total = 0
        for b in bals:
            total += b
            if total < 0:
                assert total == firsts[i]
                break
    return True
def sol56(balances=[[2, 7, -2, 4, 3, -15, 10, -45, 3], [3, 4, -17, -1], [100, -100, -101], [-1]]):
    """
    Given a list of numbers which represent bank deposits and withdrawals, find the *first* negative balance.

    Sample Input:
    [[12, -5, 3, -99, 14, 88, -99], [-1, 2, 5]]

    Sample Output:
    [-89, -1]
    """
    firsts = []
    for bals in balances:
        total = 0
        for b in bals:
            total += b
            if total < 0:
                firsts.append(total)
                break
    return firsts
# assert sat56(sol56())

def sat57(x: float, nums=[12, -2, 14, 3, -15, 10, -45, 3, 30]):
    return sum((n - x) ** 2 for n in nums) * len(nums) <= sum((m - n) ** 2 for m in nums for n in nums) * .5 + 1e-4
def sol57(nums=[12, -2, 14, 3, -15, 10, -45, 3, 30]):
    """
    Given a list of numbers, find x that minimizes mean squared deviation.

    Sample Input:
    [4, -5, 17, -9, 14, 108, -9]

    Sample Output:
    17.14285
    """
    return sum(nums) / len(nums)  # mean minimizes mean squared deviation
# assert sat57(sol57())

def sat58(li: List[int], nums=[12, 23, -2, 5, 0], sep=4):
    return li[::2] == nums and li[1::2] == [sep] * (len(nums) - 1)
def sol58(nums=[12, 23, -2, 5, 0], sep=4):
    """
    Given a list of numbers and a number to inject, create a list containing that number in between each pair of
    adjacent numbers.

    Sample Input:
    [8, 14, 21, 17, 9, -5], 3

    Sample Output:
    [8, 3, 14, 3, 21, 3, 17, 3, 9, 3, -5]
    """
    ans = [sep] * (2 * len(nums) - 1)
    ans[::2] = nums
    return ans
# assert sat58(sol58())

def sat59(depths: List[int], parens="() (()) ((()()())) (((((((())))))))"):
    groups = parens.split()
    for depth, group in zip(depths, groups):
        budget = depth
        success = False
        for c in group:
            if c == '(':
                budget -= 1
                if budget == 0:
                    success = True
                assert budget >= 0
            else:
                assert c == ')'
                budget += 1
        assert success

    return len(groups) == len(depths)
def sol59(parens="() (()) ((()()())) (((((((())))))))"):
    """
    Given a string consisting of groups of matched nested parentheses separated by parentheses,
    compute the depth of each group.

    Sample Input:
    '(()) ((()()())) (()) ()'

    Sample Output:
    [2, 3, 2, 1]
    """
    def max_depth(s):
        m = 0
        depth = 0
        for c in s:
            if c == '(':
                depth += 1
                m = max(m, depth)
            else:
                assert c == ')'
                depth -= 1
        assert depth == 0
        return m

    return [max_depth(s) for s in parens.split()]
# assert sat59(sol59())

