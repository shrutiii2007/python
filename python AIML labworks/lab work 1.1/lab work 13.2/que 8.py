import random

options = ["rock", "paper", "scissors"]

user = input("Enter rock, paper or scissors: ").lower()
computer = random.choice(options)

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("Computer wins!")


# output:-

# 1st time run :-
# Enter rock, paper or scissors: rock
# Computer chose: scissors
# You win!

# 2nd time run :-
# Enter rock, paper or scissors: rock
# Computer chose: rock
# It's a tie!