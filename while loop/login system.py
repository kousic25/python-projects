username = "admin"
password = "1234"
while True:
    u = input("Username: ")
    p = input("Password: ")
    if u == username and p == password:
        print("Welcome")
        break
    else:
        print("Invalid login")