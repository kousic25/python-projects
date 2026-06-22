products = [
    {"name":"Laptop","tags":{"tech","computer"}},
    {"name":"Phone","tags":{"tech","mobile"}},
    {"name":"Chair","tags":{"furniture"}}]
search = {"tech"}
for product in products:
    if search.issubset(product["tags"]):
        print(product["name"])