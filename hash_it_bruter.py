def hash_it(string):
    q = 0
    z = 127
    for i in [int(byte) for byte in bytearray(string, "utf-8")]:
        q += i
        z *= i
    return (((q << 3)+1)*z) % (2**32 - 1)

alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"

for letter in alphabet:
	for letter2 in alphabet:
		for letter3 in alphabet:
			for letter4 in alphabet:
				for letter5 in alphabet:
					for letter6 in alphabet:
						if hash_it(letter+letter2+letter3+letter4+letter5+letter6) == 293366475:
							print(letter+letter2+letter3+letter4+letter5+letter6)