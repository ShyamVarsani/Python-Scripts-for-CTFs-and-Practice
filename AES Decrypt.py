from Crypto.Cipher import AES
import base64

cipher_text= base64.b64decode('Q69htRlf08tHHf1cJYcqIwteyQK8BdSDg9UihLpVOypNMEbpaG+kGrTKkch6y1Ab')

# Decryption
decryption_suite = AES.new((base64.b64decode('MWo1Z9kJZ60a4skUlfcENA==')), 1)
plain_text = decryption_suite.decrypt(cipher_text)

print(plain_text)
