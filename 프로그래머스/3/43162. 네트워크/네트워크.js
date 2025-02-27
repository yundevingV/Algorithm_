function dfs(visited, computers, index) {
    visited[index] = 1; 
    for (let i = 0; i < computers[index].length; i++) {
        if (!visited[i] && computers[index][i]) {
            dfs(visited, computers, i);
        }
    }
}

function solution(n, computers) {
    let answer = 0; 
    let visited = new Array(n).fill(0);

    for (let i = 0; i < n; i++) {
        if (!visited[i]) { 
            dfs(visited, computers, i); 
            answer++; 
        }
    }
    return answer; 
}
