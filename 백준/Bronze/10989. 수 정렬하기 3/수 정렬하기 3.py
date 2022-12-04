import sys

num = int(sys.stdin.readline())
lst=[0] * 10001

for i in range(num) :
    a = int(sys.stdin.readline())
    lst[a]+= 1

for i in range(len(lst)) :
    if lst[i] >=1 :
        for j in range(lst[i]) :
            print(i)