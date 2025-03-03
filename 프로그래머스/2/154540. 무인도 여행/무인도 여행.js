// 방문하지 않았고 X가 아닌곳에서 bfs 시작
// 섬에 도착하고 X가 아닌 곳 모두 더함
// answer에 추가
function solution(maps) {
    var answer = [];
    let w = maps[0].length;
    let h = maps.length;
    const visited = Array.from({ length: h }, () => Array(w).fill(false));

    
    function bfs(startX, startY, visited) {
        let queue = [];
        let temp = 0;
        
        queue.push([startX,startY]);
        visited[startY][startX] = true;
        temp += Number(maps[startY][startX]);
        
            while(queue.length) { 
                
                const dx = [1,-1,0,0];
                const dy = [0,0,1,-1];

                const [x,y] = queue.shift();

                for (let i=0;i<dx.length;i++){
                    let nx = x + dx[i];    
                    let ny = y + dy[i];

                     if(0 <= nx && nx < w && 0 <= ny && ny < h){
                       if(!visited[ny][nx] && maps[ny][nx] !== 'X'){
                            visited[ny][nx] = true;
                            temp += Number(maps[ny][nx]);
                            queue.push([nx,ny])
                        }
                    }
                }
            }
        answer.push(temp);
    } 
    for (let i=0;i<w;i++){
        for(let j=0;j<h;j++){
            if(!visited[j][i] && maps[j][i] !== 'X'){
                bfs(i,j,visited);
            }
        }
    }
    return answer.length > 0 ? answer.sort((a, b) => a - b) : [-1]; 
}