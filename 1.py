def isprime(n):
    if n == 1:
        return False
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True
    
a = []
for i in range(2, 15000):
    if isprime(i):
        a.append(i)
    
c = 0
m = 529700
xans = 529700
ans = set()

for i in a:
    for j in a:
        for k in a:
            if i == k or i == j or j == k:
                continue
            if i % 10 == j % 10 == k % 10:
                if 485617 <= i * j * k <= 529678:
                    c += 1
                    ans.add(i * j * k)
                    if max(i, j, k) - min(i, j, k) < m:
                        m = max(i, j, k) - min(i, j, k)
                        xans = i * j * k
                        b = [i, j, k]
            if i * j * k > 529678:
                break
                        
print(len(ans), xans)
