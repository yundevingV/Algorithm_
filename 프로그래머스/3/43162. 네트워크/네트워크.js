function solution(n, computers) {

    const visited = Array(n).fill(false);
    var answer = 0;

    function dfs(v) {
      visited[v] = true;
      computers.forEach((value,idx) => {
        if(!visited[idx] && value[v])  
            dfs(idx);
            }
        )
    }

    computers.forEach((_,i) => {
        console.log(i)
        if(!visited[i]){
        dfs(i);
        answer++;    
        }

    })
    return answer;
}

