import sys

n = int(sys.stdin.readline())

for i in range(n) :
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())

    planet = 0

    nn = int(sys.stdin.readline())
    for i in range(nn) :
        x,y,r = map(int, sys.stdin.readline().split())
        a = ((x1-x)**2+(y1-y)**2)**0.5
        b = ((x2-x)**2+(y2-y)**2)**0.5

        if (a > r and b < r ) or (a < r and b > r) :
            planet +=1
        
    print(planet)