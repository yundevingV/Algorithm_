function solution(ingredient) {
    var answer = 0;
    let lst = [];
    
    ingredient.forEach(x => {
       lst.push(x);
        if(lst.slice(-4).join('') === '1231'){
            lst.splice(-4);
            answer+=1
        }
    });
    
    return answer;
}