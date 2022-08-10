import sys

num = int(sys.stdin.readline())


for i in range(num) :
    num, s = input().split()
    num = int(num)
    for j in s :
        jn = j*num
        print(jn,end='')
    print()


