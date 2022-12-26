let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log

n = input[0]
c(n)

let lst = []

for (let i = 1; i < input.length ; i++) {
    if (input[i] !== '') {
        lst.push(input[i].split(' '));
    }
}

for (let i = 0 ; i < lst.length ; i++){
    if (lst[i].length == n ) {
        lst[i][3] = lst[i][3].replace(/\r/,"")
    } 

}

for (let i = 0 ; i < lst.length ; i++){
    for (let j = 0 ; j < lst.length ; j++){
        lst[i][j] = Number(lst[i][j])    
    }
}

let visited = []

for (let i = 0 ; i < lst.length ; i++){
    visited[i] = 0
    
}
c(visited)

let result = []

dfs = (x) => {
    if (x === n) {

    } else {
        for(let i = 0 ; i < n ; i ++){
            if(check(i,x)) {
                visited[x] = i
            }
            dfs(x+1)
            visited[x] = 0
        }
    }

}

check = (i,x) => {
    if (i ===  x+1) return false
    for (let k = 0 ; k < visited.length ; k++){
        if(i === visited[k]) return false
    }
    return true
}

dfs(0)

c(lst)