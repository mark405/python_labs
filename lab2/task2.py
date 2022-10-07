import math


class Rational(object):
    def __init__(self, nominator=1, denominator=1):
        if isinstance(nominator, int) and isinstance(denominator, int) and denominator != 0:
            div = math.gcd(nominator, denominator)
            self.__nominator = nominator // div
            self.__denominator = denominator // div
        else:
            raise ValueError

    def get_str_result(self):
        return f"{self.__nominator} / {self.__denominator}"

    def get_result(self):
        return self.__nominator / self.__denominator


try:
    rat = Rational(0, 2)
    print(rat.get_str_result())
    print(rat.get_result())
except ValueError:
    print("ValueError")

