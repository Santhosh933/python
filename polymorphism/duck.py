class Duck:
    def quack(self):
        print("Duck Sounding")
        
class Person:
    def quack(self):
        print("I can also quack like Duck")

def make_quack(obj):
    obj.quack()

make_quack(Duck())
make_quack(Person())