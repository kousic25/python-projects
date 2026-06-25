class Employee:
    def __init__(self):
        self.names = ["hari","hema","kousic"]
    def generate_email(self):
        for name in self.names:
            email = name + "@company.com"
            yield email
emp = Employee()
for email in emp.generate_email():
    print(email)