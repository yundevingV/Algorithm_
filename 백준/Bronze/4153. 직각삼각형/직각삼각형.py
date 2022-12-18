import sys

while True :
    lst = []
    x,y,z = map(int, sys.stdin.readline().split())
    
    lst.append(x)
    lst.append(y)
    lst.append(z)
    lst.sort()



    xx = lst[0] * lst[0]
    yy = lst[1] * lst[1]
    zz = lst[-1] * lst[-1]

    if x == 0 and y == 0 and z == 0 :
        break

    if zz == yy + xx :
        print('right')
    else :
        print('wrong')