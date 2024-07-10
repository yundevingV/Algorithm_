function solution(n, wires) {
    let answer = Number.MAX_SAFE_INTEGER; // 최소값을 찾기 위함

    // 인덱스는 0부터 전선은 1부터 시작하기 때문에 n + 1
    const graph = Array.from(Array(n + 1), () => []);
    // 인덱스는 노드, 해당 인덱스에 연결된 노드들을 저장
    // 각 전선을 연결된 노드들로 그래프에 추가
    wires.forEach((wire) =>{
      let [from, to] = wire;

      graph[from].push(to);
      graph[to].push(from);
    })
  
    // 출발지점 과 가지않는곳 (연결이 끊긴곳)     
    const dfs = (start,except) => {
        let visited = Array.from(Array(n + 1), () => false);
        let count = 0
        let q = [start]
        console.log(q)

        visited[start] = true
        // 큐가 비워질때까지
        while(q.length) {
            let n = q.shift()
            graph[n].forEach((i)=>{
                console.log(i)
                // 연결이 끊기지않고 방문가능하지않은곳
                if(i !== except && visited[i] === false){
                    visited[i] = true
                    q.push(i)
                }
            })
          count++;
        }
        return count
    }
    
    
    wires.forEach((i)=>{
        let [a,b] = i
        console.log(`${i} ___`)
        answer = Math.min(answer,Math.abs(dfs(a,b) - dfs(b,a)))
    })
    return answer;
}