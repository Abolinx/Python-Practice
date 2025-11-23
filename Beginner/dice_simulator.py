import random

def roll_dice():
    dice_rool = random.randint(1, 6)
    print(f"your number is {dice_rool}")

def main():
    should_roll = True
    print("Welcome to Dice simulator👋")

    while should_roll:
        roll_dice()
        user_input = input("Roll dice again?(y/n):").lower()
        if user_input == "no":
            should_roll = False
            print("Bay Bay👋")
        elif user_input == "yes":
            pass
        else:
            print("The input is invalid. It is assumed that you do not wish to continue.❌")
            should_roll = False

if __name__ == "__main__":
    main()