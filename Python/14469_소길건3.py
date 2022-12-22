import sys

n= int(sys.stdin.readline())

lst = []

for i in range(n) :
    x,y = map(int, sys.stdin.readline().split())
    lst.append((x,y))

lst.sort()
c =0
for i in range(n) :
    if c <= lst[i][0] :
        c = lst[i][0] + lst[i][1]
    else :
        c += lst[i][1] 



print(c)