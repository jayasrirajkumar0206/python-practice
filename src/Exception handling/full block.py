try:
    a = int(input("Enter number: "))
    print(10 / a)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("No exception occurred")
finally:
    print("This will always execute")
