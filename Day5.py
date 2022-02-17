import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_length = nr_letters + nr_symbols + nr_numbers

def random_password_easy(total_length, nr_letters,nr_symbols,nr_numbers):
    '''
    Easy Level - Order not random:
    e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    '''
    password = ''
    for i in range(total_length):
        if i < nr_letters:
            # print(letters[random.randint(0, (len(letters)-1))])
            password += letters[random.randint(0, (len(letters)-1))]
        elif (i >= nr_letters) & (i < (total_length - nr_numbers)):
            # print(letters[random.randint(0, (len(letters)-1))])
            password +=symbols[random.randint(0, (len(symbols)-1))]
        else:
            # print(letters[random.randint(0, (len(letters)-1))])
            password += numbers[random.randint(0, (len(numbers)-1))]
    return password

def random_password_hard(password):
    '''
    Hard Level - Order of characters random:
    e.g. 4 letter, 2 symbol, 2 number = g^2jk8&
    '''
    hard_password = ''
    password_copy =[ x for x in password]
    for i in range(len(password)-1):
        final_index = len(password_copy) - 1
        rand_index = random.randint(0, final_index)
        hard_password += password_copy[rand_index]
        password_copy.pop(rand_index)
    return hard_password+password_copy[-1]

easy_password = random_password_easy(total_length, nr_letters, nr_symbols, nr_numbers)
print(f'Easy generated password:{easy_password}')
print(f'Hard generated password:{random_password_hard(easy_password)}')