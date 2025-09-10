class Animal:
    def sound(self):
        print("Animal Making Sound")
        
class Dog(Animal):
    def sound(self): # overriding
        print("Dog Making Sound")

class Cat(Animal):
    def sound(self): # overriding
        print("Cat Making Sound")

a = Animal()
a.sound()

d = Dog()
d.sound()

c = Cat()
c.sound()