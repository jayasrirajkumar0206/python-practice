def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n

n = int(input())
print(is_perfect(n))
