function solution(maps) {
    let W = maps[0].length;
    let H = maps.length;
    
    let visited = Array.from({ length: H }, () => new Array(W).fill(false));
    
    let dx = [1, -1, 0, 0];
    let dy = [0, 0, 1, -1];
    
    let queue = [[0, 0]];
    visited[0][0] = true;
    
    while (queue.length > 0) {
        let [x, y] = queue.shift();
        
        for (let i = 0; i < 4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];
            
            if (nx >= 0 && nx < H && ny >= 0 && ny < W) {
                if (!visited[nx][ny] && maps[nx][ny] === 1) {
                    visited[nx][ny] = true;
                    maps[nx][ny] = maps[x][y] + 1;
                    queue.push([nx, ny]);
                }
            }
        }
    }
    
    let answer = maps[H - 1][W - 1];
    return answer === 1 ? -1 : answer;
}