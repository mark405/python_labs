class Rational(object):
    def __init__(self, nominator=1, denominator=1):

        self.__nominator = int(nominator)
        self.__denominator = int(denominator)

        try:
            while nominator % denominator != 0:
                old_nominator = nominator
                old_denominator = denominator

                nominator = old_denominator
                denominator = old_nominator % old_denominator

            self.__nominator //= denominator
            self.__denominator //= denominator
        except Exception as e:
            print("Invalid argument - ", e)

    def print_fraction(self):
        print(self.__nominator, "/", self.__denominator)

    def print_fraction_in_float_form(self):
        print(self.__nominator / self.__denominator)


rat = Rational(2, 10)

rat.print_fraction()
rat.print_fraction_in_float_form()