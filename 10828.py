import sys

s = []

n = int(sys.stdin.readline())

for i in range(n) :
    lst = sys.stdin.readline().split()
    if lst[0] == 'push' :
        s.append(lst[1])
    elif lst[0]  == 'size' :
        print(len(s))
    elif lst[0]  == 'pop' :
        if len(s) == 0 :
            print('-1')
        else :
            print(s[-1])
            s.pop()
    elif lst[0]  == 'empty' :
        if s :
            print('0')
        else :
            print('1')            
    elif lst[0]  == 'top' :
        if s :
            print(s[-1])
        else :
            print(-1)            
