import random

# Function to play one round
def play_game():
    choices = ["stone", "paper", "scissors"]

    user = input("Enter stone, paper, or scissors: ").lower().strip()

    if user not in choices:
        print("Invalid choice!")
        return

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("Match Draw!")

    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")

    else:
        print("Computer Wins!")


# Menu function
def menu():
    while True:
        print("\n--- Stone Paper Scissors Game ---")
        print("1. Play Game")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            play_game()

        elif choice == "2":
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice!")


# Run program
menu()