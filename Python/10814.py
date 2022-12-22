import sys

n= int(sys.stdin.readline())
lst =[]
for _ in range(n):
    a,b= input().split()
    lst.append((int(a),b))

lst.sort(key=lambda x:(x[0]))

for j in range(len(lst)) :
    for k in range(2) :
        print(lst[j][k], end=' ')
    print(end='\n')