

print('Welcome To Password Generator')

import random  # import random module to use random character in program
import string  # to use string functions and to save time

# function 
def password_generator(length):
    # string built-in functions that will save time
    password_characters = string.ascii_letters + string.punctuation + string.digits 
    
    # (for loop) for taking random char from password_characters according to length of password
    # random.choice function is for random choice of char from password_charcters
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

# driver code
length_of_password = int(input(" Enter Length Of Password You Want : ")) # takin input of length of password from user

password_generator=password_generator(length_of_password)   # function call
print('Password is :',password_generator)  # final password printing



