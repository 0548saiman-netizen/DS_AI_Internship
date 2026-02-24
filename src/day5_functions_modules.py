<<<<<<< HEAD
#task 1
=======
# Task 1
>>>>>>> 81e6580 (Day7)

def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


length = float(input("Enter length: "))
width = float(input("Enter width: "))

X, Y = calc_rectangle(length, width)

print(f"Area: {X}, Perimeter: {Y}")

