class A:
    def show(self):
        print("Class A")

class B:
    def display(self):
        print("Class B")

class C(A, B):
    def test(self):
        print("Class C")

c = C()
c.show()
c.display()
c.test()
