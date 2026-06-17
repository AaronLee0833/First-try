import random

print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================")

print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")

player_choice = 0

player_choice = int(input("Pick a number: "))

computer_choice = random.choice(["✊", "✋", "✌️", "🦎", "🖖"])
print(f"CPU chose: {computer_choice}")

if player_choice == 1:
    if computer_choice == "✊":
        print("It's a tie!")
    elif computer_choice == "✋":
        print("You lose!")
    elif computer_choice == "✌️":
        print("You win!")
    elif computer_choice == "🦎":
        print("You win!")
    else:
        print("You lose!")
elif player_choice == 2:
    if computer_choice == "✊":
        print("You win!")
    elif computer_choice == "✋":
        print("It's a tie!")
    elif computer_choice == "✌️":
        print("You lose!")
    elif computer_choice == "🦎":
        print("You lose!")
    else:
        print("You win!")
elif player_choice == 3:
    if computer_choice == "✊":
        print("You lose!")
    elif computer_choice == "✋":
        print("You win!")
    elif computer_choice == "✌️":
        print("It's a tie!")
    elif computer_choice == "🦎":
        print("You win!")
    else:
        print("You lose!")
elif player_choice == 4:
    if computer_choice == "✊":
        print("You lose!")
    elif computer_choice == "✋":
        print("You win!")
    elif computer_choice == "✌️":
        print("You lose!")
    elif computer_choice == "🦎":
        print("It's a tie!")
    else:
        print("You win!")
elif player_choice == 5:
    if computer_choice == "✊":
        print("You win!")
    elif computer_choice == "✋":
        print("You lose!")
    elif computer_choice == "✌️":
        print("You win!")
    elif computer_choice == "🦎":
        print("You lose!")
    else:
        print("It's a tie!")
else:
    print("Error: Invalid choice. Please choose a number between 1 and 5.")