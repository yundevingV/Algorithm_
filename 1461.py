import sys

pos = []
nev = []
sum1=0
sum2=0
result =0
count = 0

n,m = [int(x) for x in sys.stdin.readline().split()]
n=abs(n)
m=abs(m)
num_list = list(map(int, input().split()))

num_list.sort()

# 양수 음수 리스트
for i in num_list :
    if i >= 0 :
        pos.append(i)
    else :
        nev.append(-i)


if len(pos) > 0 and len(nev) == 0 :
    for w in range(n-1,-1,-m) :
        result += pos[w]*2
        count +=1
    if count >= n/m :
        result -= max(pos)
elif len(pos) == 0 and len(nev) > 0 :
    for z in range(0,n,m) :
        result += abs(nev[z]*2)
        count +=1
    if count >= n/m :
        result -= abs(max(nev))
elif len(pos) > 0 and len(nev) > 0 :
    for i in range(n-len(nev)-1,-1,-m) :
        result += pos[i] *2
        count +=1
    for j in range(0,n-len(pos),m) :
        result += abs(nev[j]*2) 
        count +=1
    if count >= (n/m) : 
        if max(pos) >= abs(max(nev)) :
            result -=max(pos)
        else :
            result -=abs(max(nev))


print(result)

