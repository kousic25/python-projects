orders = (
    ("Pizza", 10),
    ("Burger", 20),
    ("Coffee", 30)
)
best_item = ""
max_sales = 0
for item, quantity in orders:
    if quantity > max_sales:
        max_sales = quantity
        best_item = item
print("Best Selling:", best_item)