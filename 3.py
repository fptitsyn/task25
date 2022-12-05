def isprime(n):
    if n == 1:
        return False
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True

for x1 in range(105000000, 115000000 + 1):
    x = x1
    while x % 2 == 0:
        x //= 2
    m = x ** 0.25
    if int(m) == m and isprime(m):
        print(x1, m ** 4)
        