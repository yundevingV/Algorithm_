import sys

n,c = map(int, sys.stdin.readline().split())

#n은 집의개수 , c는 공유기의 개수
lst = []
for _ in range(n) :
    o = int(sys.stdin.readline())
    lst.append(o)


start = min(lst)
end = max(lst)-min(lst)

while start <= end :
    mid =(start + end) // 2
    p=0
    cnt=0
    for i in lst :
        pre = lst[p]
        if mid + pre <= i :
            p+=1
            cnt+=1
    if c <= cnt :
        end = mid - 1
    else :
        start = mid + 1

print(end)