from random import randint
from art import logo


def get_user_input_number():
    ''' Get an interger as input from user by verifying the input and asking the
    user to enter a number again incase of invalid input. '''
    number = input("Make a guess: ")
    while not number.isdigit():
        print(f"{number} is not a number. Please enter a valid number between 1 to 100.")
        number = input("Make a guess: ")
    return int(number)


def get_total_guess_attempts():
    ''' Asks the user to select easy or hard mode, if user selects hard mode
    it retund 5 attempts, else it returns 10. '''
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = 5 if choice == 'hard' else 10
    return attempts


def game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100!")

    choosen_num = randint(1, 100)
    attempts_remaining = get_total_guess_attempts()

    while attempts_remaining:
        number = get_user_input_number()
        attempts_remaining -= 1

        if number == choosen_num:
            print(f"\nYou got it! \\(ᵔᵕᵔ)/ The answer is {choosen_num}\n")
            break
        elif number > choosen_num:
            print("Too high.\nGuess again.")
        else:
            print("Too low.\nGuess again.")

        print(f"You have {attempts_remaining} attempts_remaining remaining to guess the number.")
        if attempts_remaining == 0:
            print("\nGame over (ᵟຶ︵ ᵟຶ)\n")


if __name__ == "__main__":
    game()
