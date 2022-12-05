def isprime(n):
    if n == 1:
        return False
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True
    
a = set()
for i in range(2, 15000):
    if isprime(i):
        a.add(i)
    
m = 529700
xans = 529700
ans = set()

for x in range(485617, 529678 + 1):
    for k1 in range(2, int(x ** 0.5) + 1):
        if x % k1 == 0 and k1 in a:
            for k2 in range(2, int((x // k1) ** 0.5) + 1):
                if x // k1 % k2 == 0 and k2 in a and k1 != k2 and k1 % 10 == k2 % 10:
                    k3 = x // k1 // k2
                    if k3 in a and k3 % 10 == k2 % 10 and k3 != k2 and k3 != k1:
                        ans.add(x)
                        if max(k1, k2, k3) - min(k1, k2, k3) < m:
                            xans = x
                            m = max(k1, k2, k3) - min(k1, k2, k3)
                            
print(len(ans), xans)
            