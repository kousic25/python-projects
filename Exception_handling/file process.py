try:
    file = open("students.txt", "r")
    data = file.read()
    number = int(data)
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("File contains invalid data")
else:
    print("Number from file:", number)
finally:
    print("Closing process")