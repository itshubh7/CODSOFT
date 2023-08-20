import random
import string

complexity = int(input('Choose the complexity of the password (1/2/3): ')) # Taking the complexity as an input
length = int(input("Enter the length of the password: ")) # Taking the length of the password

if complexity == 1:
    pswrd = string.ascii_letters # Only use letters as a password
if complexity == 2:
    pswrd = string.ascii_letters + string.digits # Use letters and digits to build the password
if complexity == 3:
    pswrd = string.ascii_letters + string.punctuation + string.digits # Combines letters, digits and special characters
    
password = ''

for i in range(length):
    password += ''.join(random.choice(pswrd)) 
    
print(f'Password is : {password}')
