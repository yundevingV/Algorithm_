import sys

n = int(sys.stdin.readline())

lst = list(map(int , sys.stdin.readline().split()))

lst.sort()

if len(lst) % 2 == 1 :
    print(lst[(len(lst)//2)]**2)
else :
    print(lst[0] * lst[-1])
