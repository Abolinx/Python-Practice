import random

def guess_game():
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("___Wellcome to guess game___")
    print("Guess a number between 1 and 100")
    
    while True:

        try:
            user_guess = int(input("Your guess:"))
            attempts += 1
        except ValueError:
            print("Invalid input; Please enter an integer number")
            continue
        
        if user_guess < secret_number:
            print("The secret number is larger. Try again.⬆️")
        elif user_guess > secret_number:
            print("The secret number is smaller. Try again.⬇️")
        else:
            print(f"Congratulations🎉\nYou guessed the number {secret_number} in {attempts} tries.")
            break
if __name__ == "__main__":
    guess_game()