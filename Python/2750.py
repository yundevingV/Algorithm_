import sys

num = int(sys.stdin.readline())
list=[]

for i in range(num) :
    a = int(sys.stdin.readline())
    list.append(a)


list.sort()

for i in list :
    print(i)
