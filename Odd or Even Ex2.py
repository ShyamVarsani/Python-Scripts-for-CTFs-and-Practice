num = int(input('Enter a number: '))
check = int(input('Enter a second number: '))

rem = num % 2

m4 = num % 4

numcheck = num % check

if rem == 1:
    print('The first number you have entered is odd!')
elif m4 == 0:
    print('The first number you entered is a multiple of 4')
else:
    print('The first number you have entered is even!\nThe first number you entered is not a multiple of 4')


if numcheck > 0:
    print('The first number does NOT divide into the second evenly!')
else:
    print('The first number DOES divide into the second evenly!')


