let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log

let string = input[0].replace(/\s*/g, "");

let n = Number(input[1])

let inputsList = []

for(let i = 2 ; i < n+2 ; i++){
    let inputs = input[i].split(' ')
    inputsList.push(inputs)
}


let result = []

for(let i = 0 ; i < n ; i++){
    
    let prefix_sum = []
    
    let temp = 0
    
    for(k of string){
        if (inputsList[i][0] == k){
            temp+=1
            prefix_sum.push(temp)

        }
        else{
            prefix_sum.push(temp)

        }
    }

    if (Number(inputsList[i][1]) == 0 ){
        result.push(prefix_sum[Number(inputsList[i][2])] - prefix_sum[Number(inputsList[i][1])])
    }
    else {
        result.push(prefix_sum[Number(inputsList[i][2])] - prefix_sum[Number(inputsList[i][1])-1])
    }
}

c(result.join('\n'))