class BinaryTree:

    def __init__(self, kod, price, number_of_items):

        self.left = None
        self.right = None
        self.kod = kod
        self.price = price
        self.number_of_items = number_of_items

    def insert(self, kod, price, number_of_items):
        # Compare the new value with the parent node
        if self.kod:
            if kod < self.kod:
                if self.left is None:
                    self.left = BinaryTree(kod, price, number_of_items)
                else:
                    self.left.insert(kod, price, number_of_items)
            elif kod > self.kod:
                if self.right is None:
                    self.right = BinaryTree(kod, price, number_of_items)
                else:
                    self.right.insert(kod, price, number_of_items)
        else:
            self.kod = kod
            self.price = price
            self.number_of_items = number_of_items

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(f"№{self.kod} - {int(self.number_of_items) * float(self.price)}$"),
        if self.right:
            self.right.print_tree()


# Use the insert method to add nodes
tree = BinaryTree(None, None, None)
while True:

    kod_input = input("Enter kod: ")
    price_input = input("Enter price: ")
    number_of_items_input = input("Enter number: ")

    print(len(kod_input))

    list_of_input = [kod_input, price_input, number_of_items_input]

    status = True

    for i in list_of_input:
        if not i:
            status = False

    if not status:
        break

    tree.insert(kod_input, price_input, number_of_items_input)

try:
    tree.print_tree()
except TypeError:
    print("TypeError")

#root.insert("203", 303, 30)
#root.insert("202", 303, 30)
#root.insert("2002", 922, 20)
#root.insert("202", 923, 9)


