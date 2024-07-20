function solution(n, computers) {
    var answer = 0;
    let visited = new Array(n).fill(false);

    const dfs = (index) => {
        visited[index] = true;
        for (let i = 0; i < n; i++) {
            if (computers[index][i] === 1 && !visited[i]) {
                dfs(i);
            }
        }
    };

    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i);
            answer += 1;
        }
    }

    return answer;
}
