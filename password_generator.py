import random
import string

complexity = int(input('Choose the complexity of the password (1/2/3): ')) # Taking the complexity as an input
length = int(input("Enter the length of the password: ")) # Taking the length of the password

if complexity == 1:
    pswrd = string.ascii_letters
if complexity == 2:
    pswrd = string.ascii_letters + string.digits
if complexity == 3:
    pswrd = string.ascii_letters + string.punctuation + string.digits
    
password = ''

for i in range(length):
    password += ''.join(random.choice(pswrd)) 
    
print(f'Password is : {password}')
