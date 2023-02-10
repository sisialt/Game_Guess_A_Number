import random

computer_number = random.randint(1, 100)
guess_counter = 0

while True:
    player_number = input("Guess the number (1-100): ")
    guess_counter += 1

    if player_number[0] == "-":
        player_number_as_list = []

        for i in range(1, len(player_number)):
            player_number_as_list.append(player_number[i])

        player_number = "".join(player_number_as_list)

        if player_number.isdigit():
            print("Your number is out of range...")
            continue

    if not player_number.isdigit():
        print("Invalid input! Try again...")
        continue

    player_number = int(player_number)

    if player_number == 0 or player_number > 100:
        print("Your number is out of range...")
        continue

    if player_number < computer_number:
        print("Too low. Try with HIGHER number...")

    elif player_number > computer_number:
        print("Too high. Try with LOWER number...")

    else:
        print(f"Excellent!\nYou guessed the computers number on the {guess_counter}. attempt.")

        if guess_counter == 1:
            print("You are THE MASTER of this game!!!")
        elif guess_counter < 3:
            print("Your attempts to guess were less than 3, you are The Best at this game!")

        print("Let's play again! :)")
        break
