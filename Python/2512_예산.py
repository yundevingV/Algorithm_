
import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

result = int(sys.stdin.readline())

lst.sort()

start = 0
end = max(lst)

while start <= end :
    mid = (start + end) //2 
    numsum = 0
    for i in lst :
        if i <= mid :
            numsum += i
        else :
            numsum += mid
    if numsum <= result :
        start = mid + 1
        #오른쪽이동
    else :
        end = mid -1 

print(end)