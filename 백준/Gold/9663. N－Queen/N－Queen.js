let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log

let n = Number(input[0])

let visited = []

for (let i=0 ; i < n ; i++){
    visited[i] = 0
}

let count = 0

dfs = (a) => {
    if (a === n ){
        count +=1
    }
    else {
        for(let i = 0 ; i < n ; i++){
            if (visited[a]) continue
            visited[a] = i
            if (check(a)){
                dfs(a+1)
            }
            visited[a] = 0
        }
    }
}

check = (x) => {
    for (let i = 0 ; i < x ; i++){
        if (visited[x] === visited[i]) return false
        if (Math.abs(visited[x] - visited[i]) === x-i) return false
    }
    return true
}

dfs(0)

c(count)