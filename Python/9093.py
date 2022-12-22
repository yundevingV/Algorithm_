from audioop import reverse
import sys

num = int(sys.stdin.readline())
lst = []
for i in range(num) :
    str = input().split(' ')
    for j in str :
        print(j[::-1],end=' ')
    print('',end='\n')
