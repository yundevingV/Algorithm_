import sys

lst1 = []
lst2 = []

n,m = map(int,sys.stdin.readline().split())

for i in range(n) :
    inputLst = list(map(int,sys.stdin.readline().split()))
    lst1.append(inputLst)
for i in range(n) :
    inputLst = list(map(int,sys.stdin.readline().split()))
    lst2.append(inputLst)


for i in range(n) :
    for j in range(m) :
        lst1[i][j] += lst2[i][j]
    
for i in range(n) :
    for j in range(m) :
        print(lst1[i][j],end=' ')
    print(end='\n')

