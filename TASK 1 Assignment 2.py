#This will take the input from the user
number = int(input('Enter a Number: '))

#This will check whether the number is odd or even
remainder = number % 2

#This will judge the result of odd and even and then print the statement accordingly
if remainder == 1:
    print(f'{number} is an odd number.')
else:
    print(f'{number} is an even number.')
