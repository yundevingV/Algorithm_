import sys,math

num = int(sys.stdin.readline())
for i in range(num) :
    x1,y1,r1,x2,y2,r2 = [int(x) for x in sys.stdin.readline().split()]

    d = math.sqrt( math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    minus = r1 -r2
    plus= r1+r2
    if abs(minus) < d and plus > d :
        print(2)
    elif x1 == x2 and y1 == y2 and r1 == r2 :
        print(-1)
    elif abs(minus) == d or plus == d :
        print(1)
    elif plus < d or abs(minus) > d :
        print(0)
    

