import sys

n = int(sys.stdin.readline())

d=[0] * (n+1)

#t는 시간 p는 보상
lstt = []
lstp = []
for _ in range(n) :
    t,p = map(int, sys.stdin.readline().split())
    lstt.append(t)
    lstp.append(p)

for i in range(0,n) :
    if lstt[i] + i <= n :
        d[i] = max(d[i+1] , lstp[i] + d[i+lstt[i]])
    else :
        d[i] = d[i+1]

print(d)
print(d[n])