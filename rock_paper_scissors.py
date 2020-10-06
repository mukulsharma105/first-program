import random
t = ["Rock", "Paper", "Scissors"]

computer = random.choice(t)
# print(computer)

player = True

while player:
    player = input("Rock, Paper, Scissors?\n\n")
    if player == computer:
        print("\nComputer: ",computer)
        print("\nTie!")
    elif player == "Rock" or 'rock' or 'r' or 'R':
        if computer == "Paper":
            print("\nComputer: ",computer)
            print("\nYou lose!", computer, "covers", player)
        else:
            print("\nComputer: ",computer)
            print("\nYou win!", player, "smashes", computer)
    elif player == "Paper"  or 'paper' or 'p' or 'P':
        if computer == "Scissors":
            print("\nComputer: ",computer)
            print("\nYou lose!", computer, "cut", player)
        else:
            print("\nComputer: ",computer)
            print("\nYou win!", player, "covers", computer)
    elif player == "Scissors"  or 'scissors' or 's' or 'S':
        if computer == "Rock":
            print("\nComputer: ",computer)
            print("\nYou lose...", computer, "smashes", player)
        else:
            print("\nComputer: ",computer)
            print("\nYou win!", player, "cut", computer)
else:
    print("That's not a valid play. Check your spelling!")