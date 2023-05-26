import random

computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number (1-100): ")
    if not player_input.isdigit():
        print("Invalid input. Try again...")
    if int(player_input) == computer_number:
        print("Congratulations! You guessed it!")
        break
    elif int(player_input) < computer_number:
        print("Too low!")
    elif int(player_input) > computer_number:
        print("Too high!")