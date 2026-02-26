# Task 1

import random
trials = 1000
count_sum_7 = 0

for _ in range(trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    if dice1 + dice2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials

print("Experimental Probability (Sum = 7):", experimental_probability)
print("Theoretical Probability:", 1/6)

# Task 2

import random

P_heads = 1/2
P_six = 1/6
P_independent = P_heads * P_six

print("=== Independent Events ===")
print("Theoretical P(Heads AND 6):", P_independent)

trials = 100000
count = 0

for _ in range(trials):
    coin = random.choice(["Heads", "Tails"])
    die = random.randint(1, 6)
    
    if coin == "Heads" and die == 6:
        count += 1

experimental_independent = count / trials
print("Experimental Probability:", experimental_independent)
print("\n=== Dependent Events ===")

P_first_red = 5/10
P_second_red_given_first = 4/9
P_dependent = P_first_red * P_second_red_given_first

print("Theoretical P(Both Red):", P_dependent)
trials = 100000
count = 0

for _ in range(trials):
    bag = ["Red"]*5 + ["Blue"]*5
    
    first = random.choice(bag)
    bag.remove(first)  # without replacement
    
    second = random.choice(bag)
    
    if first == "Red" and second == "Red":
        count += 1

experimental_dependent = count / trials
print("Experimental Probability:", experimental_dependent)

# Task 3

P_spam = 0.1
P_ham = 0.9
P_free_given_spam = 0.9
P_free_given_ham = 0.05

P_free = P_free_given_spam * P_spam + P_free_given_ham * P_ham

P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("Probability the email is Spam given 'Free':", round(P_spam_given_free, 4))


