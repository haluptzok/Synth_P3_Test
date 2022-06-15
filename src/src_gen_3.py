from typing import List

def sat30(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == rods[1] == []
def sol30():
    """
    Eight disks of sizes 1-8 are stacked on three towers, with each tower having disks in order of largest to
    smallest. Move [i, j] corresponds to taking the smallest disk off tower i and putting it on tower j, and it
    is legal as long as the towers remain in sorted order. Find a sequence of moves that moves all the disks
    from the first to last towers.
    """
    def helper(m, i, j):
        if m == 0:
            return []
        k = 3 - i - j
        return helper(m - 1, i, k) + [[i, j]] + helper(m - 1, k, j)

    return helper(8, 0, 2)
# assert sat30(sol30())

def sat31(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 1, 2, 3, 8], [4, 5], [6, 7]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target
def sol31(source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 1, 2, 3, 8], [4, 5], [6, 7]]):
    """
    A state is a partition of the integers 0-8 into three increasing lists. A move is pair of integers i, j in
    {0, 1, 2} corresponding to moving the largest number from the end of list i to list j, while preserving the
    order of list j. Find a sequence of moves that transform the given source to target states.
    """
    state = {d: i for i, tower in enumerate(source) for d in tower}
    final = {d: i for i, tower in enumerate(target) for d in tower}
    disks = set(state)
    assert disks == set(final) and all(isinstance(i, int) for i in state) and len(source) == len(target) >= 3
    ans = []

    def move(d, i):  # move disk d to tower i
        if state[d] == i:
            return
        for t in range(3):  # first tower besides i, state[d]
            if t != i and t != state[d]:
                break
        for d2 in range(d + 1, max(disks) + 1):
            if d2 in disks:
                move(d2, t)
        ans.append([state[d], i])
        state[d] = i

    for d in range(min(disks), max(disks) + 1):
        if d in disks:
            move(d, final[d])

    return ans
# assert sat31(sol31())

def sat32(x: List[int], length=13, s="Dynamic programming solves this puzzle!!!"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))
def sol32(length=13, s="Dynamic programming solves this puzzle!!!"):
    """
    Remove as few characters as possible from s so that the characters of the remaining string are alphebetical.
    Here x is the list of string indices that have not been deleted.
    """
    # O(N^2) method. Todo: add binary search solution which is O(n log n)
    if s == "":
        return []
    n = len(s)
    dyn = []  # list of (seq length, seq end, prev index)
    for i in range(n):
        try:
            dyn.append(max((length + 1, i, e) for length, e, _ in dyn if s[e] <= s[i]))
        except ValueError:
            dyn.append((1, i, -1))  # sequence ends at i
    _length, i, _ = max(dyn)
    backwards = [i]
    while dyn[i][2] != -1:
        i = dyn[i][2]
        backwards.append(i)
    return backwards[::-1]
# assert sat32(sol32())

def sat33(x: List[int], length=20, s="Dynamic programming solves this classic job-interview puzzle!!!"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))
def sol33(length=20, s="Dynamic programming solves this classic job-interview puzzle!!!"):
    """Find the indices of the longest substring with characters in sorted order"""
    # O(N^2) method. Todo: add binary search solution which is O(n log n)
    if s == "":
        return []
    n = len(s)
    dyn = []  # list of (seq length, seq end, prev index)
    for i in range(-n, n):
        try:
            dyn.append(max((length + 1, i, e) for length, e, _ in dyn if s[e] <= s[i]))
        except ValueError:
            dyn.append((1, i, None))  # sequence ends at i
    _length, i, _ = max(dyn)
    backwards = [i]
    while dyn[n + i][2] is not None:
        i = dyn[n + i][2]
        backwards.append(i)
    return backwards[::-1]
# assert sat33(sol33())

def sat34(quine: str):
    return eval(quine) == quine
def sol34():
    """Find a string that when evaluated as a Python expression is that string itself."""
    return "(lambda x: f'({x})({chr(34)}{x}{chr(34)})')(\"lambda x: f'({x})({chr(34)}{x}{chr(34)})'\")"
# assert sat34(sol34())

def sat35(rev_quine: str):
    return eval(rev_quine[::-1]) == rev_quine
def sol35():
    """Find a string that, when reversed and evaluated gives you back that same string."""
    return "rev_quine"[::-1]  # thanks GPT-3!
# assert sat35(sol35())

def sat36(colors: List[int], n=100):
    assert set(colors) <= {0, 1} and len(colors) >= n
    squares = {i ** 2: colors[i] for i in range(1, len(colors))}
    return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())
def sol36(n=100):
    """
    Color the first n integers with one of two colors so that there is no monochromatic Pythagorean triple.
    A monochromatic Pythagorean triple is a triple of numbers i, j, k such that i^2 + j^2 = k^2 that
    are all assigned the same color. The input, colors, is a list of 0/1 colors of length >= n.
    """
    sqrt = {i * i: i for i in range(1, n)}
    trips = [(sqrt[i], sqrt[j], sqrt[i + j]) for i in sqrt for j in sqrt if i < j and i + j in sqrt]
    import random
    random.seed(0)
    sol = [random.randrange(2) for _ in range(n)]
    done = False
    while not done:
        done = True
        random.shuffle(trips)
        for i, j, k in trips:
            if sol[i] == sol[j] == sol[k]:
                done = False
                sol[random.choice([i, j, k])] = 1 - sol[i]
    return sol
# assert sat36(sol36())

def sat37(hands: List[int], target_angle=45):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]
def sol37(target_angle=45):
    """Find clock hands = [hour, min] such that the angle is target_angle degrees."""
    for h in range(1, 13):
        for m in range(60):
            hour_angle = 30 * h + m / 2
            minute_angle = 6 * m
            if abs(hour_angle - minute_angle) % 360 in [target_angle, 360 - target_angle]:
                return [h, m]
# assert sat37(sol37())

def sat38(daygroups: List[List[List[int]]]):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 3 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 15 * 15
def sol38():
    """
    Arrange 15 people into groups of 3 each day for seven days so that no two people are in the same group twice.
    """
    from itertools import combinations
    import random
    rand = random.Random(0)
    days = [[list(range(15)) for _2 in range(2)] for _ in range(7)]  # each day is pi, inv
    counts = {(i, j): (7 if j in range(k, k + 3) else 0)
              for k in range(0, 15, 3)
              for i in range(k, k + 3)
              for j in range(15) if j != i
              }

    todos = [pair for pair, count in counts.items() if count == 0]
    while True:
        pair = rand.choice(todos)  # choose i and j to make next to each other on some day
        if rand.randrange(2):
            pair = pair[::-1]

        a, u = pair
        pi, inv = rand.choice(days)
        assert pi[inv[a]] == a and pi[inv[u]] == u
        bases = [3 * (inv[i] // 3) for i in pair]
        (b, c), (v, w) = [[x for x in pi[b: b + 3] if x != i] for i, b in zip(pair, bases)]
        if rand.randrange(2):
            b, c, = c, b
        # current (a, b, c) (u, v, w). consider swap of u with b to make (a, u, c) (b, v, w)

        new_pairs = [(a, u), (c, u), (b, v), (b, w)]
        old_pairs = [(u, v), (u, w), (b, a), (b, c)]
        gained = sum(counts[p] == 0 for p in new_pairs)
        lost = sum(counts[p] == 1 for p in old_pairs)
        if rand.random() <= 100 ** (gained - lost):
            for p in new_pairs:
                counts[p] += 1
                counts[p[::-1]] += 1
            for p in old_pairs:
                counts[p] -= 1
                counts[p[::-1]] -= 1
            pi[inv[b]], pi[inv[u]], inv[b], inv[u] = u, b, inv[u], inv[b]
            todos = [pair for pair, count in counts.items() if count == 0]
            if len(todos) == 0:
                return [[pi[k:k + 3] for k in range(0, 15, 3)] for pi, _inv in days]
# assert sat38(sol38())

def sat39(n: int):
    for i in range(5):
        assert n % 5 == 1
        n -= 1 + (n - 1) // 5
    return n > 0 and n % 5 == 1
def sol39():
    """
    Find the number of coconuts to solve the following riddle:
        There is a pile of coconuts, owned by five men. One man divides the pile into five equal piles, giving the
        one left over coconut to a passing monkey, and takes away his own share. The second man then repeats the
        procedure, dividing the remaining pile into five and taking away his share, as do the third, fourth, and
        fifth, each of them finding one coconut left over when dividing the pile by five, and giving it to a monkey.
        Finally, the group divide the remaining coconuts into five equal piles: this time no coconuts are left over.
        How many coconuts were there in the original pile?
                                          Quoted from https://en.wikipedia.org/wiki/The_monkey_and_the_coconuts
    """
    m = 1
    while True:
        n = m
        for i in range(5):
            if n % 5 != 1:
                break
            n -= 1 + (n - 1) // 5
        if n > 0 and n % 5 == 1:
            return m
        m += 5
# assert sat39(sol39())

