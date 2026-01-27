def remove_special(s):
    result = ""

    for ch in s:
        if ch.isalnum() or ch == " ":
            result += ch

    return result


s = input()
print(remove_special(s))
