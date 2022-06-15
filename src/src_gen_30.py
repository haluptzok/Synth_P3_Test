from typing import List

def sat300(good_boards: List[str]):
    board_bit_reps = {tuple(sum(1 << i for i in range(9) if b[i] == c) for c in "XO") for b in good_boards}
    win = [any(i & w == w for w in [7, 56, 73, 84, 146, 273, 292, 448]) for i in range(512)]

    def tie(x, o):  # returns True if X has a forced tie/win assuming it's X's turn to move.
        x |= 1 << [i for i in range(9) if (x | (1 << i), o) in board_bit_reps][0]
        return not win[o] and (win[x] or all((x | o) & (1 << i) or tie(x, o | (1 << i)) for i in range(9)))

    return tie(0, 0)
def sol300():
    """
    Compute a strategy for X (first player) in tic-tac-toe that guarantees a tie. That is a strategy for X that,
    no matter what the opponent does, X does not lose.

    A board is represented as a 9-char string like an X in the middle would be "....X...." and a
    move is an integer 0-8. The answer is a list of "good boards" that X aims for, so no matter what O does there
    is always good board that X can get to with a single move.
    """
    win = [any(i & w == w for w in [7, 56, 73, 84, 146, 273, 292, 448]) for i in range(512)]  # 9-bit representation

    good_boards = []

    def x_move(x, o):  # returns True if x wins or ties, x's turn to move
        if win[o]:
            return False
        if x | o == 511:
            return True
        for i in range(9):
            if (x | o) & (1 << i) == 0 and o_move(x | (1 << i), o):
                good_boards.append("".join(".XO"[((x >> j) & 1) + 2 * ((o >> j) & 1) + (i == j)] for j in range(9)))
                return True
        return False  # O wins

    def o_move(x, o):  # returns True if x wins or ties, x's turn to move
        if win[x] or x | o == 511:  # full board
            return True
        for i in range(9):
            if (x | o) & (1 << i) == 0 and not x_move(x, o | (1 << i)):
                return False
        return True  # O wins

    res = x_move(0, 0)
    assert res

    return good_boards
# assert sat300(sol300())

def sat301(good_boards: List[str]):
    board_bit_reps = {tuple(sum(1 << i for i in range(9) if b[i] == c) for c in "XO") for b in good_boards}
    win = [any(i & w == w for w in [7, 56, 73, 84, 146, 273, 292, 448]) for i in range(512)]

    def tie(x, o):  # returns True if O has a forced tie/win. It's O's turn to move.
        if o | x != 511:  # complete board
            o |= 1 << [i for i in range(9) if (x, o | (1 << i)) in board_bit_reps][0]
        return not win[x] and (win[o] or all((x | o) & (1 << i) or tie(x | (1 << i), o) for i in range(9)))

    return all(tie(1 << i, 0) for i in range(9))
def sol301():
    """
    Compute a strategy for O (second player) in tic-tac-toe that guarantees a tie. That is a strategy for O that,
    no matter what the opponent does, O does not lose.

    A board is represented as a 9-char string like an X in the middle would be "....X...." and a
    move is an integer 0-8. The answer is a list of "good boards" that O aims for, so no matter what X does there
    is always good board that O can get to with a single move.
    """
    win = [any(i & w == w for w in [7, 56, 73, 84, 146, 273, 292, 448]) for i in range(512)]  # 9-bit representation

    good_boards = []

    def x_move(x, o):  # returns True if o wins or ties, x's turn to move
        if win[o] or x | o == 511:  # full board
            return True
        for i in range(9):
            if (x | o) & (1 << i) == 0 and not o_move(x | (1 << i), o):
                return False
        return True  # O wins/ties

    def o_move(x, o):  # returns True if o wins or ties, o's turn to move
        if win[x]:
            return False
        if x | o == 511:
            return True
        for i in range(9):
            if (x | o) & (1 << i) == 0 and x_move(x, o | (1 << i)):
                good_boards.append(
                    "".join(".XO"[((x >> j) & 1) + 2 * ((o >> j) & 1) + 2 * (i == j)] for j in range(9)))
                return True
        return False  # X wins

    res = x_move(0, 0)
    assert res

    return good_boards
# assert sat301(sol301())

def sat302(probs: List[float]):
    assert len(probs) == 3 and abs(sum(probs) - 1) < 1e-6
    return max(probs[(i + 2) % 3] - probs[(i + 1) % 3] for i in range(3)) < 1e-6
def sol302():
    """Find optimal probabilities for playing Rock-Paper-Scissors zero-sum game, with best worst-case guarantee"""
    return [1 / 3] * 3
# assert sat302(sol302())

def sat303(strategies: List[List[float]], A=[[1.0, -1.0], [-1.3, 0.8]], B=[[-0.9, 1.1], [0.7, -0.8]], eps=0.01):
    m, n = len(A), len(A[0])
    p, q = strategies
    assert len(B) == m and all(len(row) == n for row in A + B), "inputs are a bimatrix game"
    assert len(p) == m and len(q) == n, "solution is a pair of strategies"
    assert sum(p) == sum(q) == 1.0 and min(p + q) >= 0.0, "strategies must be non-negative and sum to 1"
    v = sum(A[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
    w = sum(B[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
    return (all(sum(A[i][j] * q[j] for j in range(n)) <= v + eps for i in range(m)) and
            all(sum(B[i][j] * p[i] for i in range(m)) <= w + eps for j in range(n)))
def sol303(A=[[1.0, -1.0], [-1.3, 0.8]], B=[[-0.9, 1.1], [0.7, -0.8]], eps=0.01):
    """
    Find an eps-Nash-equilibrium for a given two-player game with payoffs described by matrices A, B.
    For example, for the classic Prisoner dilemma:
       A=[[-1., -3.], [0., -2.]], B=[[-1., 0.], [-3., -2.]], and strategies = [[0, 1], [0, 1]]

    eps is the error tolerance
    """
    NUM_ATTEMPTS = 10 ** 5

    def sat303(strategies: List[List[float]], A, B, eps):
        m, n = len(A), len(A[0])
        p, q = strategies
        assert len(B) == m and all(len(row) == n for row in A + B), "inputs are a bimatrix game"
        assert len(p) == m and len(q) == n, "solution is a pair of strategies"
        assert sum(p) == sum(q) == 1.0 and min(p + q) >= 0.0, "strategies must be non-negative and sum to 1"
        v = sum(A[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        w = sum(B[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        return (all(sum(A[i][j] * q[j] for j in range(n)) <= v + eps for i in range(m)) and
                all(sum(B[i][j] * p[i] for i in range(m)) <= w + eps for j in range(n)))

    import random
    r = random.Random(0)
    dims = len(A), len(A[0])
    # possible speedup: remove dominated strategies
    for _attempt in range(NUM_ATTEMPTS):
        strategies = []
        for d in dims:
            s = [max(0.0, r.random() - 0.5) for _ in range(d)]
            tot = sum(s) + 1e-6
            for i in range(d):
                s[i] = (1.0 - sum(s[:-1])) if i == d - 1 else (s[i] / tot)  # to ensure sum is exactly 1.0
            strategies.append(s)
        if sat303(strategies, A, B, eps):
            return strategies
# assert sat303(sol303())

def sat304(strategies: List[List[float]], A=[[0.0, -0.5, 1.0], [0.75, 0.0, -1.0], [-1.0, 0.4, 0.0]], eps=0.01):
    m, n = len(A), len(A[0])
    p, q = strategies
    assert all(len(row) == n for row in A), "inputs are a matrix"
    assert len(p) == m and len(q) == n, "solution is a pair of strategies"
    assert sum(p) == sum(q) == 1.0 and min(p + q) >= 0.0, "strategies must be non-negative and sum to 1"
    v = sum(A[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
    return (all(sum(A[i][j] * q[j] for j in range(n)) <= v + eps for i in range(m)) and
            all(sum(A[i][j] * p[i] for i in range(m)) >= v - eps for j in range(n)))
def sol304(A=[[0.0, -0.5, 1.0], [0.75, 0.0, -1.0], [-1.0, 0.4, 0.0]], eps=0.01):
    """
    Compute minimax optimal strategies for a given zero-sum game up to error tolerance eps.
    For example, rock paper scissors has
    A = [[0., -1., 1.], [1., 0., -1.], [-1., 1., 0.]] and strategies = [[0.33, 0.33, 0.34]] * 2
    """
    MAX_ITER = 10 ** 4
    m, n = len(A), len(A[0])
    a = [0 for _i in range(m)]
    b = [0 for _j in range(n)]

    for count in range(1, MAX_ITER):
        i_star = max(range(m), key=lambda i: sum(A[i][j] * b[j] for j in range(n)))
        j_star = min(range(n), key=lambda j: sum(A[i][j] * a[i] for i in range(m)))
        a[i_star] += 1
        b[j_star] += 1
        p = [x / (count + 1e-6) for x in a]
        p[-1] = 1 - sum(p[:-1])  # rounding issues
        q = [x / (count + 1e-6) for x in b]
        q[-1] = 1 - sum(q[:-1])  # rounding issues

        v = sum(A[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        if (all(sum(A[i][j] * q[j] for j in range(n)) <= v + eps for i in range(m)) and
                all(sum(A[i][j] * p[i] for i in range(m)) >= v - eps for j in range(n))):
            return [p, q]
# assert sat304(sol304())

def sat305(e: List[int], edges=[[0, 217], [40, 11], [17, 29], [11, 12], [31, 51]]):
    return e in edges
def sol305(edges=[[0, 217], [40, 11], [17, 29], [11, 12], [31, 51]]):
    """Find any edge in edges."""
    return edges[0]
# assert sat305(sol305())

def sat306(tri: List[int], edges=[[0, 17], [0, 22], [17, 22], [17, 31], [22, 31], [31, 17]]):
    a, b, c = tri
    return [a, b] in edges and [b, c] in edges and [c, a] in edges and a != b != c != a
def sol306(edges=[[0, 17], [0, 22], [17, 22], [17, 31], [22, 31], [31, 17]]):
    """Find any triangle in the given directed graph."""
    from collections import defaultdict
    outs = defaultdict(set)
    ins = defaultdict(set)
    for i, j in edges:
        if j != i:
            outs[i].add(j)
            ins[j].add(i)
    for i in outs:
        for j in outs[i]:
            try:
                if j in outs:
                    k = min(outs[j].intersection(ins[i]))
                    return [i, j, k]
            except ValueError:
                pass
# assert sat306(sol306())

def sat307(nodes: List[int], size=3, edges=[[0, 17], [0, 22], [17, 22], [17, 31], [22, 31], [31, 17]]):
    assert len(nodes) == len(set(nodes)) >= size
    edge_set = {(a, b) for (a, b) in edges}
    for a in nodes:
        for b in nodes:
            assert a == b or (a, b) in edge_set or (b, a) in edge_set

    return True
def sol307(size=3, edges=[[0, 17], [0, 22], [17, 22], [17, 31], [22, 31], [31, 17]]):
    """Find a clique of the given size in the given undirected graph. It is guaranteed that such a clique exists."""
    # brute force (finds list in increasing order), but with a tiny bit of speedup
    if size == 0:
        return []
    from collections import defaultdict
    neighbors = defaultdict(set)
    n = max(max(e) for e in edges)
    for (a, b) in edges:
        if a != b:
            neighbors[a].add(b)
            neighbors[b].add(a)
    pools = [list(range(n + 1))]
    indices = [-1]
    while pools:
        indices[-1] += 1
        if indices[-1] >= len(pools[-1]) - size + len(pools):  # since list is increasing order
            indices.pop()
            pools.pop()
            continue
        if len(pools) == size:
            return [pool[i] for pool, i in zip(pools, indices)]
        a = (pools[-1])[indices[-1]]
        pools.append([i for i in pools[-1] if i > a and i in neighbors[a]])
        indices.append(-1)
    assert False, f"No clique of size {size}"
# assert sat307(sol307())

def sat308(path: List[int], weights=[{1: 20, 2: 1}, {2: 2, 3: 5}, {1: 10}], bound=11):
    return path[0] == 0 and path[-1] == 1 and sum(weights[a][b] for a, b in zip(path, path[1:])) <= bound
def sol308(weights=[{1: 20, 2: 1}, {2: 2, 3: 5}, {1: 10}], bound=11):
    """
    Find a path from node 0 to node 1, of length at most bound, in the given digraph.
    weights[a][b] is weight on edge [a,b] for (int) nodes a, b
    """
    # Dijkstra's algorithm (bound is ignored)
    u, v = 0, 1  # go from 0 to 1
    import heapq
    queue = [(0, u, u)]  # distance, node, trail

    trails = {}

    while queue:
        dist, i, j = heapq.heappop(queue)
        if i in trails:
            continue
        trails[i] = j
        if i == v:
            break
        for j in weights[i]:
            if j not in trails:
                heapq.heappush(queue, (dist + weights[i][j], j, i))
    if v in trails:
        rev_path = [v]
        while rev_path[-1] != u:
            rev_path.append(trails[rev_path[-1]])
        return rev_path[::-1]
# assert sat308(sol308())

def sat309(path: List[int], edges=[[0, 11], [0, 7], [7, 5], [0, 22], [11, 22], [11, 33], [22, 33]], u=0, v=33, bound=3):
    assert path[0] == u and path[-1] == v and all([i, j] in edges for i, j in zip(path, path[1:]))
    return len(path) <= bound
def sol309(edges=[[0, 11], [0, 7], [7, 5], [0, 22], [11, 22], [11, 33], [22, 33]], u=0, v=33, bound=3):
    """Find a path from node u to node v, of a bounded length, in the given digraph on vertices 0, 1,..., n."""
    # Dijkstra's algorithm
    import heapq
    from collections import defaultdict
    queue = [(0, u, u)]  # distance, node, trail

    trails = {}
    neighbors = defaultdict(set)
    for (i, j) in edges:
        neighbors[i].add(j)

    while queue:
        dist, i, j = heapq.heappop(queue)
        if i in trails:
            continue
        trails[i] = j
        if i == v:
            break
        for j in neighbors[i]:
            if j not in trails:
                heapq.heappush(queue, (dist + 1, j, i))
    if v in trails:
        rev_path = [v]
        while rev_path[-1] != u:
            rev_path.append(trails[rev_path[-1]])
        return rev_path[::-1]
# assert sat309(sol309())

