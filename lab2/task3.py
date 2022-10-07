class Product(object):
    def __init__(self, price, description, dimension):
        if price > 0:
            self.__price = price
            self.__description = description
            self.__dimension = dimension
        else:
            raise ValueError

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__description

    def get_dimension(self):
        return self.__dimension


class Customer(object):
    def __init__(self, surname, name, patronymic, mobile_phone):
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__mobile_phone = mobile_phone

    def get_surname(self):
        return self.__surname

    def get_name(self):
        return self.__name

    def get_patronymic(self):
        return self.__patronymic

    def get_mobile_phone(self):
        return self.__mobile_phone


class Order(object):
    def __init__(self, customer):
        self.__products = []
        self.__customer = customer

    def add_product(self, product):
        self.__products.append(product)

    def get_list_of_products(self):
        return self.__products

    def get_customer(self):
        return self.__customer

    def get_total_order_value(self):
        total = 0
        for product in self.__products:
            total += product.get_price() * product.get_dimension()

        return total


try:
    product1 = Product(200, "Phone", 5)
    product2 = Product(3000, "TV", 3)

    person = Customer("Zavgod", "Mark", "Sergeevich", "0992032033")

    order = Order(person)

    order.add_product(product1)
    order.add_product(product2)

    list_of_products = order.get_list_of_products()

    print("Name:", order.get_customer().get_name())
    for i in list_of_products:
        print(f"Item: {i.get_description()} | Price: {i.get_price()}$ | Dimension: {i.get_dimension()}")

    print(f"Total price: {order.get_total_order_value()}$")
except ValueError:
    print("ValueError")
