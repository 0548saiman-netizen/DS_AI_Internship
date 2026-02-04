#task 1

inventory = ["Apples", "Bananas", "Carrots", "Dates"]
print("Current inventory:", inventory)
inventory.append("Eggs")
inventory.remove("Bananas")
inventory.sort()
print("Final updated inventory:", inventory)

#task2
 
temperature = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print("First reading:", temperature[0])
print("Last reading:", temperature[-1])
afternoon_peak = temperature[3:6]
print("Afternoon Peak readings:", afternoon_peak)
last_3_hours = temperature[-3:]
print("Last 3 hours readings:", last_3_hours)

#task3

screen_res = (1920, 1080)
print("Current Resolution:", screen_res[0], "x", screen_res[1])
screen_res[0] = 1280
print( "Tuples cannot be modified!")