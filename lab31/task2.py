class Composition:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    @property
    def name(self):
        return self.__name

    @property
    def quantity(self):
        return self.__quantity

    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError

        self.__name = name

    @quantity.setter
    def quantity(self, quantity):
        if quantity <= 0:
            raise ValueError

        self.__quantity = quantity

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError

        self.__price = price

    def __gt__(self, other):
        if isinstance(other, Composition):
            return self.price > other.price

    def __ge__(self, other):
        if isinstance(other, Composition):
            return self.price >= other.price

    def __lt__(self, other):
        if isinstance(other, Composition):
            return self.price < other.price

    def __le__(self, other):
        if isinstance(other, Composition):
            return self.price <= other.price

    def __eq__(self, other):
        if isinstance(other, Composition):
            return self.price == other.price

    def __str__(self):
        return f"{self.name} in quantity of {self.quantity} for {self.price}$"


class Request:
    def __init__(self):
        self.__name_of_compositions_list = []
        self.__index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.__name_of_compositions_list):
            self.index += 1
            return self.__name_of_compositions_list[self.index - 1]

        raise StopIteration

    def __add__(self, other):
        if isinstance(other, str):
            self.__name_of_compositions_list.append(other)
            return self.__name_of_compositions_list

        if isinstance(other, Request):
            for request in other:
                self.__name_of_compositions_list.append(request)
                return self.__name_of_compositions_list

        raise ValueError



class Report:
    def __init__(self, composition_list, request):
        self.__composition_list = composition_list
        self.__request = request

    @property
    def list(self):
        return self.__composition_list

    @property
    def request(self):
        return self.__request

    def __str__(self):
        stock_list = [el for el in self.__composition_list if self.__is_composition_in_request(el.name)]

        result = f"For request of {self.__request}:\n"
        for comp in stock_list:
            result += f"\t{comp} is available\n"

        return result

    def __is_composition_in_request(self, name):
        for re in self.__request:
            if re == name:
                return True

        return False


try:
    c1 = Composition("a", 5, 6)
    c2 = Composition("b", 1, 2)
    c3 = Composition("c", 3, 4)
    c4 = Composition("d", 5, 4)
    c5 = Composition("e", 1, 2)

    comp_list = [c1, c2, c3, c4, c5]

    r1 = Request()
    r1 += "a"
    r1 += "b"
    r1 += "g"

    report = Report(comp_list, r1)

    print(report)
except ValueError:
    print("ValueError")
