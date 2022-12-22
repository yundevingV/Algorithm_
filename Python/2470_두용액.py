import sys

n = int(sys.stdin.readline())
#n은 용액의 갯수

result = []

lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

pivot = 1e9 * 2 

#start, end 설정
s , e= 0,n-1

while s < e :
    r = (lst[s] + lst[e]) 
    
    if abs(r) < pivot :
        result.clear()
        result.append(lst[s])
        result.append(lst[e])
        pivot = abs(r)

    if r < 0 :
        s = s + 1
    else :
        e = e - 1


#오름차순으로 출력.
result.sort()

for i in result :
    print(i,end=' ')


#반례
# 3
# 999999998 999999999 1000000000
# 999999998 999999999 