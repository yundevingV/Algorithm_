let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log

n = Number(input[0])

if (200 <= n && n <= 205) {
    c(1)
}
else if (206 <= n && n <= 217){
    c(2)
}
else if (218 <= n && n <= 228){
    c(3)
}
else {
    c(4)
}

