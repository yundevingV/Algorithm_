import sys

n = int(sys.stdin.readline())
x = set(map(int, input().split()))

m = int(sys.stdin.readline())
y = list(map(int, input().split()))

lst =[0] * m

for i in range(m) :
    if y[i] in x :
        print('1',end=' ')
    else :
        print('0',end=' ')

#순서와 중복을 상관하지않을땐
#리스트 보단 set(집합)으로 !