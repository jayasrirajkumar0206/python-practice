"""Count how many vowels in a string
Example
Input: education
Output: 5"""

V=str(input("Enter a word:"))
vowels="aeiouAEIOU"
count = 0

for ch in V:
    if ch in vowels:
        count += 1
print("no.o vowels:" , count )


