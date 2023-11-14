function solution(maps) {

    let targetX = maps.length-1;
    let targetY = maps[0].length-1;
    
    let dx = [1,-1,0,0];
    let dy = [0,0,1,-1];
    
    let queue = [];

    queue.push([0,0,1]);
    
    while(queue.length > 0){

        let [x,y,count] = queue.shift();

        if(x === targetX && y === targetY){
            return count;
        }

        for(let i=0;i<4;i++){
            let nx = x + dx[i];
            let ny = y + dy[i];
            if(nx >= 0 && ny >= 0 && nx <= targetX && ny <= targetY && maps[nx][ny] === 1){
                maps[nx][ny] = 0;
                queue.push([nx,ny,count+1]);
            }
        }
    }
    return -1;

}
