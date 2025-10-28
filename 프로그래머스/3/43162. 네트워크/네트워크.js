const dfs = (i,visited,computers) => {
    visited[i] = 1;
    for(let j=0;j<computers[i].length;j++) {
        if(!visited[j] && computers[i][j]) {
            dfs(j,visited,computers);
        }
    }    
}

function solution(n, computers) {
    var answer = 0;
    
    let visited = new Array(n).fill(0);
    for(let i=0; i<n;i++) {
        if(!visited[i]) {
            dfs(i,visited,computers);    
            answer++;
        }
        
    }
    
    
    return answer;
}