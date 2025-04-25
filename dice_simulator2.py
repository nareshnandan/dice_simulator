import random

def roll_dice():
    dice_value = random.randint(1, 6)
    print(f"🎲 You rolled: {dice_value}")

# Run the dice roll
roll_dice()

# -----------------------------
# Simple Dice Model (Reference Only)
# Dice has 6 faces: 1, 2, 3, 4, 5, 6
# Used in games like Snakes and Ladders, Ludo, Monopoly, etc.
# Each time you roll, it gives a random number between 1 and 6
# -----------------------------
