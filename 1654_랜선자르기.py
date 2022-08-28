import sys

k,n = map(int, sys.stdin.readline().split())
#k는 가지고있는 랜선의 갯수
#n은 만들고자하는 랜선의 갯수

lst=[]

for _ in range(k) :
    fostjs = int(sys.stdin.readline())
    lst.append(fostjs)

lst.sort()

start = 1
end = max(lst)

while start <= end :
    aa = 0

    mid = (start + end ) // 2
    for i in lst :
        aa += i // mid 
    if n <= aa :
        start = mid + 1 
    else :
        end = mid - 1 

print(mid-1)

#이분탐색은 일단 반을 잘라보고 
#그보다 작으면 start = mid +1
#반대면 end = mid =1
