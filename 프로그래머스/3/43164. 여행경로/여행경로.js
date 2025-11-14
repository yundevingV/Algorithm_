function solution(tickets) {
    var answer = [];
    const sortedTickets = tickets.sort();
    let visited = new Array(tickets.length).fill(0);
    const dfs = (start,count,route) => {
        if(count === tickets.length) {
            answer.push(route);
            return;
        }
        for(let i=0;i<tickets.length;i++) {
            if(!visited[i] && start === tickets[i][0]) {
                visited[i] = 1;
                dfs(tickets[i][1],count+1,route+" "+tickets[i][1]);
                visited[i] = 0;
            }
        }
    }
    dfs("ICN",0,"ICN");
    
    return answer[0].split(' ');
}