
import random

def play():
    print("Welcome to Rock-Paper-Scissors Game 🎮")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
    print("------------------------------------------------------")

    options = ["rock", "paper", "scissors"]

    while True:
        user = input("Enter your choice (rock, paper, scissors or quit): ").lower()

        if user == "quit":
            print("Thanks for playing! 👋")
            break

        if user not in options:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer = random.choice(options)
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a tie! 🤝")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("You win! 🎉")
        else:
            print("Computer wins! 😢")
        print("------------------------------------------------------")

if __name__ == "__main__":
    play()