let fs = require('fs');
const filePath = process.platform === "linux" ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().trim().split(' ');
const c = console.log

let lst = []

for (let i=0 ; i < input.length ; i++){
    lst.push(Number(input[i]))
}

n = lst[0]
m = lst[1]

let visited = []

for(let i = 0 ; i< n+1 ; i++){
    visited[i] = false
}

let output = []
let result = ''

dfs = (count) => {
    if (count === m+1) {
        result += `${output.join(' ')}\n`
        c(visited)
    }
    
    for (let i = 1; i < n+1 ; i++) {
        c(count , i)
        c(output)

        if (visited[i] === true) continue
        else{
            visited[i] = true
            output.push(i)
            dfs(count+1)
            output.pop()
            visited[i] = false
        }
        }
    }

dfs(1)
c(result.trim())