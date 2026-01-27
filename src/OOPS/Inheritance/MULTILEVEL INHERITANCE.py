class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

class C(B):
    def test(self):
        print("Class C")

c = C()
c.show()
c.display()
c.test()
