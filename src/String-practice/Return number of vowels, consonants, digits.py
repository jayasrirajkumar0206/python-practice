def count_all(s):
    c = 0
    v = 0
    d = 0
    for ch in s:
        if ch.isdigit():
            d += 1
        elif ch.isalpha():
            if ch.lower() in "aeiou":
                v += 1
            else:
                c += 1
    return v, c, d


s = input()
print(count_all(s))
