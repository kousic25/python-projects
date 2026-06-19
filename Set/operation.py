student_A = {
    "Python",
    "Java",
    "SQL",
    "HTML"
}
student_B = {"Python","C++","SQL","JavaScript"}
all_courses = student_A | student_B
common_courses = student_A & student_B
only_A_knows = student_A - student_B
only_B_knows = student_B - student_A
print("All courses:", all_courses)
print("Common courses:", common_courses)
print("Only Student A knows:", only_A_knows)
print("Only Student B knows:", only_B_knows)