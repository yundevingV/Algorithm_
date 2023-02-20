let fs = require('fs');
const filePath = process.platform === "linux" ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().trim().split('\n');
const c = console.log

n = Number(input[0])

let array = [];

//입력값 받기
for (let i = 1; i < input.length; i++) {
    if (input[i] !== '') {
        array.push(input[i].split(' '));
    }
}

for (let i = 0 ; i<array.length ; i++){
    if (array[i].length == 2 ) {
        array[i][1] = array[i][1].replace(/\r/,"")
    } 
    else if (array[i].length == 1) {
        array[i][0] = array[i][0].replace(/\r/,"")
    }
}

let lst = [] 
let dict = {}
let resultOutput = []
let count = 0

for (let i=0 ; i < array.length ; i++ ){
    
    let result = 1
    

    if (array[i].length == 2 ) {
        lst.push(array[i][1])
    } 
    else if (array[i].length == 1) {
        count = Number(array[i][0])
    }
    
    if (count == lst.length) {

        for (let v of lst) {
            dict[v] = dict[v] ? dict[v] + 1 : 1
        }

        for (let k in dict) {
            result = result * (dict[k]+1)
        }
        lst = []
        dict={}
        resultOutput.push(result-1)
    }

}

for (let i = 0 ; i < n ; i++){
    c(resultOutput[i])
}