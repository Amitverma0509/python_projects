import random

num_range = input("Enter a number: ")

if num_range.lstrip('-').isdigit():
	num_range = int(num_range)
	
	if num_range < 0:
		print("Enter a number greater than zero next time!")
		quit()
else:
	print("Enter a number next time")
	quit()

random_num = random.randint(0,num_range)
guesses = 0

while True:
	guesses += 1
	user_guess = input("Make a guess: ")
	
	if user_guess.isdigit():
		user_guess = int(user_guess)
	
	else:
		print("pls type a number next time!")
		guesses -=1
		continue
	
	if user_guess == random_num:
		print("You got it!")
		break	
	elif user_guess > random_num:
		print("You are above it")
	else:
		print("You are below it")

print("You got it in", guesses, "guess")