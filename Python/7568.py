import sys

n = int(sys.stdin.readline())
lst =[]
for i in range(n) :
    x = list(map(int, input().split()))
    lst.append(x)


r=[]
for i in lst :

    rank = 1
    for j in lst :
        if i[0] < j[0] and i[1] < j[1] :
            rank +=1
    r.append(rank)

for k in r :
    print(k,end=' ')

