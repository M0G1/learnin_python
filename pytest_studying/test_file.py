import pytest


@pytest.fixture()
def setup_teardown():
    with open("cov.html", mode="w") as f:
        print("\nSetup")
        yield f
    # automatic close


# ========================= SIMPLE TESTS =====================================

@pytest.fixture(autouse=True)  # implicit(неявный) fixture call - bad
def setup2():
    print("\nSetup2")


@pytest.fixture()
def setup():
    print("\nSetup")


def test1():
    print("Executing test1!")
    assert True


def test2(setup):
    print("Executing test2!")
    assert True


# ========================= SCOPE DEFINING ====================================

@pytest.fixture(scope="session", autouse=True)
def setup_session():
    """
    scope – The scope for which this fixture is shared;
    one of "function" (default),
    "class", "module", "package" or "session".
 """

    print("\nSetup session")


@pytest.fixture(scope="module", autouse=True)
def setup_module():
    print("\nSetup module")


# ======================= PARAMETERS IN TESTING ===============================

@pytest.fixture(params=[1, 2])
def setup_data(request):
    return request.param


def test_with_data(setup_data):
    print("I got ", setup_data)


@pytest.mark.parametrize(
    ("value", "expected"),
    [  # one tuple - one set of parameters for test function
        (1, 1),
        (2, 2),
        # (3, None)
    ]
)
def test_parametrized(value, expected):
    assert value == expected


note1 = """

https://www.youtube.com/playlist?list=PLQC2_0cDcSKBHamFYA6ncnc_fYuEQUy0s
(тестирование)

mock
- подмена настоящих объектов на mock объектов
mock при вызове атрибутов и методов тоже возвращается mock объект, если
он не определен.

Можно запихнуть в mock то, что необходимо в проверках и то что влияет на
логику,
когда нужно проверить возвращаемое значение.

"""


# ======================= FLOAT NUMBER COMPARE ================================

# # FAILING TEST
# def test_bad_float_compare():
#     assert (0.1 + 0.2) == 0.3


def test_good_float_compare():
    val = 0.1 + 0.2
    assert val == pytest.approx(0.3)


def test_except_exception():
    # assert it if code throws exception
    with pytest.raises(ValueError):
        raise ValueError()


note2 = """
testpaths. After the command "path" "path" ... "path" 
"""
