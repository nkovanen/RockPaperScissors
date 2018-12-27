from random import randint

#list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play for computer
computer = t[randint(0,2)]

#player False
player = False

while player == False:
    #set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
            print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("Bot picked Paper")
            print("You lose!", computer, "covers", player)
        else:
            print("Bot picked Scissors")
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("Bot picked Scissors")
            print("You lose!", computer, "cut", player)
        else:
            print("Bot picked Rock")
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("Bot picked Rock")
            print("You lose...", computer, "smashes", player)
        else:
            print("Bot picked Paper")
            print("You win!", player, "cut", computer)
    else:
            print("That's not a valid play. Check your spelling!")

player = False
computer = t[randint(0,2)]
