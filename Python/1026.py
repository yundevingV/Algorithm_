import sys

n = int(sys.stdin.readline())

a = []
b = []

a=map(int, input().split())
a = list(a)

b=map(int, input().split())
b = list(b)
sum=0


while True :

    if n != 0 :
        ma=max(a)
        mb=min(b)
        sum += ma *mb
        a.remove(ma)
        b.remove(mb)
        n-=1
    else :
        print(sum)
        break;

    