class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Bark")

class Cat(Animal):
    def meow(self):
        print("Meow")

d = Dog()
c = Cat()

d.sound()
c.sound()
