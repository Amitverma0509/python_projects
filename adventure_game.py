def intro():
    print("You find yourself in a dense, mist-covered forest.")
    print("The path ahead splits into three diresctions:")
    print("1. Enter the dark cave to the left.")
    print("2. Take the narrow path straigth ahead.")
    print("3. Cross the crumbling bridge to the right.")


def choice1():
    print("You enter the dark cave. It's pitch black.")
    choice = input("Do you want to light the torch or move forward in the dark? (torch/forward): ")
    if choice == "torch":
        print("Yor light the torch and avoid traps. You find a powerful artifact! You Win!")
    elif choice == "forward":
        print("You stumble in the dark and fall into a pit. Game Over!.")
    else:
        print("Not a valid option, Game Over!")
        

def choice2():
    print("You take the narrow path. It's lined with poisonous plants.")
    choice = input("Do you want to sneak carefully or run quickly? (sneak/run):")
    if choice == "sneak":
        print("You sneak past the dangers and find an enchanted tree. It grants you a wish! You Won!")
    elif choice == "run":
        print("You get caught in the poisonous plants and died, Game Over!")
    else:
        print("Not a valid option, Game Over!")

def choice3():
    print("You cross the crumbling bridge. It's unstable.")
    choice = input("Do you move slowly or rush across? (slowly/rush): ")
    if choice == "slowly":
        print("You carefully make it across and encounter a ghostly figure.")
        choice = input("Do you fight the ghost or negotiate? (fight/negotiate): ")
        if choice == "negotiate":
            print("The ghost is appeased and gives you the treasure. You win!")
        elif choice == "fight":
            print("The ghost is angered and attacks you. Game over.")
        else:
            print("Not a valid option, Game Over!")
    
    elif choice == "rush":
        print("The bridge collapses and you fall into the chasm. Game over.")
    else:
        print("Not a valid option, Game Over!")


intro()
choice = input("Which path will you take? (1/2/3): ")

if choice == "1":
    choice1()

elif choice == "2":
    choice2()

elif choice == "3":
    choice3()

else:
    print("Invalid choice, Game Over.")