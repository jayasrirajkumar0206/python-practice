class Bank:
    def __init__(self, balance):
        self.__balance = balance   # private

    def get_balance(self):
        return self.__balance

    def add_money(self, amt):
        self.__balance += amt

b = Bank(1000)

print(b.get_balance())   # allowed
b.add_money(500)
print(b.get_balance())
