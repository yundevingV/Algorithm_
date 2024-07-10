function solution(n, computers) {
    var answer = 0;
    let v = Array(n+1).fill(false)    
    const dfs = (idx,v) => {
        v[idx] = true
        for(let i = 0;i<computers[idx].length;i++){
            if((i !== idx) && (computers[idx][i] === 1) &&(!v[i]) ){
                dfs(i,v)
            }
        }
    }
   for(let i =0;i<computers.length;i++){
       if(!v[i]){
            dfs(i,v)    
            answer+=1
       }
}
    
    return answer; 
    }
    