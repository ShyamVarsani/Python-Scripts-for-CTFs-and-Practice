import re

encrypted = "4e;36k>m"
decrypted = []

for i in encrypted:
	decrypted += i

for x in range(8):
	decrypted[x] = chr(ord(decrypted[x]) - x)

print(''.join(decrypted))
