def validatepassword(password):
    rules = {"length":len(password)>=8,
             "number":any(char.isdigit()
for char in password),
        "uppercase":any(char.isupper()
for char in password) }
    return rules
print(
    validatepassword("Kousic123"))