num1 = int(input("Enter a number: "))

divisors = []

for number in range(1,num1+1):
	if num1 % number == 0:
		divisors.append(number)

print(divisors)
