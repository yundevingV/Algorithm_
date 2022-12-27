let fs = require('fs');
const { resourceLimits } = require('worker_threads');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`;  
let input = fs.readFileSync(filePath).toString().trim().split('\n');
const c = console.log
c(input)
let lst = []

let result = ''
let output = []

for (let i = 0 ; i < input.length ; i++){
    for(let j = 0 ; j < input[i].length ; j+=2)
        c(input[i][j])
}


dfs = (x) => {
    if (x === 6){
        result += `${output.join(' ')}\n`
    }
    

}

dfs(0)