def count_even_odd(lst):
    even = 0
    odd = 0

    for x in lst:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd

lst = [10,12,23,34,56,77]
print(count_even_odd(lst))
