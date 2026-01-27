class Person:
    def speak(self):
        print("I am a person")

class Student(Person):   # Student inherits Person
    def study(self):
        print("I am studying")

s = Student()
s.speak()   # from parent
s.study()   # from child
