try:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    assert name != "", "Name cannot be empty"
    if age < 5:
        raise ValueError("Age too small")
    print("Registration successful")
except AssertionError as error:
    print("Problem:", error)
except ValueError as error:
    print("Problem:", error)