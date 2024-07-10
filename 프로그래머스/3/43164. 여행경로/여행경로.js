function solution(tickets) {
    var answer = [];
    let len = tickets.length
    // 알파벳순서
    tickets.sort()
    // 방문
    let visited = Array(len).fill(false)
    
    const dfs = (now,count,route) => {
        if(count === len){
            answer.push(route)
            return
        }
        for(let i=0;i<len;i++){
            if(!visited[i] && now === tickets[i][0]){
                visited[i] = true
                dfs(tickets[i][1],count+1,route+" "+tickets[i][1])
                visited[i] = false
            }
        }
    }
    
    dfs("ICN",0,"ICN")
    
    return answer[0].split(' ');
}