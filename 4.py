s1 = ' 0123456789'
s2 = '0123456789'

ans = set()

for i1 in s1:
    for i2 in s1:
        for i3 in s1:
            for i4 in s1:
                for i5 in s2:
                    s = f"4{i1}{i2}{i3}{i4}1{i5}009"
                    s = s.replace(" ", "")
                    x = int(s)
                    if int(x ** 0.5) == x ** 0.5:
                        ans.add((int(x ** 0.5), x))
                        
print(ans)
    