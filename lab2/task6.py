class Node:

    def __init__(self, kod, price, number):

        self.left = None
        self.right = None
        self.kod = kod
        self.price = price
        self.number = number

    def insert(self, kod, price, number):
        if self.kod:
            if kod < self.kod:
                if self.left is None:
                    self.left = Node(kod, price, number)
                else:
                    self.left.insert(kod, price, number)
            elif kod > self.kod:
                if self.right is None:
                    self.right = Node(kod, price, number)
                else:
                    self.right.insert(kod, price, number)
        else:
            self.kod = kod
            self.price = price
            self.number = number

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(f"{self.kod} - {self.number * self.price}$"),
        if self.right:
            self.right.print_tree()


root = Node(None, None, None)

n = int(input("How many nodes?"))

try:

    for i in range(n):
        kod_input = int(input("Enter kod: "))
        price_input = int(input("Enter price: "))
        number_of_items_input = int(input("Enter number: "))

        root.insert(kod_input, price_input, number_of_items_input)

    root.print_tree()
except TypeError:
    print("TypeError")
except ValueError:
    print("ValueError")

