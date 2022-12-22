import sys

n = int(sys.stdin.readline())

for i in range(n) :
    lst = list(map(int, sys.stdin.readline().split()))
    lst.sort()
    del lst[0]
    lst.pop()
    if lst[-1] - lst[0] < 4 :
        print(sum(lst))
    else :
        print('KIN')
