class Result:
    def __init__(self):
        self.__cgpa = 0
    def set_cgpa(self, cgpa):
        if 0 <= cgpa <= 10:
            self.__cgpa = cgpa
        else:
            print("Invalid CGPA")
    def get_cgpa(self):
        return self.__cgpa
student = Result()
student.set_cgpa(8.5)
print("CGPA:", student.get_cgpa())