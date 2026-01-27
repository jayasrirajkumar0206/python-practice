class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):          # overriding
        print("Bark")

d = Dog()
d.sound()
