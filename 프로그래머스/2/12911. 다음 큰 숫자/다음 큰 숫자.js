function solution(n) {
    var answer = 0;
    
    let count1 = 0

    nx = n.toString(2)
    for(let j=0;j<nx.length;j++){
        if(nx[j] == 1) {
            count1 +=1
        }
    }
    
    for(let i=n+1; i < 1000000; i++){
        let count2 = 0
        bin = i.toString(2)

        for(let j=0;j<bin.length;j++){
            if(bin[j] == 1){
                count2 +=1
            }
        }
        if(count1 == count2){
            answer = i
            break
        }
    }
    return answer;
}