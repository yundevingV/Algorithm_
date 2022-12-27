let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log

n = Number(input[0])

let lst = []

for (let i = 1; i < input.length ; i++) {
    if (input[i] !== '') {
        lst.push(input[i].split(' '));
    }

}

for (let i = 0 ; i < lst.length ; i++){
    for (let j = 0 ; j < lst.length ; j++){
        lst[i][j] = Number(lst[i][j])    
    }
}

let visited = []

for (let i = 0 ; i < n ; i++){
    visited[i] =0 
    
}

//최대값 생성
let minimumNumber = Number.MAX_SAFE_INTEGER;


dfs = (x,p) => {
    if (x === n/2) {

        let result = []
        let other = []
        let resultSum = 0
        let otherSum = 0
        //팀 조깨기
        for(let i = 0 ; i < n ; i++){
            if (visited[i]) {
                result.push(i)
            }
            else {
                other.push(i)
            }
        }
        //계산
        // c('r',result)
        // c(other)
        let s = n/2
        for(let i = 0 ; i < s ; i++){
            for(let j = i+1 ; j < s ; j++){
                resultSum = resultSum + lst[result[i]][result[j]] + lst[result[j]][result[i]]
                otherSum = otherSum + lst[other[i]][other[j]] + lst[other[j]][other[i]]
            }
        }
        minimumNumber = Math.min(minimumNumber, Math.abs(resultSum - otherSum))
        return
        }   
        for(let i = p ; i < n ; i++){
            visited[i] = 1    
            dfs(x+1,i+1)
            visited[i] = 0
            
        }

}
dfs(0,0)

c(minimumNumber)