# SCHOOL TIMETABLE
timetable = (
    ("Monday",    "Math",     "Mr. Kumar",  "08:00", "09:00"),
    ("Monday",    "Science",  "Ms. Priya",  "09:00", "10:00"),
    ("Tuesday",   "English",  "Mr. Raj",    "08:00", "09:00"),
    ("Tuesday",   "Math",     "Mr. Kumar",  "09:00", "10:00"),
    ("Wednesday", "Computer", "Ms. Anitha", "08:00", "09:00"),
)

print(f"{'Day':<12} {'Subject':<10} {'Teacher':<14} {'Start':>6} {'End':>6}")
print("-" * 62)
for day, subject, teacher, start, end in timetable:
    print(f"{day:<12} {subject:<10} {teacher:<14} {start:>6} {end:>6}")