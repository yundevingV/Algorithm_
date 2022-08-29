import sys

n,c = map(int, sys.stdin.readline().split())

#n은 집의개수 , c는 공유기의 개수
lst = []
for _ in range(n) :
    o = int(sys.stdin.readline())
    lst.append(o)

lst.sort()

start = 1 
end = max(lst)

while start <= end :
    mid =(start + end) // 2
    