class Student:
    def details(self, **kwargs):
        for key, value in kwargs.items():
            print(key, ":", value)
s1 = Student()
s1.details(name="Kousic", age=21, course="Python")