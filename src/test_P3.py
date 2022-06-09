from src_P3 import *

from typing import List

def f1(s: str):
    return "Hello " + s == "Hello world"

# def g1():
#     return "world"

def test_g1():
    assert f1(g1())

def f2(s: str):
    return "Hello " + s[::-1] == "Hello world"

def g2():
    return "world"[::-1]

def test_g2():
    assert f2(g2())

def f3(x: List[int]):
    return len(x) == 2 and sum(x) == 3

def g3():
    return [1, 2]

def test_g3():
    assert f3(g3())

def f4(s: List[str]):
    return len(set(s)) == 1000 and all((x.count("a") > x.count("b")) and ('b' in x) for x in s)

def g4():
    return ["a"*(i+2)+"b" for i in range(1000)]

def test_g4():
    assert f4(g4())

def f5(n: int):
    return str(n * n).startswith("123456789")

def g5():
    return int(int("123456789" + "0"*9) ** 0.5) + 1

def test_g5():
    assert f5(g5())


# import math
# def test_sqrt():
#     num = 25
#     assert math.sqrt(num) == 5

# def testsquare():
#     num = 7
#    assert 7 * 7 == 49

