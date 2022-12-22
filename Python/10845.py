import sys

q = []

n = int(sys.stdin.readline())

for i in range(n) :
    lst = sys.stdin.readline().split()
    if lst[0] == 'push' :
        q.append(lst[1])
    elif lst[0] == 'front' :
        if len(q) == 0 :
            print('-1')
        else :
            print(q[0])
    elif lst[0]  == 'back' :
        if len(q) == 0 :
            print('-1')
        else :
            print(q[-1])
    elif lst[0]  == 'size' :
        print(len(q))
    elif lst[0]  == 'pop' :
        if len(q) == 0 :
            print('-1')
        else :
            print(q[0])
            del q[0]
    elif lst[0]  == 'empty' :
        if q :
            print('0')
        else :
            print('1')            
