let c = console.log

// let chelseaMember=['리스제임스','하베르츠','포터','케파','마운트']

// const length = chelseaMember.filter(item => item.length > 2)

// c(length)

const chelseaMembers = [
    { name : '리스제임스' , team : 'Chelsea'},
    { name : '하베르츠' , team : 'Chelsea'},
    { name : '조르지뉴' , team : 'Aresnal'},
    { name : '케파' , team : 'Chelsea'},
    { name : '호날두' , team : '알니사르'},

]

const isChelsea = chelseaMembers.filter(item => item.team === 'Chelsea')
                                .map(item => item.name)

c(isChelsea)
