import sys
n,m = map(int, sys.stdin.readline().split())

money = []

for i in range(n) :
    t = int(sys.stdin.readline())
    money.append(t)

s = min(money)
e = sum(money)

r = 0
while s <= e :
    mid = (s+e) // 2
    a = 0
    c = 0

    for i in money :
        if a < i : 
            c+=1
            a = mid
        a-=i

    if c > m or mid < max(money):
        s = mid + 1
        
    else :
        e = mid - 1 
        r=mid
        

print(r)