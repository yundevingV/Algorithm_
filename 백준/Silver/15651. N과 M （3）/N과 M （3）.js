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

let output = []
let result = ''

dfs = (count) => {
    if (count === m) {
        result += `${output.join(' ')}\n`
        return ;
    }
    
    for (let i = 1; i < n+1 ; i++) {
            output.push(i)
            dfs(output.length)
            output.pop()
            }
        }
    
dfs(0)
c(result.trim())