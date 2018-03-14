import random


a = random.sample(range(1,100),random.randint(1,100))
b = random.sample(range(1,100),random.randint(1,100))
c  = []

for i in a:
    if i in b:
        c.append(i)

print("List A is: ",a)
print("List B is: ",b)
print(set(c))


