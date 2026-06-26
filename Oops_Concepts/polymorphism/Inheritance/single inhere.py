class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def show_product(self):
        print(f"Product: {self.name}")
        print(f"Price: ₹{self.price}")
class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty
    def show_warranty(self):
        print(f"Warranty: {self.warranty} Years")
mobile = Electronics("iPhone", 80000, 2)
mobile.show_product()
mobile.show_warranty()