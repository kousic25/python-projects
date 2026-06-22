accounts = {
    1001:{"name":"Kousic","balance":10000 },
    1002:{"name":"Alex","balance":15000}}
accounts[1001]["balance"] += 5000
amount = 3000
if accounts[1001]["balance"] >= amount:
    accounts[1001]["balance"] -= amount
else:
    print("Insufficient balance")
for acc, data in accounts.items():
    print(
        acc,
        data["name"],
        data["balance"] )