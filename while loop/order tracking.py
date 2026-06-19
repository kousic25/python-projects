status = "preparing"
while status != "delivered":
    print("Order status:", status)
    status = input("Update status (preparing / on the way / delivered): ")
print("Enjoy your meal!")