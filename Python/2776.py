import sys

n = int(sys.stdin.readline())


for i in range(n) :
    s1s = int(sys.stdin.readline())
    s1= set(map(int, sys.stdin.readline().split()))    

    s2s = int(sys.stdin.readline())
    s2= list(map(int, sys.stdin.readline().split()))
    for i in s2 :
        if i in s1 :
            print(1)
        else :
            print(0)
