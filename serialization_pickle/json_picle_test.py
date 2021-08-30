import jsonpickle


class Thing:
    def __init__(self, value):
        self.v = value


class Class1:
    def __init__(self, class2):
        self.class2 = class2


class Class2:
    def __init__(self, class1):
        self.class1 = class1


def first_test():
    a = Thing(["a", 1, 1.2123231, complex(1, 1), [1, 0, 0]])
    frozen = jsonpickle.encode(obj, make_refs=True)
    print(frozen)
    thawed = jsonpickle.decode(frozen)
    print("isinstance(thawed, Thing):", isinstance(thawed, Thing))
    print("isinstance(thawed.v[3],complex)", isinstance(thawed.v[3], complex))
    print("obj == thawed:", obj == thawed)


def cross_links():
    a = Class1(None)
    b = Class2(a)

    a.class2 = b

    pickled = jsonpickle.encode(a)
    print(pickled)
    thawed = jsonpickle.decode(pickled)

    print("isinstance(thawed, Class1):", isinstance(thawed, Class1))


def outher_class():
    from outher_class import OutherClass
    a = OutherClass(["a", 1, 1.2123231, complex(1, 1), [1, 0, 0]])
    pickled = jsonpickle.encode(a)
    print(pickled)
    thawed = jsonpickle.decode(pickled)

    print("isinstance(thawed, OutherClass):", isinstance(thawed, OutherClass))


def old_version_class():
    launch_time = 1

    with open("launch_time.txt", mode="r") as f:
        s = f.read()
        if s != "":
            launch_time = int(s)
        launch_time = launch_time + 1
    with open("launch_time.txt", mode="w") as f:
        f.write(str(launch_time))
    file_path = "some_class.json"
    log = "old_version_class.log"
    a = Thing(["a", 1, 1.2123231, complex(1, 1), [1, 0, 0]])

    def write(o):
        with open(file_path, mode="w") as file:
            frozen = jsonpickle.encode(o, make_refs=True)
            file.write(frozen)

    def read():
        with open(file_path, mode="r") as file:
            s = file.read()
            return jsonpickle.decode(s)

    with open(log, mode="a") as log_file:
        if launch_time % 2 != 0:
            write(a)
            log_file.write(f"number of launch: {launch_time}\n" +
                           "Class have pickled\nNow change path of inner struct of class or delete it or do nothing\n")
        else:
            b = read()
            log_file.write(f"number of launch: {launch_time}\nisinstance(b,Thing): {isinstance(b, Thing)}\n\n\n")


def main():
    # first_test()
    # cross_links()
    # outher_class()
    old_version_class()


if __name__ == '__main__':
    main()
