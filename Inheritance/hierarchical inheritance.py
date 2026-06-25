class Employee:
    def __init__(self, name):
        self.name = name
    def login(self):
        print(f"{self.name} Logged In")
class Developer(Employee):
    def write_code(self):
        print("Writing Code")
class Tester(Employee):
    def test_application(self):
        print("Testing Application")
class Manager(Employee):
    def conduct_meeting(self):
        print("Conducting Meeting")
dev = Developer("Hari")
tester = Tester("Hema")
manager = Manager("Rahul")
dev.login()
dev.write_code()
tester.login()
tester.test_application()
manager.login()
manager.conduct_meeting()