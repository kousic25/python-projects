# phone contact
contacts = [
    {"name": "Alice",   "phone": "9876543210"},
    {"name": "Bob",     "phone": "9123456789"},
    {"name": "Charlie", "phone": "9988776655"},
    {"name": "Dave",    "phone": "9345678901"},
]
print("Contacts")
print("-" * 30)
for c in contacts:
    print(f"{c['name']:<12} {c['phone']}")
search = "Bob"
found  = next((c for c in contacts if c["name"] == search), None)
print(f"\nSearch '{search}': {found['phone'] if found else 'Not found'}")