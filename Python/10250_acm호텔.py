import sys

t = int(sys.stdin.readline())



for i in range(t) :
    #h층 w방수 n몇번째 손님
    h, w, n = map(int,sys.stdin.readline().split())
    c = 1 
    while n  > h :
        n-=h
        c+=1
    print(n,end='')
    if c >= 10 :
        print(c)
    else : 
        print('0',end='')
        print(c)