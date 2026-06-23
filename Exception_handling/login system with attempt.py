correct_password = "python123"
attempts = 3
while attempts > 0:
    try:
        password = input("Enter password: ")
        if password == "":
            raise ValueError("Password cannot be empty")
        if password != correct_password:
            raise Exception("Wrong password")
        print("Login successful")
        break
    except ValueError as error:
        print(error)
    except Exception as error:
        attempts -= 1
        print(error)
        print("Attempts left:", attempts)
    finally:
        if attempts == 0:
            print("Account locked")