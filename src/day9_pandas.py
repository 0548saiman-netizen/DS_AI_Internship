# Task 1

import pandas as pd

products = pd.Series(
    data=[700, 150, 300],
    index=['Laptop', 'Mouse', 'Keyboard'],
    name='Product Prices'
)

laptop_price = products.loc['Laptop']

first_two = products.iloc[:2]

print("Full Series:\n")
print(products)

print("\nPrice of Laptop:")
print(laptop_price)

print("\nFirst Two Products (Positional Indexing):")
print(first_two)

# Task 2

import pandas as pd
grades = pd.Series([85, None, 92, 45, None, 78, 55])

missing = grades.isnull()

filled_grades = grades.fillna(0)

filtered_grades = filled_grades[filled_grades > 60]
print("Original Series:")
print(grades)

print("\nMissing Values (True indicates missing):")
print(missing)

print("\nFilled Series:")
print(filled_grades)

print("\nFiltered Scores (greater than 60):")
print(filtered_grades)

# Task 3

import pandas as pd

usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

cleaned_usernames = usernames.str.strip().str.lower()

contains_a = cleaned_usernames.str.contains('a')

print("Cleaned Usernames:")
print(cleaned_usernames)

print("\nContains letter 'a':")
print(contains_a)

