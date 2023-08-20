import random
import string

def pw(length, pswrd): # Will create the password
    password = ''

    for i in range(length):
        password += ''.join(random.choice(pswrd)) 
    
    print(f'Password is : {password}')

length = int(input("Enter the length of the password: ")) # Taking the length of the password
complexity = int(input('Choose the complexity of the password (1/2/3): ')) # Taking the complexity as an input

if complexity == 1:
    pswrd = string.ascii_letters # Only use letters as a password
    pw(length, pswrd)
elif complexity == 2:
    pswrd = string.ascii_letters + string.digits # Use letters and digits to build the password
    pw(length, pswrd)
elif complexity == 3:
    pswrd = string.ascii_letters + string.punctuation + string.digits # Combines letters, digits and special characters
    pw(length, pswrd)
else:
    print('Wrong Choice!') # For wrong choices only
