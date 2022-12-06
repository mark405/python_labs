from datetime import datetime


class Pizza:
    __pizzas = {
        "Carbonara": {"price": 200, "ingredients": ["meet", "cheese"]},
        "Myslyvska": {"price": 210, "ingredients": ["cheese", "kovbasa"]},
        "4 cheeses": {"price": 240, "ingredients": ["cheese"]},
        "Margarita": {"price": 140, "ingredients": ["cheese", "tomato"]},
        "BBQ": {"price": 200, "ingredients": ["bbq", "cheese"]},
        "peperoni": {"price": 190, "ingredients": ["sausage", "kovbasa", "tomato"]},
        "Chicken and Ananas": {"price": 200, "ingredients": ["chicken", "ananas"]},
    }

    def __init__(self, pizza_name):
        if not pizza_name:
            raise ValueError("Pizza must have a name")
        if pizza_name not in self.__pizzas:
            raise ValueError(f"Pizza with this name doesn't exists - {pizza_name}")

        self.__pizza_name = pizza_name
        self.__ingredients = self.__pizzas[pizza_name]["ingredients"]
        self.__price = self.__pizzas[pizza_name]["price"]

    @property
    def name(self):
        return self.__pizza_name

    @property
    def ingredients(self):
        return self.__ingredients

    @property
    def price(self):
        return self.__price

    def add_ingredients(self, ingredients):
        self.__pizzas[self.__pizza_name]["ingredients"].append(ingredients)

    def __str__(self):
        return f"{self.name} with {self.ingredients} for {self.price}"


def get_today():
    return datetime.now().strftime('%A')


class PizzaOfTheDay(Pizza):
    __pizzas = {
        "Monday": "Carbonara",
        "Tuesday": "Myslyvska",
        "Wednesday": "4 cheeses",
        "Thursday": "Margarita",
        "Friday": "BBQ",
        "Saturday": "Chicken and Ananas",
        "Sunday": "peperoni",
    }

    def __init__(self):
        super().__init__(self.__pizzas[get_today()])


class Customer:
    def __init__(self, name, surname):
        if not name or not surname:
            raise ValueError("Name or surname haven't been recognised")
        self.__name = name
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    def __str__(self):
        return f"{self.name} {self.surname}"


class Order:
    def __init__(self, customer, pizzas):
        self.__pizzas = []
        self.__customer = customer

        for i in pizzas:
            self.add_pizza(i)

    def add_pizza(self, pizza):
        self.__pizzas.append(pizza)

    @property
    def customer(self):
        return self.__customer

    @property
    def pizzas(self):
        message = ""
        for i in self.__pizzas:
            message += str(i) + " "

        return message

    def __str__(self):
        return f"{self.customer} ordered {self.pizzas}"


try:
    customer1 = Customer("mark", "zavgod")
    pizza1 = Pizza("Carbonara")
    pizza2 = PizzaOfTheDay()

    a = [pizza1, pizza2]
    order1 = Order(customer1, a)
    order1.add_pizza(pizza1)
    print(order1)
except ValueError as verr:
    print(verr)
