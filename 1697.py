from collections import deque
import sys

n,k = map(int, sys.stdin.readline().split())
# n이 내 위치 k가 목표위치
maxnum = 100000
visited = [0 for _ in range(100001)]


def move(i,x) :
    if i == 0 and 0 <= x+1 <= maxnum:
        return x+1
    elif i == 1 and 0 <= x-1 <= maxnum :
        return x-1
    elif i ==2 and 0 <= x*2 <= maxnum :
        return x*2
    else :
        return -5

def bfs() :
    q = deque()
    q.append(n)
    visited[n] = 1
    while q :
        x = q.popleft()
        if x == k :
            print(visited[x]-1)
            break
        for i in range(3) :
            nx = move(i,x)
            if 0 <= nx <= maxnum and visited[nx] == 0 :
                visited[nx] = visited[x] +1
                q.append(nx)

bfs()
