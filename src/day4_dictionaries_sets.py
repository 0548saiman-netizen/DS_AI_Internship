# task 1
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
   
# task 2 
# Step 1: Create a list with duplicate user IDs
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

# Step 2: Convert list to a set to remove duplicates
unique_users = set(raw_logs)

# Step 3: Membership test
print("Is ID05 in unique_users?", "ID05" in unique_users)

# Step 4: Count comparison
print("Original list length:", len(raw_logs))
print("Unique set length:", len(unique_users))

# Step 5: Output the unique set
print("Unique users:", unique_users)

# task 3
# Create two sets
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

# Common interests (Intersection)
shared_interests = friend_a & friend_b

# All interests (Union)
all_interests = friend_a | friend_b

# Interests friend_a has but friend_b does not (Difference)
unique_to_a = friend_a - friend_b

# Print results
print("Shared Interests:", shared_interests)
print("All Interests:", all_interests)
print("Unique Interests of Friend A:", unique_to_a)
