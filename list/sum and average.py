 #Sum and average
marks = [85, 90, 78, 92, 88, 76, 95]
total = 0
for m in marks:
    total += m
avg    = total / len(marks)
high   = max(marks)
low    = min(marks)
print(f"Marks  : {marks}")
print(f"Total  : {total}")
print(f"Average: {avg:.2f}")
print(f"Highest: {high} | Lowest: {low}")