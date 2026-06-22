students = [
    {"name":"Alex","dept":"CS"},
    {"name":"John","dept":"IT"},
    {"name":"Sam","dept":"CS"}
]
groups = {}
for student in students:
    dept = student["dept"]
    if dept not in groups:
        groups[dept] = []
    groups[dept].append(student["name"])
print(groups)