import random

ascii_image = ['''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
]

def show_image(my_input):
    '''
    This function will show the corresponding image.
    '''
    if my_input == 0:
        print(ascii_image[0])
    elif my_input == 1:
        print(ascii_image[1])
    elif my_input == 2:
        print(ascii_image[2])
    else:
        print("You entered a wrong input. Program will exit")
        # exit()

user_input = int(input('What do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors.'))
show_image(user_input)
computer_choice = random.randint(0, 2)
show_image(computer_choice)

if user_input == computer_choice:
    print("This is a draw.")
elif (computer_choice == 0 & user_input == 1) or (computer_choice == 2 & user_input == 0) or (computer_choice == 1  & user_input == 2):
    print("You won")
else:
    print('You lose')