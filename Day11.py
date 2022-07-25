import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def custom_rand():
    """
    A function to generate random number tailored for blackjack. 
    """
    number = random.randint(1, 13)
    if number > 10:
        number = 10
    return number

option = 'y'
while option.lower() != 'n':
    print(logo)
    player_cards = []
    computer_cards = []
    for _ in range(0,2):
        player_cards.append(custom_rand())
        computer_cards.append(custom_rand())

    print(f'Your cards: {player_cards}')
    print(f"Computer's first card: {computer_cards[0]}")
    # print(sum(player_cards))
    while sum(player_cards) < 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        
        if another_card == 'y':
            another_card = custom_rand()
            player_cards.append(another_card)
            print(f'Your cards: {player_cards}')
                   
            if sum(player_cards) > 21:
                print("Game over. You lose.")
                print(f"Computer's final hand: {computer_cards}")
                break
 
        else:
            if sum(player_cards) > sum(computer_cards):
                print(f"Computer's final hand: {computer_cards}")
                print("You win!!!!")
            elif sum(player_cards) == sum(computer_cards):
                print(f"Computer's final hand: {computer_cards}")
                print("It's a draw.")
            else:
                print("Game over. You lose.")
                print(f"Computer's final hand: {computer_cards}")
            break
    
    option = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
