from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    # 처음 방문
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    
    # 이동방향
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위에 벗어나지 않고 1이면
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                if not visited[ny][nx]:
                    # 방문처리
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    maps[ny][nx] = maps[y][x] + 1

    if maps[n-1][m-1] == 1:
        return -1
    
    return maps[n-1][m-1]
