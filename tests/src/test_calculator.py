import pytest
from math import isclose
import sys
import os

sys.path.append(os.path.abspath("."))
from src.calculator import Calculator


def test_calculator():
    Calculator()
    assert True


@pytest.mark.parametrize("test_input_a", [None, "qwerty", 1, 1.15, True])
def test_calculator_wrong(test_input_a):
    with pytest.raises(TypeError):
        Calculator(test_input_a)


@pytest.fixture(scope="module", autouse=True)
def get_class_object():
    yield Calculator()


@pytest.mark.parametrize(
    "test_input_a, test_input_b, expected",
    [
        (0, 0, 0),
        (10, -25, -15),
        (-2, -3, -5),
        (5, 3, 8),
        (1585416574651, 468516504186, 2053933078837),
        (
            -3524653413534854165135468848486,
            -3598798768489748658746846879854,
            -7123452182024602823882315728340,
        ),
        (0.0, 0.0, 0.0),
        (1.52, 3.241, 4.761),
        (-2.01, -0.365, -2.375),
        (3.25, -1.25, 2),
        (
            0.000000000000000000000000000000000003,
            0.000000000000000000000000000000000001,
            0.000000000000000000000000000000000004,
        ),
        (3, 1.5, 4.5),
        (True, True, 2),
    ],
)
def test_calculator_addition(test_input_a, test_input_b, expected, get_class_object):
    assert isclose(
        get_class_object.addition(test_input_a, test_input_b), expected, abs_tol=1e-10,
    )


@pytest.mark.parametrize(
    "test_input_a, test_input_b, expected",
    [("A", 1, "A1"), (2, b"1", 3), (None, 1, 1), (2 + 3j, 3 + 2j, 5 + 5j),],
)
def test_calculator_addition_wrong(
    test_input_a, test_input_b, expected, get_class_object
):
    with pytest.raises(TypeError):
        assert isclose(
            get_class_object.addition(test_input_a, test_input_b),
            expected,
            abs_tol=1e-10,
        )


@pytest.mark.parametrize(
    "test_input_a, test_input_b, expected",
    [
        (0, 0, 0),
        (10, -25, 35),
        (-3, -2, -1),
        (5, 3, 2),
        (1585416574651, 468516504186, 1116900070465),
        (
            -3524653413534854165135468848486,
            -3598798768489748658746846879854,
            74145354954894493611378031368,
        ),
        (0.0, 0.0, 0.0),
        (1.52, 3.241, -1.721),
        (-2.01, -0.365, -1.645),
        (3.25, -1.25, 4.5),
        (
            0.000000000000000000000000000000000003,
            0.000000000000000000000000000000000001,
            0.000000000000000000000000000000000002,
        ),
        (3, 1.5, 1.5),
        (True, True, 0),
    ],
)
def test_calculator_subtraction(test_input_a, test_input_b, expected, get_class_object):
    assert isclose(
        get_class_object.subtraction(test_input_a, test_input_b),
        expected,
        abs_tol=1e-10,
    )


@pytest.mark.parametrize(
    "test_input_a, test_input_b, expected",
    [("A", 1, "A-1"), (2, b"1", 1), (None, 1, -1), (2 + 3j, 3 + 2j, -1 + 1j),],
)
def test_calculator_subtraction_wrong(
    test_input_a, test_input_b, expected, get_class_object
):
    with pytest.raises(TypeError):
        assert isclose(
            get_class_object.subtraction(test_input_a, test_input_b),
            expected,
            abs_tol=1e-10,
        )


@pytest.mark.parametrize(
    "test_input_a, test_input_b, expected",
    [
        (0, 0, 0),
        (10, -25, -250),
        (-2, -3, 6),
        (5, 3, 15),
        (1585416574651, 468516504186, 742793831234029022989086),
        (
            -3524653413534854165135468848486,
            -3598798768489748658746846879854,
            12684518363982421976375384113099857928105164810507183371801044,
        ),
        (0.0, 0.0, 0.0),
        (1.52, 3.241, 4.92632),
        (-2.01, -0.365, 0.73365),
        (3.25, -1.25, -4.0625),
        (
            0.000000000000000000000000000000000003,
            0.000000000000000000000000000000000001,
            3e-72,
        ),
        (3, 1.5, 4.5),
        (True, True, 1),
    ],
)
def test_calculator_multiplication(
    test_input_a, test_input_b, expected, get_class_object
):
    assert isclose(
        get_class_object.multiplication(test_input_a, test_input_b),
        expected,
        abs_tol=1e-10,
    )


@pytest.mark.parametrize(
    "test_input_a, test_input_b, expected",
    [("A", 1, "A*1"), (2, b"1", 2), (None, 1, 0), (2 + 3j, 3 + 2j, 13j),],
)
def test_calculator_multiplication_wrong(
    test_input_a, test_input_b, expected, get_class_object
):
    with pytest.raises(TypeError):
        assert isclose(
            get_class_object.multiplication(test_input_a, test_input_b),
            expected,
            abs_tol=1e-10,
        )


@pytest.mark.parametrize(
    "test_input_a, test_input_b, expected",
    [
        (10, -25, -0.4),
        (-2, -3, 0.66666666666),
        (5, 3, 1.66666666666),
        (1585416574651, 468516504186, 3.38390763289),
        (
            -3524653413534854165135468848486,
            -3598798768489748658746846879854,
            0.97939719341,
        ),
        (1.52, 3.241, 0.46899105214),
        (-2.01, -0.365, 5.50684931506),
        (3.25, -1.25, -2.6),
        (
            0.000000000000000000000000000000000003,
            0.000000000000000000000000000000000001,
            3,
        ),
        (3, 1.5, 2),
        (True, True, 1),
    ],
)
def test_calculator_division(test_input_a, test_input_b, expected, get_class_object):
    assert isclose(
        get_class_object.division(test_input_a, test_input_b), expected, abs_tol=1e-10
    )


@pytest.mark.parametrize(
    "test_input_a, test_input_b, expected",
    [
        ("A", 1, "A/1"),
        (2, b"1", 2),
        (None, 1, 0),
        (2 + 3j, 3 + 2j, 0.9230769230769231 + 0.38461538461538464j),
    ],
)
def test_calculator_division_wrong_type(
    test_input_a, test_input_b, expected, get_class_object
):
    with pytest.raises(TypeError):
        assert isclose(
            get_class_object.division(test_input_a, test_input_b),
            expected,
            abs_tol=1e-10,
        )


@pytest.mark.parametrize(
    "test_input_a, test_input_b, expected", [(1, 0, 0), (1.1, 0.0, 0.1),],
)
def test_calculator_division_wrong_value(
    test_input_a, test_input_b, expected, get_class_object
):
    with pytest.raises(ZeroDivisionError):
        assert isclose(
            get_class_object.division(test_input_a, test_input_b),
            expected,
            abs_tol=1e-10,
        )


@pytest.mark.parametrize(
    "test_input_a, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (10, 3628800),
        (20, 2432902008176640000),
        (True, 1),
    ],
)
def test_calculator_factorial(test_input_a, expected, get_class_object):
    assert get_class_object.factorial(test_input_a) == expected


@pytest.mark.parametrize(
    "test_input_a, expected",
    [(2.563, 5.126), ("A", "A"), ("B", "AB"), (None, 1), (2 + 3j, 2 + 6j), (b"3", 6)],
)
def test_calculator_factorial_wrong_type(test_input_a, expected, get_class_object):
    with pytest.raises(TypeError):
        assert get_class_object.factorial(test_input_a) == expected


@pytest.mark.parametrize(
    "test_input_a, expected", [(-1, 1), (-3, -6),],
)
def test_calculator_factorial_wrong_value(test_input_a, expected, get_class_object):
    with pytest.raises(ValueError):
        assert get_class_object.factorial(test_input_a) == expected


@pytest.mark.parametrize(
    "test_input_a, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1.41421356237),
        (3, 1.73205080756),
        (10, 3.16227766016),
        (20, 4.47213595499),
        (True, 1),
    ],
)
def test_calculator_square_root(test_input_a, expected, get_class_object):
    assert isclose(get_class_object.square_root(test_input_a), expected, abs_tol=1e-10)


@pytest.mark.parametrize(
    "test_input_a, expected",
    [("A", "sqrt(A)"), (None, 0), (4 + 9j, 2 + 3j), (b"4", 2)],
)
def test_calculator_square_root_wrong_type(test_input_a, expected, get_class_object):
    with pytest.raises(TypeError):
        assert get_class_object.square_root(test_input_a) == expected


@pytest.mark.parametrize(
    "test_input_a, expected", [(-1, 1j), (-9, 3j),],
)
def test_calculator_square_root_wrong_value(test_input_a, expected, get_class_object):
    with pytest.raises(ValueError):
        assert get_class_object.square_root(test_input_a) == expected
