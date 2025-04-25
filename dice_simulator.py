import random

def roll_dice():
    return random.randint(1, 6)

print("🎲 Welcome to Dice Simulator 🎲")
while True:
    user_input = input("Press Enter to roll the dice or type 'q' to quit: ")
    if user_input.lower() == 'q':
        print("Thanks for playing! 👋")
        break
    dice_value = roll_dice()
    print(f"🎲 You rolled: {dice_value}\n")


#simple 