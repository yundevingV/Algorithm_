function solution(maps) {
    const height = maps.length;
    const width = maps[0].length;
    
    // 1. 방향 벡터 (상, 하, 좌, 우)
    const dx = [0, 0, 1, -1];
    const dy = [1, -1, 0, 0];
    

    let visited = Array.from({ length: height }, () => Array(width).fill(0));
    let queue = [];
    queue.push([0, 0]); 
    visited[0][0] = 1;  
    
    while (queue.length > 0) {
        let [y, x] = queue.shift(); 
        
        for (let i = 0; i < 4; i++) {
            let ny = y + dy[i];
            let nx = x + dx[i];
            
            if (ny >= 0 && ny < height && nx >= 0 && nx < width) {
                if (maps[ny][nx] === 1 && visited[ny][nx] === 0) {
                    visited[ny][nx] = 1;
                    maps[ny][nx] = maps[y][x] + 1;
                    queue.push([ny, nx]);
                }
            }
        }
    }

    const answer = maps[height - 1][width - 1];
    
    return answer === 1 ? -1 : answer;
}