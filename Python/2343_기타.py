import sys

n,m = map(int, sys.stdin.readline().split())

#강의는 n , 블루레이는 m

s = list(map(int, sys.stdin.readline().split()))

start = max(s)
end = sum(s)

result = 0
while start <= end :
    mid = (start + end) // 2

    dvd = 0 #dvd 플레이타임
    cnt = 0 #블루레이갯수
    for i in s :
        if dvd + i > mid :
            cnt += 1
            dvd = 0
        dvd += i

    if dvd :
        cnt +=1

    if cnt > m :
            start = mid + 1
            
    else :
            end = mid - 1
            result = mid 

print(result)

#9 3       
#1 2 3 4 5 6 7 8 9

