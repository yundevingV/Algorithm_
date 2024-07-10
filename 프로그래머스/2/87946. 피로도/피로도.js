function solution(k, dungeons) {
    var answer = 0;
    let len = dungeons.length
    
    const dfs = (k,d,c,v) => {
        answer = Math.max(answer,c)

        for(let i = 0;i<len;i++){
            if(k >= d[i][0] && !v[i]){
                
                v[i] = true
                dfs(k - d[i][1],d,c+1,v)
                v[i] = false
            }
        }
    }
    let v = Array(len).fill(false)
    dfs(k,dungeons,0,v)
    return answer
}