"""
Some examples of using type in python 3.9
And my own test
"""
from typing import Any, TypeVar, NewType, NamedTuple, Callable
import time

import numpy as np


def sum_(vector: list[float]):
    sum_val: float = 0
    for val in vector:
        sum_val += val
    return sum_val


TYPE_FILE = "game_with_types.txt"
TIME_FORMAT = "%Y.%m.%d %H:%M:%S"


def main():
    with open(TYPE_FILE, "a") as file:
        print(f"\nTime of starting {time.strftime(TIME_FORMAT, time.localtime())}", file=file)
        vec = [1, 2, 3, 4, 5]
        print(f"sum of {vec} is {sum_(vec)}", file=file)

        d: dict[int, str] = dict()
        d[2] = "5"
        d["2"] = 2
        print("What is going on? It is working or not?", file=file)
        print(d, file=file)
        print("This dictionary declare like dict[int, str]", file=file)
        # There is needed classes List, Dict from typing

        BeastId = NewType("BeastId", int)
        print(BeastId(666), file=file)

        T = TypeVar("T")
        G = TypeVar("G")
        Pair = NamedTuple("Pair", (("var1", T), ("var2", G)))
        print("New Type", Pair, file=file)

        # https://stackoverflow.com/questions/61569324/type-annotation-for-callable-that-takes-kwargs
        def fu(func: Callable) -> Callable:
            def ans(*args, **kwargs):
                print("I'm a decorator", file=file)
                func(*args, **kwargs)
                print("The creator have remembered gagna style song")

            return ans

        foo = fu(print)
        foo("Decorator + typing")

        # ====================================== NumPy =========================================================
        # https://numpy.org/devdocs/reference/arrays.dtypes.html#arrays-dtypes
        vec_c = np.dtype((np.complex, (2,)))

        print("New NumPy type" + str(vec_c), file=file)


if __name__ == '__main__':
    main()
