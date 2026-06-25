def account_lock(func):
    def wrapper(self, password):
        if self.attempts >= 3:
            print("Account Locked")
            return
        return func(self, password)
    return wrapper
class LoginSystem:
    def __init__(self):
        self.password = "admin123"
        self.attempts = 0
    @account_lock
    def login(self, password):
        if password == self.password:
            print("Login Successful")
        else:
            self.attempts += 1
            print("Wrong Password")
user = LoginSystem()
user.login("123")
user.login("abc")
user.login("xyz")
user.login("admin123")