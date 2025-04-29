# This program simulates dice rolls and shows results

import random

def roll_dice():
    return random.randint(1, 6)

# Ask user how many times to roll
times = int(input("How many times do you want to roll the dice? "))

results = []  # Store all results

for i in range(times):
    result = roll_dice()
    results.append(result)
    print(f"Roll {i+1}: 🎲 You rolled a {result}")

# Final output
print("\nAll Rolls:", results)
print("Total:", sum(results))
print("Average:", round(sum(results)/len(results), 2))
