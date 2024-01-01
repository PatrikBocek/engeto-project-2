"""
projekt_2_v3.py: druhy projekt do Engeto Online Python Akademie
author: Patrik Bocek
email: patrik.bocek@tria-tr.cz
discord: Patrik B fallencz#2217
"""


import random
import time

def generate_random_number():
    return ''.join(random.sample('123456789', 4))

def single_plural(count: int, singular: str, plural: str):
    if count == 1:
        return f"{count} {singular}"
    else:
        return f"{count} {plural}"

def check_input(user_input: str, previous_guesses: list):
    if len(user_input) != 4 or not user_input.isnumeric() or user_input[0] == "0" or len(set(user_input)) < 4:
        print("Please enter a valid four-digit number with unique digits and without leading 0!")
        return False
    elif user_input in previous_guesses:
        print("Please enter a new number. The number you wrote has already been guessed!")
        return False
    else:
        return True

def evaluate_guess(secret_number: str, user_guess: str):
    bulls, cows = 0, 0
    for i in range(4):
        if user_guess[i] == secret_number[i]:
            bulls += 1
        elif user_guess[i] in secret_number:
            cows += 1
    return bulls, cows

def print_results(bulls: int, cows: int):
    print(f'{single_plural(bulls, "bull", "bulls")} {single_plural(cows, "cow", "cows")}')
    print("-----------------------------")

def save_amount_of_guesses(number, minutes, seconds):
    filename = "results.txt"
    try:
        with open(filename, 'a') as file:
            file.write(f"Guesses: {number} Time: {minutes}:{seconds}\n")
    except IOError:
        print(f"Error: Unable to write to {filename}.")

def main():
    random_number = generate_random_number()
    status = True
    guesses_num = 0
    bulls, cows = 0, 0
    guesses = []
    start_time = time.time()

    print("Hi there!")
    print("""-----------------------------------------------
I've generated a random 4-digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------""")

    while status:
        user_guess = input("Enter a number: ")
        if check_input(user_guess, guesses):
            bulls, cows = evaluate_guess(random_number, user_guess)
            print_results(bulls, cows)
            guesses_num += 1

            if bulls == 4:
                end_time = time.time()
                status = False
                print("Congratulations! You've guessed the right number!")
                minutes, seconds = divmod(int(end_time - start_time), 60)
                save_amount_of_guesses(guesses_num, minutes, seconds)
                print(f'You guessed the answer in {guesses_num} {single_plural(guesses_num, "guess", "guesses")}, '
                      f'{minutes} {single_plural(minutes, "minute", "minutes")} and '
                      f'{seconds} {single_plural(seconds, "second", "seconds")}')

if __name__ == "__main__":
    main()
