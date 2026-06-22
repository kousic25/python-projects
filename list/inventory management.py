inventory = [
    ["Laptop",5],
    ["Phone",0],
    ["Mouse",10]]
for item in inventory:
    if item[1] == 0:
        print(item[0],"Out of Stock")