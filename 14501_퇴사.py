import sys

n = int(sys.stdin.readline())

d=[0] * (n+1)

#t는 시간 p는 보상
lstt = [0]
lstp = [0]
for _ in range(n) :
    t,p = map(int, sys.stdin.readline().split())
    lstt.append(t)
    lstp.append(p)


#d[n] = max(d[n+1] , lstp[n]+d[n+lstt[n]])

