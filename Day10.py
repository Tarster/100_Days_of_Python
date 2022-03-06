import general_functions as gf

logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

option = 'yes'
first_number = gf.return_int("Please  enter the first number: ")
while option.lower() != 'exit':
    operator = input("+\n-\n*\n/\nPlease enter the operator: ")
    while True:
        if operator in ['+', '-', '*', '/']:
            break
        else:
            operator = input("Enter the correct operator from the list: ")

    second_number = gf.return_int("Please  enter the second number: ")

    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    else:
        if second_number == 0:
            print("Error, Well you can't divide a number by 0.")
            result = 0 
        else:    
            result = first_number / second_number
    option = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start the new calculation. You can write 'exit' to exit the program: ")
    if option == 'y':
        first_number = result
    elif option != 'exit':
        first_number = gf.return_int("Please  enter the first number: ")