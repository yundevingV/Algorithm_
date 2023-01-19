let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log

n = Number(input[0])

let lst = []

for(let i = 1 ; i < n+1 ; i++){
    let numbers = input[i].split(" ").map(Number)
    lst.push(numbers)
}
lst.sort((a, b) => {
        return a[0] - b[0]
    })

lst.sort((a,b) =>{
        return a[1] - b[1]
})

final = 0
let temp = 0 

for(i in lst){
    if (lst[i][0] >= final){
        temp +=1
        final = lst[i][1]
    }
}

c(temp)