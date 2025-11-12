function solution(rectangle, characterX, characterY, itemX, itemY) {
    var answer = 0;
    
    
    let grid = Array.from({length : 102 }, () => Array(102).fill(0));
    
    // 외벽 그리기
    for(const rect of rectangle) {
        // 좌표 2배로 만들기
        const [x1,y1,x2,y2] = rect.map((item) =>  item * 2);
        
        for(let i=x1;i<=x2;i++){
            grid[y1][i] = 1;
            grid[y2][i] = 1;
        }
        
        for(let i=y1;i<y2;i++){
            grid[i][x1] = 1;
            grid[i][x2] = 1;
        }
    }
    
    // 내벽 그리기
    for(const rect of rectangle) {
        // 좌표 2배로 만들기
        const [x1,y1,x2,y2] = rect.map((item) =>  item * 2);
        
        for(let x=x1+1;x<x2;x++) {
            for(let y=y1+1;y<y2;y++) {
                grid[y][x] = 0;
            }
        }
    }
    const [x,y,iX,iY] = [characterX * 2, characterY * 2, itemX * 2, itemY * 2]
    
    let queue = [[y,x,0]];
    
    let dy = [1,-1,0,0];
    let dx = [0,0,1,-1];
    
    while(queue.length > 0) {
        let [y,x,count] = queue.shift();
        grid[y][x] = 0;
        
        if(y === iY && x === iX) return count / 2;
        
        for(let i=0;i<4;i++) {
            let ny = y + dy[i];
            let nx = x + dx[i];
            if(0 <= ny && ny < 102 && 0 <= nx && nx < 102) {
                if(grid[ny][nx] === 1) {
                    queue.push([ny,nx,count + 1]);
                }
            }
        }
    }
    return answer;
}