import sys

n = int(sys.stdin.readline())

lst = []

d = []

#2차원 배열 생성
for i in range(n) :
    a = list(map(int, sys.stdin.readline().split()))
    lst.append((a))
    d.append((a))

for i in range(1,n) : 
    for j in range(len(lst[i])) :
        if j == 0 :
            d[i][j] = lst[i-1][j] + lst[i][j]
        elif j == i :
            d[i][j] = lst[i][j] + lst[i-1][j-1]
        else :
            d[i][j] = max(lst[i-1][j] + lst[i][j] , lst[i][j] + lst[i-1][j-1])

print(max(d[n-1]))
