import sys

n,m = map(int, sys.stdin.readline().split())

#n은 나무 갯수 , m은 가져가야하는 나무갯수

lst = list(map(int, sys.stdin.readline().split()))

start = 1 
end = max(lst)

while start <= end :
    mid = (start + end) // 2
    r = 0
    for i in lst :
        if i >= mid :
            r += i - mid
    if r >= m :
        start = mid +1
    else :
        end = mid - 1

print(end)