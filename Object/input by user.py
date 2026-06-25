class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
name = input("Enter name: ")
salary = int(input("Enter salary: "))
emp = Employee(name, salary)
emp.display()