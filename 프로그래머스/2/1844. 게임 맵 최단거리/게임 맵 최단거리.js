function solution(maps) {
    var answer = 0;
    
    let dx = [1, -1, 0, 0];
    let dy = [0, 0, 1, -1];
    let lenX = maps.length
    let lenY = maps[0].length
    let q = []
    q.push([0,0])
    
    let visited = Array.from({ length: maps.length }, 
            () => Array(maps[0].length).fill(false));

    while (q.length){
        let [x,y] = q.shift()
        visited[x][y] = true
        for (let i =0;i<4;i++){
            let nx = x + dx[i]
            let ny = y + dy[i]
            if((0<=nx) && (nx<lenX) && (0<=ny) && (ny < lenY)){
                if(maps[nx][ny] == 1){
                    if(!visited[nx][ny]){
                        q.push([nx,ny])
                        maps[nx][ny] = maps[x][y] + 1 
                    }
                }
            }
        }
    }
    
    return maps[lenX-1][lenY-1] === 1 ? -1 : maps[lenX-1][lenY-1];
}