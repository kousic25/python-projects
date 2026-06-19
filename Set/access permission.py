adminpermissions = {"read","write","delete","upload"}
userpermissions = { "read","upload"}
if userpermissions.issubset(adminpermissions):
    print("Access granted")
else:
    print("Access denied")