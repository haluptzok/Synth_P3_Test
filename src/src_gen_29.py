from typing import List

def sat290(t: str, s="))(Add)some))parens()to()(balance(()(()(me!)(((("):
    for i in range(len(t) + 1):
        depth = t[:i].count("(") - t[:i].count(")")
        assert depth >= 0
    return depth == 0 and s in t
def sol290(s="))(Add)some))parens()to()(balance(()(()(me!)(((("):
    """Add parentheses to the beginning and end of s to make all parentheses balanced"""
    return "(" * s.count(")") + s + ")" * s.count("(")
# assert sat290(sol290())

def sat291(squares: List[List[int]], m=8, n=8):
    k = min(m, n)
    assert all(i in range(m) and j in range(n) for i, j in squares) and len(squares) == k
    return 4 * k == len({t for i, j in squares for t in [('row', i), ('col', j), ('SE', i + j), ('NE', i - j)]})
def sol291(m=8, n=8):
    """Position min(m, n) <= 8 queens on an m x n chess board so that no pair is attacking each other."""
    # brute force
    k = min(m, n)

    from itertools import permutations
    for p in permutations(range(k)):
        if 4 * k == len(
                {t for i, j in enumerate(p) for t in [('row', i), ('col', j), ('SE', i + j), ('NE', i - j)]}):
            return [[i, j] for i, j in enumerate(p)]
# assert sat291(sol291())

def sat292(squares: List[List[int]], m=9, n=9):
    k = min(m, n)
    assert all(i in range(m) and j in range(n) for i, j in squares), "queen off board"
    assert len(squares) == k, "Wrong number of queens"
    assert len({i for i, j in squares}) == k, "Queens on same row"
    assert len({j for i, j in squares}) == k, "Queens on same file"
    assert len({i + j for i, j in squares}) == k, "Queens on same SE diagonal"
    assert len({i - j for i, j in squares}) == k, "Queens on same NE diagonal"
    return True
def sol292(m=9, n=9):
    """
    Position min(m, n) > 8 queens on an m x n chess board so that no pair is attacking each other.
    """
    t = min(m, n)
    ans = []
    if t % 2 == 1:  # odd k, put a queen in the lower right corner (and decrement k)
        ans.append([t - 1, t - 1])
        t -= 1
    if t % 6 == 2:  # do something special for 8x8, 14x14 etc:
        ans += [[i, (2 * i + t // 2 - 1) % t] for i in range(t // 2)]
        ans += [[i + t // 2, (2 * i - t // 2 + 2) % t] for i in range(t // 2)]
    else:
        ans += [[i, 2 * i + 1] for i in range(t // 2)]
        ans += [[i + t // 2, 2 * i] for i in range(t // 2)]
    return ans
# assert sat292(sol292())

def sat293(tour: List[List[int]], m=8, n=8):
    assert all({abs(i1 - i2), abs(j1 - j2)} == {1, 2} for [i1, j1], [i2, j2] in zip(tour, tour[1:])), 'legal moves'
    return sorted(tour) == [[i, j] for i in range(m) for j in range(n)]  # cover every square once
def sol293(m=8, n=8):
    """Find an (open) tour of knight moves on an m x n chess-board that visits each square once."""
    # using Warnsdorff's heuristic, breaking ties randomly
    import random
    for seed in range(100):
        r = random.Random(seed)
        ans = [(0, 0)]
        free = {(i, j) for i in range(m) for j in range(n)} - {(0, 0)}

        def possible(i, j):
            moves = [(i + s * a, j + t * b) for (a, b) in [(1, 2), (2, 1)] for s in [-1, 1] for t in [-1, 1]]
            return [z for z in moves if z in free]

        while True:
            if not free:
                return [[a, b] for (a, b) in ans]
            candidates = possible(*ans[-1])
            if not candidates:
                break
            ans.append(min(candidates, key=lambda z: len(possible(*z)) + r.random()))
            free.remove(ans[-1])
# assert sat293(sol293())

def sat294(seq: List[int], compressed_len=17, text="Hellooooooooooooooooooooo world!"):
    index = [chr(i) for i in range(256)]
    pieces = [""]
    for i in seq:
        pieces.append((pieces[-1] + pieces[-1][0]) if i == len(index) else index[i])
        index.append(pieces[-2] + pieces[-1][0])
    return "".join(pieces) == text and len(seq) <= compressed_len
def sol294(compressed_len=17, text="Hellooooooooooooooooooooo world!"):
    """
    Find a (short) compression that decompresses to the given string for the provided implementation of the
    Lempel-Ziv decompression algorithm from https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch
    """
    # compressed_len is ignored
    index = {chr(i): i for i in range(256)}
    seq = []
    buffer = ""
    for c in text:
        if buffer + c in index:
            buffer += c
            continue
        seq.append(index[buffer])
        index[buffer + c] = len(index) + 1
        buffer = c

    if text != "":
        seq.append(index[buffer])

    return seq
# assert sat294(sol294())

def sat295(words: List[str], num=100, bits=100, dist=34):
    assert len(words) == num and all(len(word) == bits and set(word) <= {"0", "1"} for word in words)
    return all(sum([a != b for a, b in zip(words[i], words[j])]) >= dist for i in range(num) for j in range(i))
def sol295(num=100, bits=100, dist=34):
    """Pack a certain number of binary strings so that they have a minimum hamming distance between each other."""
    import random  # key insight, use randomness!
    r = random.Random(0)
    while True:
        seqs = [r.getrandbits(bits) for _ in range(num)]
        if all(bin(seqs[i] ^ seqs[j]).count("1") >= dist for i in range(num) for j in range(i)):
            return [bin(s)[2:].rjust(bits, '0') for s in seqs]
# assert sat295(sol295())

def sat296(init: List[List[int]], period=3):
    target = {x + y * 1j for x, y in init}  # complex numbers encode live cells

    deltas = (1j, -1j, 1, -1, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j)
    live = target
    for t in range(period):
        visible = {z + d for z in live for d in deltas}
        live = {z for z in visible if sum(z + d in live for d in deltas) in ([2, 3] if z in live else [3])}
        if live == target:
            return t + 1 == period
def sol296(period=3):
    """
    Find a pattern in Conway's Game of Life https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life that repeats
    with a certain period https://en.wikipedia.org/wiki/Oscillator_%28cellular_automaton%29#:~:text=Game%20of%20Life
    """
    # # generate random patterns, slow solution
    # def viz(live):
    #     if not live:
    #         return
    #     a, b = min(z.real for z in live), min(z.imag for z in live)
    #     live = {z - (a + b * 1j) for z in live}
    #     m, n = int(max(z.real for z in live)) + 1, int(max(z.imag for z in live)) + 1
    #     for x in range(m):
    #         print("".join("X" if x + y * 1j in live else "," for y in range(n)))

    import random
    rand = random.Random(1)
    # print(f"Looking for {period}:")
    deltas = (1j, -1j, 1, -1, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j)

    completes = [[x + y * 1j for x in range(n) for y in range(n)] for n in range(30)]

    for _attempt in range(10 ** 5):
        n = rand.randrange(3, 10)
        m = rand.randrange(3, n * n)
        live = set(rand.sample(completes[n], m))
        if rand.randrange(2):
            live.update([-z for z in live])
        if rand.randrange(2):
            live.update([z.conjugate() for z in live])
        memory = {}
        for step in range(period * 10):
            key = sum((.123 - .99123j) ** z for z in live) * 10 ** 5
            key = int(key.real), int(key.imag)
            if key in memory:
                if memory[key] == step - period:
                    # print(period)
                    # viz(live)
                    return [[int(z.real), int(z.imag)] for z in live]
                break
            memory[key] = step
            visible = {z + d for z in live for d in deltas}
            live = {z for z in visible if sum(z + d in live for d in deltas) in range(3 - (z in live), 4)}

    return None  # failed
# assert sat296(sol296())

def sat297(position: List[List[int]], target=[[1, 3], [1, 4], [2, 5]]):
    live = {x + y * 1j for x, y in position}  # complex numbers encode live cells
    deltas = (1j, -1j, 1, -1, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j)
    visible = {z + d for z in live for d in deltas}
    next_step = {z for z in visible if sum(z + d in live for d in deltas) in ([2, 3] if z in live else [3])}
    return next_step == {x + y * 1j for x, y in target}
def sol297(target=[[1, 3], [1, 4], [2, 5]]):
    """
    Given a target pattern in Conway's Game of Life (see https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life ),
    specified by [x,y] coordinates of live cells, find a position that leads to that pattern on the next step.
    """
    # fixed-temperature MC optimization
    TEMP = 0.05
    import random
    rand = random.Random(0)  # set seed but don't interfere with other random uses
    target = {x + y * 1j for x, y in target}
    deltas = (1j, -1j, 1, -1, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j)

    def distance(live):
        visible = {z + d for z in live for d in deltas}
        next_step = {z for z in visible if sum(z + d in live for d in deltas) in ([2, 3] if z in live else [3])}
        return len(next_step.symmetric_difference(target))

    for step in range(10 ** 5):
        if step % 10000 == 0:
            pos = target.copy()  # start with the target position
            cur_dist = distance(pos)

        if cur_dist == 0:
            return [[int(z.real), int(z.imag)] for z in pos]
        z = rand.choice([z + d for z in pos.union(target) for d in deltas])
        dist = distance(pos.symmetric_difference({z}))
        if rand.random() <= TEMP ** (dist - cur_dist):
            pos.symmetric_difference_update({z})
            cur_dist = dist
    print('Failed', len(target), step)
# assert sat297(sol297())

def sat298(moves: List[List[int]], initial_state=[5, 9, 3, 11, 18, 25, 1, 2, 4, 1]):

    def bot_move():  # bot takes objects from the largest heap to make it match the second largest heap
        vals = sorted(state, reverse=True)
        i_largest = state.index(vals[0])  # largest heap
        state[i_largest] -= max(vals[0] - vals[1], 1)  # must take some, take 1 in case of tie

    state = initial_state[:]  # copy
    for i, n in moves:
        assert 0 < n <= state[i], "Illegal move"
        state[i] -= n
        if set(state) == {0}:
            return True  # you won!
        assert any(state), "You lost!"
        bot_move()
def sol298(initial_state=[5, 9, 3, 11, 18, 25, 1, 2, 4, 1]):
    """
    Beat a bot at Nim, a two-player game involving a number of heaps of objects. Players alternate, in each turn
    removing one or more objects from a single non-empty heap. The player who takes the last object wins.
    - initial_state is list of numbers of objects in each heap
    - moves is a list of your moves: [heap, number of objects to take]
    - you play first
    """

    state = initial_state[:]
    moves = []

    def bot_move():  # bot takes objects from the largest heap to make it match the second largest heap
        vals = sorted(state, reverse=True)
        i_largest = state.index(vals[0])  # largest heap
        state[i_largest] -= max(vals[0] - vals[1], 1)  # must take some, take 1 in case of tie

    def losing(h):  # return True if h is a losing state
        xor = 0
        for i in h:
            xor ^= i
        return xor == 0

    def optimal_move():
        assert not losing(state)
        for i in range(len(state)):
            for n in range(1, state[i] + 1):
                state[i] -= n
                if losing(state):
                    moves.append([i, n])
                    return
                state[i] += n
        assert False, "Shouldn't reach hear"

    while True:
        optimal_move()
        if max(state) == 0:
            return moves
        bot_move()
# assert sat298(sol298())

def sat299(transcripts: List[str], max_moves=10):
    COLORS = "ABCDEF"

    def helper(secret: str, transcript=""):
        if transcript.count("\n") == max_moves:
            return False
        guess = min([t for t in transcripts if t.startswith(transcript)], key=len)[-4:]
        if guess == secret:
            return True
        assert all(g in COLORS for g in guess)
        perfect = {c: sum([g == s == c for g, s in zip(guess, secret)]) for c in COLORS}
        almost = sum(min(guess.count(c), secret.count(c)) - perfect[c] for c in COLORS)
        return helper(secret, transcript + f"{guess} {sum(perfect.values())}{almost}\n")

    return all(helper(r + s + t + u) for r in COLORS for s in COLORS for t in COLORS for u in COLORS)
def sol299(max_moves=10):
    """
    Come up with a winning strategy for Mastermind in max_moves moves. Colors are represented by the letters A-F.
    The solution representation is as follows.
    A transcript is a string describing the game so far. It consists of rows separated by newlines.
    Each row has 4 letters A-F followed by a space and then two numbers indicating how many are exactly right
    and how many are right but in the wrong location. A sample transcript is as follows:
    AABB 11
    ABCD 21
    ABDC

    This is the transcript as the game is in progress. The complete transcript might be:
    AABB 11
    ABCD 21
    ABDC 30
    ABDE 40

    A winning strategy is described by a list of transcripts to visit. The next guess can be determined from
    those partial transcripts.
    """
    COLORS = "ABCDEF"

    transcripts = []

    ALL = [r + s + t + u for r in COLORS for s in COLORS for t in COLORS for u in COLORS]

    def score(secret, guess):
        perfect = {c: sum([g == s == c for g, s in zip(guess, secret)]) for c in COLORS}
        almost = sum(min(guess.count(c), secret.count(c)) - perfect[c] for c in COLORS)
        return f"{sum(perfect.values())}{almost}"

    def mastermind(transcript="AABB", feasible=ALL):  # mastermind moves
        transcripts.append(transcript)
        assert transcript.count("\n") <= max_moves
        guess = transcript[-4:]
        feasibles = {}
        for secret in feasible:
            scr = score(secret, guess)
            if scr not in feasibles:
                feasibles[scr] = []
            feasibles[scr].append(secret)
        for scr, secrets in feasibles.items():
            if scr != "40":
                guesser(transcript + f" {scr}\n", secrets)

    def guesser(transcript, feasible):  # guesser moves
        def max_ambiguity(guess):
            by_score = {}
            for secret2 in feasible:
                scr = score(secret2, guess)
                if scr not in by_score:
                    by_score[scr] = 0
                by_score[scr] += 1
            # for OPTIMAL solution, use return max(by_score.values()) + 0.5 * (guess not in feasible) instead of:
            return max(by_score.values())

        # for optimal solution use guess = min(ALL, key=max_ambiguity) instead of:
        guess = min(feasible, key=max_ambiguity)

        mastermind(transcript + guess, feasible)

    mastermind()

    return transcripts
# assert sat299(sol299())

