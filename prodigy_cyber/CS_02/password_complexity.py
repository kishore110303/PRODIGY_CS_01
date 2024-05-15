import time
def wait(seconds):
    print('Checking...')
    time.sleep(seconds)

# define "Exiting in n seconds" function
def exiting_in(exit_seconds):
    print('\nExiting in', exit_seconds, 'seconds...')
    time.sleep(exit_seconds)

# define function to search a list for matching letter
def find_in_list(letter, lst):
    return any(letter in word for word in lst)

# !!! START OF PROGRAM !!!
user_input = input('Enter a password you would like to check: ')

# verifier for null input
if bool(user_input) == False:
    print('\nERROR: You inputted nothing. Try again!')
    exiting_in(5)
    exit()

# initializing variables for verifier
max_pos = len(user_input)
current_pos = 0

wait(3)

# verifier for white spaces
for current_letter in user_input:

    # print(current_pos)

    if current_letter == ' ':
        print('\nERROR: No spaces allowed. Try again!')
        exiting_in(5)
        exit()
    elif current_pos == (max_pos-1):
        print('\nYour password is good for checking!')
        break
    current_pos = current_pos + 1

wait(3)

# verifier for 12 characters
if max_pos < 12:
    print('\nERROR: Your password needs to be >= 12 characters! Please try again!')
    exiting_in(5)
    exit()

# initializing variables for verifier
max_pos = len(user_input)
current_pos = 0

# initializing boolean variables for parameters; has_{upper, lower, number, special character}, ONLY ASCII
has_ascii = 1
has_upper = 0
has_lower = 0
has_number = 0
has_specialcharacter = 0

# list of special characters whitelisted for password
special_characters = "!@#$%^&*()-+?_=,<>/"
special_characters = list(special_characters)
# print(special_characters)

# verifier for having uppercase, lowercase, number: ONLY ASCII
for current_letter in user_input:
    
    # cuts the string into substrings for scanning with string methods
    ss_current_letter = user_input[current_pos:(current_pos+1)]

    # print(ss_current_letter)

    if ss_current_letter.isascii() is False:
        has_ascii = 0
        print('\nERROR: Your password must only include ASCII characters!')
        exiting_in(5)
        exit()
    if ss_current_letter.isupper() is True:
        has_upper = 1
        
    if ss_current_letter.islower() is True:
        has_lower = 1
        
    if ss_current_letter.isnumeric() is True:
        has_number = 1

    if find_in_list(ss_current_letter, special_characters) == True:
        has_specialcharacter = 1
    
    current_pos = current_pos + 1

# calculating password complexity     
complexity = has_upper + has_lower + has_number + has_specialcharacter + 1

# print-checkers for different parameters; has_{upper, lower, number, special character}, ONLY ASCII

if complexity < 5:
    print("\nHere's a list of issues for your password:")

if has_ascii == 0:
    print('>>> Your password contains non-ascii characters.')
if has_upper == 0:
    print('>>> Your password lacks an uppercase letter.')
if has_lower == 0:
    print('>>> Your password lacks a lowercase letter.')
if has_number == 0:
    print('>>> Your password lacks a number.')
if has_specialcharacter == 0:
    print('>>> Your password lacks a special character.')

print("\nNow calculating password complexity score...")

wait(3)

# lets the user see the result for 10 seconds & exits
print(f'\nYour password complexity score is {complexity}/5.')
exiting_in(10)