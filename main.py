import random, sys
correct = random.randint(1, 20)
print("I am thinking of a number between 1 and 20. You have 5 tries.")
for i in range(1,6):
    guess = int(input("Take a guess. "))
    if guess == correct:
        print("Good job! <3.", guess, "is correct.")
        sys.exit()
    elif guess > correct:
        print("Too high! Try again")
        continue
    elif guess < correct:
        print("Too low! Try again")
        continue
print("You failed! Better luck next time!")
