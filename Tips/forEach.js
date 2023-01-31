let c = console.log

let list = ['Mount' , 'Silva' , 'Gallagher' , 'Kepa' , 'Harvertz']

list.forEach((value) => {
    c(value)
})

list.forEach((value,index) => {
    c(`index : ${index} , value : ${value}`)
})

list.forEach((value,index,array) => {
    c(`index : ${index} , value : ${value} , array[${index}] : ${array[index]}`)
})