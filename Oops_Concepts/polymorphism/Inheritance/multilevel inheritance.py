class Person:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print("Name:", self.name)
class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no
    def show_roll(self):
        print("Roll No:", self.roll_no)
class CollegeStudent(Student):
    def __init__(self, name, roll_no, department):
        super().__init__(name, roll_no)
        self.department = department
    def show_department(self):
        print("Department:", self.department)
s = CollegeStudent("Kousic", 101, "Computer Science")
s.show_name()
s.show_roll()
s.show_department()