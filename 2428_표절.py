import sys

n = int(sys.stdin.readline())

lst = []

lst = list(map(int, sys.stdin.readline().split()))


lst.sort()

#size(Fi) ≤ size(Fj)이면서, size(Fi) ≥ 0.9 × size(Fj)

cnt = 0

for i in range(len(lst)) :
    start = 0
    end = len(lst)

    while start < end :
        mid = (start + end) // 2
        if lst[i] >= 0.9*lst[mid] :
            start = mid +1
        else :
            end = mid 
    cnt += end-i-1

print(cnt)
