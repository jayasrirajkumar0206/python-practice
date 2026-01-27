class Test:
    def add(self, a, b, c=0):
        print(a + b + c)

t = Test()
t.add(2, 3)        # 5
t.add(2, 3, 4)     # 9
