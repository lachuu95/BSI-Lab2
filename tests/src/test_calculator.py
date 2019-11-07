import pytest
import sys
import os

sys.path.append(os.path.abspath("."))
from src.calculator import Calculator


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
        (3,1.5,4.5),
    ],
)
def test_calculator_addition(test_input_a, test_input_b, expected):
    calc = Calculator()
    assert calc.addition(test_input_a, test_input_b) == expected

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
        (3,1.5,1.5),
    ],
)
def test_calculator_subtraction(test_input_a, test_input_b, expected):
    calc = Calculator()
    assert calc.subtraction(test_input_a, test_input_b) == expected
