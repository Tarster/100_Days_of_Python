import os

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def custom_is_numeric(number_string):
    '''Custom implementation to check if a string contains number'''
    is_positive_integer = number_string.isdigit()
    is_negative_integer =  number_string.startswith("-") and number_string[1:].isdigit()
    return is_positive_integer or is_negative_integer

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
print(logo)
print("Welcome to the secret auction program. Not so secret!!!")

another_entry = 'yes'
bidder_details = {}
count = 0 
while another_entry.lower() != 'no': 
    amount = ''
    name = input('What is your name?: ')
    while not custom_is_numeric(amount):
        amount = input("What's your bid?: $")

    bidder_details[str(count)] = {'name': name, 'amount':amount}

    another_entry = input("Are there any other bidders? Type 'yes' or 'no'.: ")
    count += 1
    clearConsole()
    
names = []
index = 0
amount = 0
for value in sorted(bidder_details.items(), key=lambda k_v: k_v[1]['amount'], reverse= True):
    # print(value)
    if index == 0:
        previous_bet = value
        names.append(previous_bet[1]['name'])
        amount = previous_bet[1]['amount']
        
    else:
        current_bet = value
        if previous_bet[1]['amount'] == current_bet[1]['amount']:
            names.append(current_bet[1]['name'])
            amount = value[1]['amount']
        else:
            break
    index += 1
print(f"The winner of the bid is {', '.join(names)} and bidding amount is: ${amount}")
