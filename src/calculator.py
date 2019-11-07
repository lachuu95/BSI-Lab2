from math import factorial, sqrt


class Calculator:
    def __init__(self):
        pass

    def addition(self, a, b):
        self.__check_pair_number(a, b)
        return a + b

    def subtraction(self, a, b):
        self.__check_pair_number(a, b)
        return a - b

    def multiplication(self, a, b):
        self.__check_pair_number(a, b)
        return a * b

    def division(self, a, b):
        self.__check_pair_number(a, b)
        return a / b

    def factorial(self, a):
        if not isinstance(a, int):
            raise TypeError(f"Błędny typ danych, {a} jest {type(a)}. Oczekiwano int.")
        elif a >= 0:
            return factorial(a)
        else:
            raise ValueError("Podana liczba musi być większa lub równa 0.")

    def square_root(self, a):
        self.__check_number(a)
        if a >= 0:
            return sqrt(a)
        else:
            raise ValueError("Podana liczba musi być większa lub równa 0.")

    def __check_pair_number(self, x, y):
        self.__check_number(x)
        self.__check_number(y)

    def __check_number(self, x):
        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError(
                f"Błędny typ danych, {x} jest {type(x)}. Oczekiwano int lub float."
            )

