# Task 1

name = input("Enter your name: ")
goal = input("Enter your daily goal: ")

with open("journal.txt", "a") as file:
    file.write(f"Name: {name}, Goal: {goal}\n")

print("Your goal has been saved!")

# Task 2

import csv

with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        if row['Status'] == 'Pass':
            print(row['Name'])
                        
# Task 3

filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\nFile Content:\n")
        print(content)

except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")
    
    
    
