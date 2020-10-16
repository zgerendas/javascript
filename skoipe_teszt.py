'''
spam="ALma"
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    spam = "test spam"
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    spam = "test spam"
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
'''

class Osztalyom:
    "Egy egyszerű példa osztály"
    i = 12345
    def f(self):
        return 'hello világ'
    def __init__(self):
        pass

x = Osztalyom()

print(Osztalyom.f)

x.szamlalo = 1
while x.szamlalo < 10:
    x.szamlalo = x.szamlalo * 2
    print(x.szamlalo)
del x.szamlalo