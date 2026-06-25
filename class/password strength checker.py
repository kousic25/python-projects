class Password:
    def __init__(self, password):
        self.password = password
    def check(self):
        if len(self.password) >= 8:
            print("Strong Password")
        else:
            print("Weak Password")
p1 = Password("python123")
p1.check()