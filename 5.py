from fnmatch import *
o = "13579"
e = "02468"
k = 2023

for x in range(11001074, 11999911, k):
    for o1 in o:
        for e1 in e:
            if fnmatch(str(x), f"11{e1}??{o1}11"):
                print(x, x // 2023)