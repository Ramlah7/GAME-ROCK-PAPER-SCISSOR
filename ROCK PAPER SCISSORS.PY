import random
choices = ["rock", "paper", "scissors"]
print("Welcome to Rock-Paper-Scissors game!")
print("Enter 0 to end the game")
while True:
    user = input("\nYour choice (rock, paper, scissors): ").lower()
    if user == '0':
        print("Thanks for playing!")
        break
    if user not in choices:
        print("Invalid choice. Please try again.")
        continue
    computer = random.choice(choices)
    print(f"Computer's choice: {computer}")
    if computer == user:
        print("It's a draw!\n")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You won!\n")
    else:
        print("You lose!\n")
