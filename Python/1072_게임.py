import sys

x,y = map(int, sys.stdin.readline().split())
# x 경기수
# y 승리수

z = (y * 100) / x
z = int(z)


if z >= 99 :
    print(-1)
else :
    r = 0
    left = 1
    right = x
    while left <= right :
        mid = (left + right) // 2
        if int(((y+mid) * 100) / (x+mid)) <= z :
            left = mid +1
        else :
            r = mid
            right = mid -1
    print(r)    
        




