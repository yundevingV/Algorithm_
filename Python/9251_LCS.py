import sys

a = input()
b = input()

d1 = [0] * len(a)
d2 = [0] * len(b)

for i in range(len(a)) :
    for j in range(len(b)) :
        if a[i] == b[j] :
            d1[i] += 1

print(max(d1))
            
            