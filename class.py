# 類別 class
import math
print(math.pi)

class Myclass:
    i=1234


print("Myclass: ",Myclass.i)
# Myclass:  1234

class Complex:
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart
    def __del__(self):
        print('delet object')

x=Complex(3.0, -4.5)
print("x: ", x)
# x:  <__main__.Complex object at 0x1055bae48>
print("Complex: ",x.r, x.i)
# Complex:  3.0 -4.5
# delet object


class Myclass2:
    i=1234
    def f(self):
        return 'hello world'
x= Myclass2()
print("Myclass2")
# Myclass2
print(x.i)
# 1234
print(x.f())
# hello world

class Dog:
    kind= 'small dog'
    def __init__(self,name):
        self.name= name

d = Dog('small cat')
e = Dog('very small dog')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)
'''
small dog
small dog
small cat
very small dog
'''
