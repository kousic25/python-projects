balance = 50000
def checkbalance():
    return balance
def deposit(amount):
    global balance
    balance += amount
    return "Deposited Successfully"
def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        return "Withdraw Successful"
    return "Insufficient Balance"
print(checkbalance())
print(deposit(10000))
print(withdraw(15000))
print(checkbalance())