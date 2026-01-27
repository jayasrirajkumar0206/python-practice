class Student:
    def __init__(self, name):
        self._name = name   # protected

s = Student("Ravi")
print(s._name)    # allowed, but not recommended
