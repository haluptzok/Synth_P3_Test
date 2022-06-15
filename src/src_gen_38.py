from typing import List

def sat380(n: int, a=10000200001):
    return a == n * n and n < 0
def sol380(a=10000200001):
    """Find a negative integer that when squared equals perfect-square a."""
    return -int(a ** 0.5)
# assert sat380(sol380())

def sat381(x: float, a=1020):
    return abs(x ** 2 - a) < 10 ** -3
def sol381(a=1020):
    """Find a number that when squared is close to a."""
    return a ** 0.5
# assert sat381(sol381())

def sat382(x: float, a=1020):
    return abs(x ** 2 - a) < 10 ** -3 and x < 0
def sol382(a=1020):
    """Find a negative number that when squared is close to a."""
    return -a ** 0.5
# assert sat382(sol382())

def sat383(s: str):
    return "Hello " + s == "Hello world"
def sol383():
    """Find a string that when concatenated onto 'Hello ' gives 'Hello world'."""
    return "world"
# assert sat383(sol383())

def sat384(s: str):
    return "Hello " + s[::-1] == "Hello world"
def sol384():
    """Find a string that when reversed and concatenated onto 'Hello ' gives 'Hello world'."""
    return "world"[::-1]
# assert sat384(sol384())

def sat385(x: List[int]):
    return len(x) == 2 and sum(x) == 3
def sol385():
    """Find a list of two integers whose sum is 3."""
    return [1, 2]
# assert sat385(sol385())

def sat386(s: List[str]):
    return len(set(s)) == 1000 and all((x.count("a") > x.count("b")) and ('b' in x) for x in s)
def sol386():
    """Find a list of 1000 distinct strings which each have more 'a's than 'b's and at least one 'b'."""
    return ["a" * (i + 2) + "b" for i in range(1000)]
# assert sat386(sol386())

def sat387(n: int):
    return str(n * n).startswith("123456789")
def sol387():
    """Find an integer whose perfect square begins with 123456789 in its decimal representation."""
    return int(int("123456789" + "0" * 9) ** 0.5) + 1
# assert sat387(sol387())

