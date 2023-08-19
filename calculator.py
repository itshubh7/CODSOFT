print('Select Operation') #operations which can be performed in this calculator
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. Recalculate')

re = 'y' #initializing re variable
while(re == 'y'):
    choice = int(input('Choose between 1/2/3/4: ')) # taking inputs for choosing operations
    if choice in (1, 2, 3, 4):
        #taking inputs of variables
        num1 = float(input('Enter 1st number:'))
        num2 = float(input('Enter 2nd number:'))
    else:
        print("Invalid Choice. Enter any valid chioice.")
        
    # Mathematical operations
    if choice == 1:
        print(num1, '+', num2, '=', num1 + num2)
    elif choice == 2:
        print(num1, '-', num2, '=', num1 - num2)
    elif choice == 3:
        print(num1, '*', num2, '=', num1 * num2)
    elif choice == 4:
        print(num1, '/', num2, '=', num1 / num2)
    # Want to calculate again?
    re = input('Want to recalculate? Press y, or press any other key to terminate: ')
    

