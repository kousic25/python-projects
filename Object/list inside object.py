class ShoppingList:
    def __init__(self, items):
        self.items = items
    def display(self):
        for item in self.items:
            print(item)
mylist = ShoppingList(["Laptop", "Mouse", "Keyboard"])
mylist.display()