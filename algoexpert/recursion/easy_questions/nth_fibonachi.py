def getNthFib(n):
    a, b = 0, 1

    for _ in range(n-1):
        temp = a
        a = b
        b += temp

    return a

# 1 -> 0, 2 -> 1, 3-> 1 + 1