import sys
sys.path.append(r"Data\Day14")
import art
import game_data
import os

from random import choice,choices

first_choice, second_choice = choices(game_data.data, k=2)
score = 0
while True:
    print(art.logo)
    print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}.")
    print(art.vs)
    print(f"Against B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}.")
    print(first_choice["follower_count"],second_choice["follower_count"])
    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    if first_choice["follower_count"] > second_choice["follower_count"] and user_choice == "A":
        score +=1
        print(f"You are right. Current score: {score}.") 
        second_choice = choice(game_data.data)
        while first_choice == second_choice:
            second_choice = choice(game_data.data)

    elif first_choice["follower_count"] < second_choice["follower_count"] and user_choice == "B":
        score +=1
        print(f"You are right. Current score: {score}.") 
        first_choice = second_choice
        second_choice = choice(game_data.data)
        while first_choice == second_choice:
            second_choice = choice(game_data.data)
    else:
        break
os. system('cls')
print(art.logo)        
print(f"Sorry that's wrong. Final Score is {score}.")
    
