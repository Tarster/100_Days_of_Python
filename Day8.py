logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
def custom_is_numeric(number_string):
    '''Custom implementation to check if a string contains number'''
    is_positive_integer = number_string.isdigit()
    is_negative_integer =  number_string.startswith("-") and number_string[1:].isdigit()
    return is_positive_integer or is_negative_integer
    

def negative_shift(shift_number,user_message):
    ''' If user wants to shift in the backward direction '''
    encoded_message = []
    shift_number *= -1
    shift_number = shift_number % 26
    shift_number *= -1
    for letter in user_message:
        if letter.isalpha():
            numeric_value = ord(letter) + shift_number 
            if (64 < numeric_value <91 ) and letter.isupper():
                encoded_message.append(chr(numeric_value))
            elif letter.islower() and (96 < numeric_value < 123):
                encoded_message.append(chr(numeric_value))
            else:
                encoded_message.append(chr(numeric_value + 26 ))
        else:
            encoded_message.append(letter)
    return ''.join(encoded_message)

def positive_shift(shift_number,user_message):
    ''' If user wants to shift in the forward direction '''
    encoded_message = []
    shift_number = shift_number % 26
    for letter in user_message:
        if letter.isalpha():
            numeric_value = shift_number + ord(letter)
            if letter.islower() and (95 < numeric_value < 123):
                encoded_message.append(chr(numeric_value))
            elif (64 < numeric_value < 91 ) and letter.isupper():
                encoded_message.append(chr(numeric_value))
            else:
                encoded_message.append(chr(numeric_value - 26 ))
        else:
            encoded_message.append(letter)
    return ''.join(encoded_message)

def encode():
    '''
    This Function is used to encode the strings.
    '''
    user_message = input("Type your message: ")
    shift_number = ' '
    while not custom_is_numeric(shift_number):
        shift_number = input("Type the shift number: ")

    shift_number = int(shift_number)

    if shift_number == 0:
        print(f'Here is the encoded result: {user_message}')
        return
    
    if shift_number < 0:
        encoded_string = negative_shift(shift_number,user_message) 
        
    else:
        encoded_string = positive_shift(shift_number,user_message) 
    print(f'Here is the encoded result: {encoded_string}')
    


def decode():
        '''This Function is used to encode the strings.'''
        user_message = input("Type your message: ")
        shift_number = ' '
        while not custom_is_numeric(shift_number):
            shift_number = input("Type the shift number: ")

        shift_number = int(shift_number) * (-1)

        if shift_number == 0:
            print(f'Here is the encoded result: {user_message}')
            return
        
        if shift_number < 0:
            decoded_string = negative_shift(shift_number,user_message) 
            
        else:
            decoded_string = positive_shift(shift_number,user_message) 
        print(f'Here is the decoded result: {decoded_string}')

print(logo)
user_continue = True
while user_continue:
    while True:
        encoding_decoding = input("Type 'encode' to encrypt and 'decode' to decrypt: ")
        if encoding_decoding.lower() == 'encode':
            encode() 
            break
        elif encoding_decoding.lower() == 'decode':
            decode()
            break
        else: 
            print("Please provide a valid input.")
    user_continue = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    if user_continue.lower() == 'yes':
        user_continue = True
    else:
        user_continue = False

# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# abcdefghijklmnopqrstuvwxyz