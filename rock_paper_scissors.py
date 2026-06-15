import random

print("===================")
print("Rock Paper Scissors")
print("===================")

print("1) Rock")
print("2) Paper")
print("3) Scissors")

player_choice = 0

player_choice = int(input("Pick a number: "))

computer_choice = random.choice(["Rock", "Paper", "Scissors"])
print(f"CPU chose: {computer_choice}") 

if player_choice == 1:
    if computer_choice == "Rock":
        print("It's a tie!")
    elif computer_choice == "Paper":
        print("You lose!")
    else:
        print("You win!")
elif player_choice == 2:
    if computer_choice == "Rock":
        print("You win!")
    elif computer_choice == "Paper":
        print("It's a tie!")
    else:
        print("You lose!")
elif player_choice == 3:
    if computer_choice == "Rock":
        print("You lose!")
    elif computer_choice == "Paper":
        print("You win!")
    else:
        print("It's a tie!")
else:
    print("Error: Invalid choice. Please choose a number between 1 and 3.")