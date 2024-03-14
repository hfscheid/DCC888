from lang import *


def test_min(m, n):
    """
    Stores in the variable 'answer' the minimum of 'm' and 'n'

    Examples:
        >>> test_min(3, 4)
        3
        >>> test_min(4, 3)
        3
    """
    env = Env({"m": m, "n": n, "x": m, "zero": 0})
    m_min = Add("answer", "m", "zero")
    n_min = Add("answer", "n", "zero")
    p = Lth("p", "n", "m")
    b = Bt("p", n_min, m_min)
    p.add_next(b)
    interp(p, env)
    return env.get("answer")


def test_fib(n):
    """
    Stores in the variable 'answer' the n-th number of the Fibonacci sequence.

    Examples:
        >>> test_fib(2)
        2
        >>> test_fib(3)
        3
        >>> test_fib(6)
        13
    """
    env = Env({"c": 0, "N": n, "fib0": 0, "fib1": 1, "zero": 0, "one": 1})
    i0 = Lth("p", "c", "N")
    i2 = Add("aux", "fib1", "zero")
    i3 = Add("fib1", "aux", "fib0")
    i4 = Add("fib0", "aux", "zero")
    i5 = Add("c", "c", "one")
    i6 = Add("answer", "fib1", "zero")
    i1 = Bt("p", i2, i6)
    i0.add_next(i1)
    i2.add_next(i3)
    i3.add_next(i4)
    i4.add_next(i5)
    i5.add_next(i0)
    interp(i0, env)
    return env.get("answer")


def test_min3(x, y, z):
    """
    Stores in the variable 'answer' the minimum of 'x', 'y' and 'z'

    Examples:
        >>> test_min3(3, 4, 5)
        3
        >>> test_min3(5, 4, 3)
        3
    """
    # TODO: Implement this method

    # 0: lt x_lt_y x y
    # 1: bt x_lt_y 2 5
    # 2: lt x_lt_y_and_z x z
    # 3: bt x_lt_y_and_z 4 8
    # 4: add answer x 0
    # 5: lt y_lt_z y z
    # 6: bt y_lt_z 7 8
    # 7: add answer y 0
    # 8: add answer z 0

    env = Env({"x": x, "y": y, "z": z, "zero": 0})
    i0 = Lth("x_lt_y", "x", "y")
    i2 = Lth("x_lt_y_and_z", "x", "z")
    i4 = Add("answer", "x", "zero")
    i5 = Lth("y_lt_z", "y", "z")
    i7 = Add("answer", "y", "zero")
    i8 = Add("answer", "z", "zero")
    i1 = Bt("x_lt_y", i2, i5)
    i3 = Bt("x_lt_y_and_z", i4, i8)
    i6 = Bt("y_lt_z", i7, i8)

    i0.add_next(i1)
    i2.add_next(i3)
    i5.add_next(i6)
    interp(i0, env)
    return env.get("answer")




def test_div(m, n):
    """
    Stores in the variable 'answer' the integer division of 'm' and 'n'.

    Examples:
        >>> test_div(30, 4)
        7
        >>> test_div(4, 3)
        1
        >>> test_div(1, 3)
        0
    """
    # TODO: Implement this method

    # i0: lth inc m n
    # i1: add answer inc
    # i2: sub m m n
    # i3: bt inc 0 4
    # i4: add answer inc

    env = Env({"m": m, "n": n, "minus": -1, "answer": 0})
    i0 = Mul("minus_n", "n", "minus")
    i1 = Lth("inc", "n", "m") 
    i2 = Add("answer", "answer", "inc")
    i3 = Add("m", "m", "minus_n")
    i5 = Add("answer", "answer", "inc")
    i4 = Bt("inc", i0, i5)
    i0.add_next(i1)
    i1.add_next(i2)
    i2.add_next(i3)
    i3.add_next(i4)
    i4.add_next(i5)
    interp(i0, env)
    return env.get("answer")


def test_fact(n):
    """
    Stores in the variable 'answer' the factorial of 'n'.

    Examples:
        >>> test_fact(3)
        6
    """
    # TODO: Implement this method
    # i0: mul answer answer n
    # i1: add n n dec
    # i2: lt repeat 1 n
    # i3: bt repeat i0 i4
    # i4: add n n dec

    env = Env({"n": n, "dec": -1, "answer": 1, "one": 1})
    i0 = Mul("answer", "answer", "n")
    i1 = Add("n", "n", "dec")
    i2 = Lth("repeat", "one", "n")
    i4 = Add("n", "n", "dec")
    i3 = Bt("repeat", i0, i4)
    i0.add_next(i1)
    i1.add_next(i2)
    i2.add_next(i3)
    interp(i0, env)
    return env.get("answer")
