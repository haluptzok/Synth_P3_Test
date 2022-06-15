from typing import List

def sat310(path: List[int], edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [3, 4], [5, 6], [6, 7], [1, 2]]):
    for i in range(len(path) - 1):
        assert [path[i], path[i + 1]] in edges
    assert path[0] == 0
    assert path[-1] == max(max(edge) for edge in edges)
    return True
def sol310(edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [3, 4], [5, 6], [6, 7], [1, 2]]):
    """ Find any path from node 0 to node n in a given digraph on vertices 0, 1,..., n."""
    n = max(max(edge) for edge in edges)
    paths = {0: [0]}
    for _ in range(n + 1):
        for i, j in edges:
            if i in paths and j not in paths:
                paths[j] = paths[i] + [j]
    return paths.get(n)
# assert sat310(sol310())

def sat311(path: List[int], edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [3, 4], [5, 6], [6, 7], [1, 2]]):
    assert path[0] == 0 and path[-1] == max(max(e) for e in edges)
    assert all([[a, b] in edges for a, b in zip(path, path[1:])])
    return len(path) % 2 == 0
def sol311(edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [3, 4], [5, 6], [6, 7], [1, 2]]):
    """Find a path with an even number of nodes from nodes 0 to n in the given digraph on vertices 0, 1,..., n."""
    even_paths = {}
    odd_paths = {0: [0]}
    n = max(max(e) for e in edges)
    for _ in range(n + 1):
        for i, j in edges:
            if i in even_paths and j not in odd_paths:
                odd_paths[j] = even_paths[i] + [j]
            if i in odd_paths and j not in even_paths:
                even_paths[j] = odd_paths[i] + [j]
    return even_paths.get(n)
# assert sat311(sol311())

def sat312(p: List[int], edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [3, 4], [5, 6], [6, 7], [6, 1]]):
    return p[0] == 0 and p[-1] == 1 == len(p) % 2 and all([[a, b] in edges for a, b in zip(p, p[1:])])
def sol312(edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [3, 4], [5, 6], [6, 7], [6, 1]]):
    """Find a path with an even number of nodes from nodes 0 to 1 in the given digraph on vertices 0, 1,..., n."""
    even_paths = {}
    odd_paths = {0: [0]}
    n = 1
    for _ in range(max(max(e) for e in edges) + 1):
        for i, j in edges:
            if i in even_paths and j not in odd_paths:
                odd_paths[j] = even_paths[i] + [j]
            if i in odd_paths and j not in even_paths:
                even_paths[j] = odd_paths[i] + [j]
    return odd_paths.get(n)
# assert sat312(sol312())

def sat313(edges: List[List[int]], z=20, n=5, t=3):
    from itertools import combinations
    edges = {(a, b) for a, b in edges if a in range(n) and b in range(n)}  # convert to a set for efficiency
    assert len(edges) >= z

    return all(
        any((a, b) not in edges for a in left for b in right)
        for left in combinations(range(n), t)
        for right in combinations(range(n), t)
    )
def sol313(z=20, n=5, t=3):
    """Find a bipartite graph with n vertices on each side, z edges, and no K_3,3 subgraph."""
    from itertools import combinations
    all_edges = [(a, b) for a in range(n) for b in range(n)]
    for edges in combinations(all_edges, z):
        edge_set = set(edges)
        if all(any((a, b) not in edge_set for a in left for b in right)
               for left in combinations(range(n), t)
               for right in combinations(range(n), t)):
            return [[a, b] for a, b in edges]
# assert sat313(sol313())

def sat314(bi: List[int], g1=[[0, 1], [1, 2], [2, 3], [3, 4], [2, 5]], g2=[[0, 4], [1, 5], [4, 1], [1, 2], [2, 3]]):
    return len(bi) == len(set(bi)) and {(i, j) for i, j in g1} == {(bi[i], bi[j]) for i, j in g2}
def sol314(g1=[[0, 1], [1, 2], [2, 3], [3, 4], [2, 5]], g2=[[0, 4], [1, 5], [4, 1], [1, 2], [2, 3]]):
    """
    You are given two graphs which are permutations of one another and the goal is to find the permutation.
    Each graph is specified by a list of edges where each edge is a pair of integer vertex numbers.
    """
    # exponentially slow
    from itertools import permutations
    n = max(i for g in [g1, g2] for e in g for i in e) + 1
    g1_set = {(i, j) for i, j in g1}
    for pi in permutations(range(n)):
        if all((pi[i], pi[j]) in g1_set for i, j in g2):
            return list(pi)
    assert False, f"Graphs are not isomorphic {g1}, {g2}"
# assert sat314(sol314())

def sat315(li: List[int]):
    return all(j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128])) and len(li) == 9
def sol315():
    """
    Find a list of nine integers, starting with 0 and ending with 128, such that each integer either differs from
    the previous one by one or is thrice the previous one.
    """
    return [1, 3, 4, 12, 13, 14, 42, 126, 127]
# assert sat315(sol315())

def sat316(perms: List[List[int]], prices0=[7, 7, 9, 5, 3, 7, 1, 2], prices1=[5, 5, 5, 4, 2, 5, 1, 1], heights0=[2, 4, 9, 3, 8, 5, 5, 4], heights1=[1, 3, 8, 1, 5, 4, 4, 2]):
    n = len(prices0)
    perm0, perm1 = perms
    assert sorted(perm0) == sorted(perm1) == list(range(n)), "Solution must be two permutations"
    for i in range(n - 1):
        assert prices0[perm0[i]] <= prices0[perm0[i + 1]], "Permuted prices must be nondecreasing (row 0)"
        assert prices1[perm1[i]] <= prices1[perm1[i + 1]], "Permuted prices must be nondecreasing (row 1)"
    return all(heights0[i] > heights1[j] for i, j in zip(perm0, perm1))
def sol316(prices0=[7, 7, 9, 5, 3, 7, 1, 2], prices1=[5, 5, 5, 4, 2, 5, 1, 1], heights0=[2, 4, 9, 3, 8, 5, 5, 4], heights1=[1, 3, 8, 1, 5, 4, 4, 2]):
    """
    There are two rows of objects. Given the length-n integer arrays of prices and heights of objects in each
    row, find a permutation of both rows so that the permuted prices are non-decreasing in each row and
    so that the first row is taller than the second row.
    """
    n = len(prices0)
    prices = [prices0, prices1]
    orders = [sorted(range(n), key=lambda i: (prices0[i], heights0[i])),
              sorted(range(n), key=lambda i: (prices1[i], -heights1[i]))]
    jumps = [1, 1]  # next price increase locations
    for i in range(n):
        for r, (p, o) in enumerate(zip(prices, orders)):
            while jumps[r] < n and p[o[jumps[r]]] == p[o[i]]:
                jumps[r] += 1

        to_fix = orders[jumps[0] < jumps[1]]
        j = i
        while heights0[orders[0][i]] <= heights1[orders[1][i]]:
            j += 1
            to_fix[i], to_fix[j] = to_fix[j], to_fix[i]

    return orders
# assert sat316(sol316())

def sat317(indices: List[int], H=60, alpha=18, beta=2, xs=[0, 10, 20, 30, 50, 80, 100, 120, 160, 190, 200], ys=[0, 30, 10, 30, 50, 40, 10, 20, 20, 55, 10], thresh=26020):
    assert sorted({0, len(xs) - 1, *indices}) == indices, f"Ans. should be sorted list [0, ..., {len(xs) - 1}]"
    cost = alpha * (H - ys[0])
    for i, j in zip(indices, indices[1:]):
        a, b, r = xs[i], xs[j], (xs[j] - xs[i]) / 2
        assert max(ys[i], ys[j]) + r <= H, "Bridge too tall"
        assert all(ys[k] <= H - r + ((b - xs[k]) * (xs[k] - a)) ** 0.5 for k in range(i + 1, j)), \
            "Bridge too short"
        cost += alpha * (H - ys[j]) + beta * (b - a) ** 2
    return cost <= thresh
def sol317(H=60, alpha=18, beta=2, xs=[0, 10, 20, 30, 50, 80, 100, 120, 160, 190, 200], ys=[0, 30, 10, 30, 50, 40, 10, 20, 20, 55, 10], thresh=26020):
    """
    You are to choose locations for bridge bases from among a given set of mountain peaks located at
    `xs, ys`, where `xs` and `ys` are lists of n integers of the same length. Your answer should be a sorted
    list of indices starting at 0 and ending at n-1. The goal is to minimize building costs such that the bridges
    are feasible. The bridges are all semicircles placed on top of the pillars. The feasibility constraints are that:
    * The bridges may not extend above a given height `H`. Mathematically, if the distance between the two xs
    of adjacent pillars is d, then the semicircle will have radius `d/2` and therefore the heights of the
    selected mountain peaks must both be at most `H - d/2`.
    *  The bridges must clear all the mountain peaks, which means that the semicircle must lie above the tops of the
    peak. See the code for how this is determined mathematically.
    * The total cost of all the bridges must be at most `thresh`, where the cost is parameter alpha * (the sum of
    all pillar heights) + beta * (the sum of the squared diameters)
    """
    # thresh is ignored
    n = len(xs)
    cost = [-1] * n
    prior = [n] * n
    cost[0] = beta * (H - ys[0])
    for i in range(n):
        if cost[i] == -1:
            continue
        min_d = 0
        max_d = 2 * (H - ys[i])
        for j in range(i + 1, n):
            d = xs[j] - xs[i]
            h = H - ys[j]
            if d > max_d:
                break
            if 2 * h <= d:
                min_d = max(min_d, 2 * d + 2 * h - int((8 * d * h) ** 0.5))
            max_d = min(max_d, 2 * d + 2 * h + int((8 * d * h) ** 0.5))
            if min_d > max_d:
                break
            if min_d <= d <= max_d:
                new_cost = cost[i] + alpha * h + beta * d * d
                if cost[j] == -1 or cost[j] > new_cost:
                    cost[j] = new_cost
                    prior[j] = i
    rev_ans = [n - 1]
    while rev_ans[-1] != 0:
        rev_ans.append(prior[rev_ans[-1]])
    return rev_ans[::-1]
# assert sat317(sol317())

def sat318(position: List[List[int]], transcript=[[[3, 3], [5, 5], [3, 7]], [[5, 3], [6, 4]]]):
    board = {(x, y): 0 for x in range(8) for y in range(8) if (x + y) % 2 == 0}  # empty board, 0 = empty
    for x, y, p in position:
        assert -2 <= p <= 2 and board[x, y] == 0  # -1, 1 is regular piece, -2, 2 is king
        board[x, y] = p

    def has_a_jump(x, y):
        p = board[x, y]  # piece to move
        deltas = [(dx, dy) for dx in [-1, 1] for dy in [-1, 1] if dy != -p]  # don't check backwards for non-kings
        return any(board.get((x + 2 * dx, y + 2 * dy)) == 0 and board[x + dx, y + dy] * p < 0 for dx, dy in deltas)

    sign = 1  # player 1 moves first
    for move in transcript:
        start, end = tuple(move[0]), tuple(move[-1])
        p = board[start]  # piece to move
        assert p * sign > 0, "Moving square must be non-empty and players must be alternate signs"
        assert all(board[x, y] == 0 for x, y in move if [x, y] != move[0]), "Moved to an occupied square"

        for (x1, y1), (x2, y2) in zip(move, move[1:]):
            assert abs(p) != 1 or (y2 - y1) * p > 0, "Non-kings can only move forward (in direction of sign)"
            if abs(x2 - x1) == 1:  # non-jump
                assert not any(has_a_jump(*a) for a in board if board[a] * p > 0), "Must make a jump if possible"
                break
            mid = ((x1 + x2) // 2, (y1 + y2) // 2)
            assert board[mid] * p < 0, "Can only jump over piece of opposite sign"
            board[mid] = 0
        board[start], board[end] = 0, p
        assert abs(x2 - x1) == 1 or not has_a_jump(*end)
        if abs(p) == 1 and any(y in {0, 7} for x, y in move[1:]):
            board[end] *= 2  # king me at the end of turn after any jumps are done!
        sign *= -1

    return True
def sol318(transcript=[[[3, 3], [5, 5], [3, 7]], [[5, 3], [6, 4]]]):
    """
    You are given a partial transcript a checkers game. Find an initial position such that the transcript
    would be a legal set of moves. The board positions are [x, y] pairs with 0 <= x, y < 8 and x + y even.
    There are two players which we call -1 and 1 for convenience, and player 1 must move first in transcript.
    The initial position is represented as a list [x, y, piece] where piece means:
    * 0 is empty square
    * 1 or -1 is piece that moves only in the y = 1 or y = -1 dir, respectively
    * 2 or -2 is king for player 1 or player 2 respectively

    Additional rules:
    * You must jump if you can, and you must continue jumping until one can't any longer.
    * You cannot start the position with any non-kings on your last rank.
    * Promotion happens after the turn ends
    """
    START_PLAYER = 1  # assumed

    class InitOpts:
        def __init__(self, x, y):
            self.x, self.y = x, y
            self.opts = {-2, -1, 0, 1, 2}
            if y == 0:
                self.opts.remove(-1)
            if y == 7:
                self.opts.remove(1)
            self.promoted = 2 ** 63  # on which step was it promoted t >= 0
            self.jumped = 2 ** 63  # on which step was it jumped t >= 0

    # def board2str(board):  # for debugging
    #     mapping = ".bBWw"
    #     ans = ""
    #     for y in range(7, -1, -1):
    #         ans += "".join(" " if (x+y)%2 else mapping[board[x,y]] for x in range(8)) + "\n"
    #     return ans

    init_opts = {(x, y): InitOpts(x, y) for x in range(8) for y in range(8) if (x + y) % 2 == 0}
    # board = {(x, y): (1 if y < 3 else -1 if y > 4 else 0) for x in range(8) for y in range(8) if
    #          (x + y) % 2 == 0}  # new board

    transcript = [[tuple(a) for a in move] for move in transcript]

    permuted_opts = init_opts.copy()
    sign = START_PLAYER
    for t, move in enumerate(transcript):
        start, end = tuple(move[0]), tuple(move[-1])
        p = permuted_opts[start]  # opts to move
        assert p.jumped >= t
        p.opts -= {-sign, -2 * sign, 0}
        if any((y2 - y1) * sign < 0 for (x1, y1), (x2, y2) in zip(move, move[1:])):  # backward move!
            if p.promoted >= t:
                p.opts -= {sign}  # must be a king!

        for a, b in zip(move, move[1:]):
            if permuted_opts[b].jumped >= t:
                permuted_opts[b].opts -= {-2, -1, 1, 2}  # must be empty
            assert permuted_opts[a].jumped >= t
            permuted_opts[a], permuted_opts[b] = permuted_opts[b], permuted_opts[a]
            # board[a], board[b] = board[b], board[a]
            (x1, y1), (x2, y2) = a, b
            if abs(x2 - x1) == 2:  # jump
                mid = ((x1 + x2) // 2, (y1 + y2) // 2)
                assert permuted_opts[mid].jumped >= t
                permuted_opts[mid].opts -= {0, sign, 2 * sign}  # Can only jump over piece of opposite sign
                permuted_opts[mid].jumped = t
                # board[mid] = 0

        if any(y in {0, 7} for x, y in move[1:]):
            if p.promoted > t:
                p.promoted = t
            # if abs(board[x2, y2]) == 1:
            #     board[x2, y2] *= 2

        sign *= -1

    for y in range(7, -1, -1):
        for x in range(8):
            if (x, y) in init_opts:
                s = init_opts[x, y].opts
                if {1, 2} <= s:
                    s.remove(2)
                if {-1, -2} <= s:
                    s.remove(-2)

    def helper():  # returns True if success and store everything, otherwise None
        my_opts = init_opts.copy()
        sign = START_PLAYER  # player 1 always starts

        for t, move in enumerate(transcript):
            if abs(move[0][0] - move[1][0]) == 1:  # not a jump
                check_no_jumps = [a for a, p in my_opts.items() if p.jumped >= t and p.opts <= {sign, 2 * sign}]
            else:
                for a, b in zip(move, move[1:]):
                    my_opts[a], my_opts[b] = my_opts[b], my_opts[a]
                check_no_jumps = [b]

            for x, y in check_no_jumps:
                p = my_opts[x, y]
                [o] = p.opts
                assert o * sign > 0
                dys = [o] if (abs(o) == 1 and p.promoted >= t) else [-1, 1]  # only check forward jumps
                for dx in [-1, 1]:
                    for dy in dys:
                        target_o = my_opts.get((x + 2 * dx, y + 2 * dy))
                        if target_o is not None and (0 in target_o.opts or target_o.jumped < t):
                            mid_o = my_opts[x + dx, y + dy]
                            if mid_o.jumped > t and mid_o.opts <= {-sign, -2 * sign}:  # ok if jumped at t
                                if target_o.jumped < t or target_o.opts == {0}:
                                    return False
                                old_opts = target_o.opts
                                for v in target_o.opts:
                                    if v != 0:
                                        target_o.opts = {v}
                                        h = helper()
                                        if h:
                                            return True
                                target_o.opts = old_opts
                                return False

            if abs(move[0][0] - move[1][0]) == 1:  # not a jump
                a, b = move[0], move[1]
                my_opts[a], my_opts[b] = my_opts[b], my_opts[a]

            sign *= -1
        return True

    res = helper()
    assert res

    def get_opt(opts):
        if 0 in opts.opts:
            return 0
        assert len(opts.opts) == 1
        return list(opts.opts)[0]

    return [[x, y, get_opt(opts)] for (x, y), opts in init_opts.items()]
# assert sat318(sol318())

def sat319(cut_position: int, ring="yRrsmOkLCHSDJywpVDEDsjgCwSUmtvHMefxxPFdmBIpM", lower=5):
    line = ring[cut_position:] + ring[:cut_position]
    matches = {c: 0 for c in line.lower()}
    for c in line:
        if c.islower():
            matches[c] -= (1 if matches[c] > 0 else len(line))
        else:
            matches[c.lower()] += 1
    return sum(i == 0 for i in matches.values()) >= lower
def sol319(ring="yRrsmOkLCHSDJywpVDEDsjgCwSUmtvHMefxxPFdmBIpM", lower=5):
    """
    The input is a string of start and end markers "aaBAcGeg" where upper-case characters indicate start markers
    and lower-case characters indicate ending markers. The string indicates a ring (joined at the ends) and the goal is
    to find a location to split the ring so that there are a maximal number of matched start/end chars where a character
    (like "a"/"A") is matched if starting at the split and going around the ring, the start-end pairs form a valid
    nesting like nested parentheses. Can you solve it in linear time?
    """
    cumulatives = {c: [(0, 0)] for c in ring.lower()}
    n = len(ring)
    for i, c in enumerate(ring):
        v = cumulatives[c.lower()]
        v.append((i, v[-1][1] + (-1 if c.islower() else 1)))

    scores = [0]*n
    cumulatives = {c: v for c, v in cumulatives.items() if v[-1][1]==0}
    for c, v in cumulatives.items():
        if v[-1][1] != 0: # ignore things with unequal numbers of opens and closes
            continue
        m = min(t for i, t in v)
        for (i, t), (i2, t2) in zip(v, v[1:] + [(n, 0)]):
            if t == m:
                for j in range(i+1, i2+1):
                    scores[j % n] += 1
    b = max(scores)
    for i in range(n):
        if scores[i] == b:
            return i
# assert sat319(sol319())

