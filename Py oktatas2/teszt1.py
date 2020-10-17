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

class Teszt:
    __a=3 # félig privát

    def __init__(self) -> None:
        self.a=1
        self._a=2 # privát szándék
        
    def javit(self):
        self.__a +=10

t=Teszt()
print(t.a)
print(t._a)
print(t._Teszt__a)
t.javit()
print(t.a)
print(t._a)
print(t._Teszt__a)

import sys
sys.path.append("..")
import modul
aa=modul.teszt2()
