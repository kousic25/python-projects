import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
students = np.array(["Hari","Kousic","John","David","Priya"])
marks = np.array([85, 92, 76, 88, 95])
df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})
print("Student Details")
print(df)
print("\nAverage Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
plt.bar(df["Student"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()