restaurants = {
    "PizzaShop": {"ratings":[5,4,5,3] },
    "BurgerShop": {"ratings":[4,4,5]}}
for name, data in restaurants.items():
    ratings = data["ratings"]
    avg = sum(ratings)/len(ratings)
    if avg >= 4:
        data["review"] = "Excellent"
    else:
        data["review"] = "Average"
print(restaurants)