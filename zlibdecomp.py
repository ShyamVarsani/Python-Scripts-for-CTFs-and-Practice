import sys, zlib

i = 0
str_object1 = open('z0', 'rb').read()

while i < 50:
   str_object2 = zlib.decompress(str_object1)
   f = open('z'+str(i+1), 'wb')
   f.write(str_object2)
   f.close()

   str_object1 = open('z'+str(i+1), 'rb').read()
   i += 1