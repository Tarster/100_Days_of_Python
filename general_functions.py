def return_int(input_message) -> int:
    '''
    @input_message : We will provide a input message that we want to display to the user 
    return: @int The integer value that we want.
    '''
    number = ''
    is_positive_integer, is_negative_integer =  False, False
    while not (is_positive_integer or is_negative_integer):
        number = input(input_message)
        is_positive_integer = number.isdigit()
        is_negative_integer =  number.startswith("-") and number[1:].isdigit()
    return int(number)
