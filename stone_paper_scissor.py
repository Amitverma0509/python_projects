import random

user_wins = 0
computer_wins = 0

options = ["stone","paper","scissor"]

while True:
    user_pick = input("Enter stone/paper/scissor or q to exit: ").lower()
    if user_pick == "q":
        break
    if user_pick not in options:
        print("please enter stone/paper/scissor only")
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    

    if user_pick == "stone" and computer_pick == "scissor":
        print("You Won!")
        user_wins +=1
    elif user_pick == "paper" and computer_pick == "stone":
        print("You Won!")
        user_wins +=1
    elif user_pick == "scissor" and computer_pick == "paper":
        print("You Won!")
        user_wins +=1
    else:
        print("You Lose!")
        computer_wins +=1

print("You Won",user_wins,"times")
print("Computer Won",computer_wins,"times")