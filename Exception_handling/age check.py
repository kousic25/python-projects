try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Invalid age")
    print("Your age is:", age)
except ValueError as error:
    print(error)