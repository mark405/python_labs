class Product(object):
    def __init__(self, price, description, size):
        self.__price = price
        self.__description = description
        self.__size = size

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__description

    def get_size(self):
        return self.__size


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
    def __init__(self, product_list, customer):
        self.__product_list = product_list
        self.__customer = customer

    def get_product_list(self):
        return self.__product_list

    def get_customer(self):
        return self.__customer

    def get_whole_price(self):
        result = 0
        for i in self.__product_list:
            result += i.get_price() * i.get_size()

        return result


product1 = Product(200, "Phone", 5)
product2 = Product(3000, "TV", 3)

person = Customer("Zavgod", "Mark", "Sergeevich", "0992032033")

list_of_products = [product1, product2]

order = Order(list_of_products, person)

print(order.get_whole_price())
