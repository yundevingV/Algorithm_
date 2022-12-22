import sys

n= int(sys.stdin.readline())
lst =[]
for _ in range(n):
    n, d, m, y = input().split()
    lst.append((n, int(d), int(m), int(y)))

lst.sort(key=lambda x:(x[3],x[2],x[1]))


print(lst[-1][0])
print(lst[0][0])


