import random  # Importing the random module to generate random numbers

def roll_dice():
    # Function to simulate rolling a dice (returns a number between 1 and 6)
    return random.randint(1, 6)

print("🎲 Welcome to Dice Simulator 🎲")

# Infinite loop to keep rolling the dice until the user decides to quit
while True:
    user_input = input("Press Enter to roll the dice or type 'q' to quit: ")
    
    if user_input.lower() == 'q':
        # If user types 'q', exit the loop and end the program
        print("Thanks for playing! 👋")
        break
    
    # Roll the dice and display the result
    dice_value = roll_dice()
    print(f"🎲 You rolled: {dice_value}\n")
