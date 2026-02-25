# Task 1

import matplotlib.pyplot as plt
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]
plt.scatter(study_hours, scores, color='green', s=100, edgecolor='black')
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Hours Spent Studying")
plt.ylabel("Exam Score")
plt.show()

# Task 2

import matplotlib.pyplot as plt

categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

months = [1, 2, 3, 4, 5]
revenue = [2000, 2500, 3000, 3500, 4000]

plt.figure(figsize=(12, 5))  

plt.subplot(1, 2, 1)
plt.bar(categories, sales, color='skyblue')
plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Sales Units")

plt.subplot(1, 2, 2)
plt.plot(months, revenue, marker='o', linestyle='-', color='green')
plt.title("Revenue Trend Over Months")
plt.xlabel("Month")
plt.ylabel("Revenue in USD")

plt.tight_layout()
plt.show()
