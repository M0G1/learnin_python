import numpy as np


def enumeration():
    letters = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя"
    let_enum = enumerate(letters, start=1)
    print(*list(let_enum), sep="\n")


def compile_():
    str_commands = \
        """
x = 1
z = 2
print(f"{x} + {z} = {x + z}")
        """

    print("We will execute code:")
    print(str_commands)
    print("result:")
    first = compile(str_commands, "in this case any str", "exec")
    exec(first)

    expression_to_evaluate = "2 ** 10 - 1"
    print("\nWe will execute expression:", expression_to_evaluate)
    second = compile(expression_to_evaluate, "There is filename needed", "eval")
    print("result:", eval(second))


def callable_():
    "https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-callable/"
    func = lambda x: str(x) + "  "
    print("lambda function is " + ("" if callable(func) else "not ") + "callable")
    arr = np.array(range(5))
    print("numpy array is " + ("" if callable(arr) else "not ") + "callable")


def arg_mutable(l: list = []):
    l.append(len(l))
    print(l)


def arg_save_test():
    arg_mutable()
    arg_mutable()


def main():
    # enumeration()
    # compile_()
    # callable_()
    arg_save_test()


if __name__ == '__main__':
    main()
