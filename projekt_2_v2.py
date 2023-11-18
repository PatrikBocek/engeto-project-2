"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Patrik Bocek
email: patrik.bocek@tria-tr.cz
discord: Patrik B fallencz#2217
"""


import random
import time

random_number = str(random.randint(1000, 9999))
#random_number = "1234"

status = True
guessesNum = 0
bulls = 0
cows = 0
guesses = []

print("Hi there!")
print("""-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------""")
start_time = time.time()
def singlePlural(count: int, ending: str):
    if count > 1 or count == 0:
        return ending
    else:
        return ""
def checkInput(userInput: str):
    if len(userInput) != 4:
        print("Please enter a four-digit number!")
        return False
    elif not userInput.isnumeric():
        print("Please enter a four-digit number!")
        return False
    elif userInput[0] == "0":
        print("Please enter a number that doesn't start with 0!")
        return False
    elif userInput in guesses:
        print("Please enter a new number. The number you wrote has already been written!")
        return False
    else:
        guesses.append(userInput)
        return True

    
def saveAmountOfGuesses(number, minutes, seconds):
    filename = "results.txt"
    try:
        with open(filename, 'a') as file:
            file.write("Guesses: "+str(number) +" Time: "+str(minutes) + ":"+ str(seconds) + "\n")
    except IOError:
        print(f"Error: Unable to write to {filename}.")
    
while status:
    guess = input("Enter a number:")
    if checkInput(guess):
        for i in range(4):
            if guess[i] == random_number[i]:
                bulls += 1
            else:
                for x in range(4):
                    if guess[i] == random_number[x]:
                        cows += 1
        print(f'{bulls} bull{singlePlural(bulls, "s")} {cows} cow{singlePlural(cows, "s")}')
        print("-----------------------------")
        guessesNum += 1
        if bulls == 4:
            end_time = time.time()
            status = False
            print("You've guessed the right number !!!")
            minutes, seconds = divmod(int(end_time - start_time), 60)
            saveAmountOfGuesses(guessesNum, minutes, seconds)
            print(f'You got the answer in {guessesNum} guess{singlePlural(guessesNum, "es")}, {minutes} minute{singlePlural(minutes, "s")} and {seconds} second{singlePlural(seconds, "s")}')
        cows = 0
        bulls = 0