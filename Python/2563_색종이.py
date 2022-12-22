import sys

n = int(sys.stdin.readline())

rows = 100
cols = 100
matrix = [[0 for j in range(cols)] for i in range(rows)]


count = 0
for i in range(n) :
    a,b = map(int, sys.stdin.readline().split())
    for j in range(a,a+10) :
        for k in range(b,b+10) :
            if matrix[j][k] ==0 and j <= 100 and k <= 100 :
                count+=1
                matrix[j][k] = 1
            else : 
                matrix[j][k] = 1

print(count)