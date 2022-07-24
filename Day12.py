import random,sys
random_number = random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty=="hard": 
    difficulty = 5 
else:
    difficulty = 10 

while difficulty != 0:
    print(f"You have a {difficulty} attempts remaining to guess the number.")
    guess_number = int(input("Make a guess: "))
    if random_number < guess_number:
        print("Too high.")
        print("Guess again.")
        difficulty -= 1
    elif random_number == guess_number:
        print(f"You won the game. I guessed the number {guess_number}.")
        sys.exit(0)
    else:
        print("Too Low.")
        print("Guess again.")
        difficulty -= 1

print(f"You lost! I guessed the number {guess_number}")


