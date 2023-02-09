import sys

lst = []
for i in range(9) :
    inputLst = list(map(int,sys.stdin.readline().split()))
    lst.append(inputLst)
m= 0
ii = 0
for i in range(9) :
    if max(lst[i]) > m :  
        m = max(lst[i])
        ii = i
print(m)
print(ii+1 ,lst[ii].index(m)+1)
    