let c = console.log

let lst = [1,11,22,33,44,55]

for(let i = 0 ; i < 10 ; i++){
    c(i,end='')
}

for(i in lst){
    c(typeof(i))
    c(lst[(i)])
}

for(i of lst){
    c(i)
}