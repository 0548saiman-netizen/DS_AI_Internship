# Create a dictionary with at least 3 contacts
contacts = {
    "Aman": "9876543210",
    "Riya": "9123456780",
    "Sohan": "9988776655"
}

# Add / Update a contact
contacts["Riya"] = "9000011111"   # updating existing contact
contacts["Neha"] = "8899001122"   # adding new contact

# Safe access using get()
print("Lookup Results:")
print("Aman:", contacts.get("Aman", "Contact not found"))
print("Rahul:", contacts.get("Rahul", "Contact not found"))

print("\nContact List:")
# Iteration using for loop
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")