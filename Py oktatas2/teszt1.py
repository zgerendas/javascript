import struct
dir()

lista =["a","b","c"]
a=enumerate(lista)
print(a)
for i,n in a:
    print(str(i)+" "+n)

print(max([10,1,1],[10,3,100],[10,20]))

f = open("teszt1.py")

print(f.readlines())
f.close()

print("----------")
import os
print(os.linesep)