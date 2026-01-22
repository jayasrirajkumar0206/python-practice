"""Q7. Input a word and print:
First character
Last character
Middle part"""

B = str(input("Enter a string :"))
print(B[0:1])
print(B[-1])
mid=len(B)//2
print(mid)
print("Middle part:", B[1:mid])
