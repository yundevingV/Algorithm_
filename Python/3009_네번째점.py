import sys

lstx = []
lsty = []

for _ in range(3) :
    x,y = map(int, sys.stdin.readline().split())
    lstx.append(x)
    lsty.append(y)

result = []

for i in lstx :
    if lstx.count(i) != 2 :
        result.append(i)

for i in lsty :
    if lsty.count(i) != 2 :
        result.append(i)

for i in result :
    print(i,end=' ')