import math


class Rational:
    def __init__(self, nominator=1, denominator=1):
        if isinstance(nominator, int) and isinstance(denominator, int) and denominator != 0:
            self.__nominator = nominator
            self.__denominator = denominator

            self.__reduce()
        else:
            raise ValueError

    def __reduce(self):
        div = math.gcd(self.__nominator, self.__denominator)
        self.__nominator = self.__nominator // div
        self.__denominator = self.__denominator // div

    @property
    def nominator(self):
        return self.__nominator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f"{self.__nominator} / {self.__denominator}"

    def get_result(self):
        return self.__nominator / self.__denominator

    def __add__(self, other):
        nominator = self.__nominator * other.denominator + self.denominator * other.nominator
        denominator = self.__denominator * other.denominator

        return Rational(nominator, denominator)

    def __sub__(self, other):
        nominator = self.__nominator * other.denominator - self.denominator * other.nominator
        denominator = self.__denominator * other.denominator

        return Rational(nominator, denominator)

    def __mul__(self, other):
        nominator = self.__nominator * other.nominator
        denominator = self.__denominator * other.denominator

        return Rational(nominator, denominator)

    def __truediv__(self, other):
        nominator = self.__nominator * other.denominator
        denominator = self.__denominator * other.nominator

        return Rational(nominator, denominator)

    def __lt__(self, other):
        result = self - other

        if result.nominator < 0:
            return True

        return False

    def __le__(self, other):
        result = self - other

        if result.nominator <= 0:
            return True

        return False

    def __eq__(self, other):
        result = self - other

        if result.nominator == 0:
            return True

        return False

    def __ne__(self, other):
        result = self - other

        if result.nominator != 0:
            return True

        return False

    def __gt__(self, other):
        result = self - other

        if result.nominator > 0:
            return True

        return False

    def __ge__(self, other):
        result = self - other

        if result.nominator >= 0:
            return True

        return False


try:

    r1 = Rational(4, 10)

    r2 = Rational(2, 5)

    print(r1 / r2)
except ValueError:
    print("ValueError")
