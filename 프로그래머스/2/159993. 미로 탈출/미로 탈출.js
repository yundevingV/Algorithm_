function solution(maps) {
    const w = maps[0].length;
    const h = maps.length;
    
    const dx = [0, 0, 1, -1];
    const dy = [1, -1, 0, 0];

    // BFS 함수
    function bfs(startX, startY, targetChar) {
        const visited = Array.from({ length: h }, () => Array(w).fill(false));
        const queue = [[startX, startY]];
        visited[startY][startX] = true;
        let distance = 0;

        while (queue.length > 0) {
            const size = queue.length;

            for (let i = 0; i < size; i++) {
                const [x, y] = queue.shift();

                // 목표 문자 도달 시 거리 반환
                if (maps[y][x] === targetChar) {
                    return distance;
                }

                // 인접한 칸 탐색
                for (let j = 0; j < dx.length; j++) {
                    const nx = x + dx[j];
                    const ny = y + dy[j];

                    // 범위 검사 및 방문 여부 검사
                    if (0 <= nx && nx < w && 0 <= ny && ny < h && !visited[ny][nx] && maps[ny][nx] !== 'X') {
                        visited[ny][nx] = true;
                        queue.push([nx, ny]);
                    }
                }
            }
            distance++;
        }

        return -1; // 목표에 도달하지 못한 경우
    }

    // 시작점 찾기
    let startX, startY;
    for (let i = 0; i < h; i++) {
        for (let j = 0; j < w; j++) {
            if (maps[i][j] === 'S') {
                startX = j;
                startY = i;
            }
        }
    }

    // 레버까지의 거리
    const leverDistance = bfs(startX, startY, 'L');
    if (leverDistance === -1) return -1; // 레버에 도달할 수 없는 경우

    // 레버 위치 찾기
    let leverX, leverY;
    for (let i = 0; i < h; i++) {
        for (let j = 0; j < w; j++) {
            if (maps[i][j] === 'L') {
                leverX = j;
                leverY = i;
            }
        }
    }

    // 출구까지의 거리
    const exitDistance = bfs(leverX, leverY, 'E');
    if (exitDistance === -1) return -1;

    // 총 거리 반환
    return leverDistance + exitDistance;
}


