function solution(begin, target, words) {
    var answer = 0;
    
    if(!words.includes(target)) {
        return 0;
    }
    
    let visited = new Array(words.length).fill(0);   
    
    let queue = [[begin,0]];
    
    while(queue.length > 0) {
        let [currentWord,changeCount] = queue.shift();
        if(currentWord === target) {
            return changeCount;
        }
        
        words.forEach((word,index) => {
            let diff = 0;
            
            if(!visited[index]) {
                for(let i=0;i<currentWord.length;i++){
                    if(currentWord[i] !== word[i]) {
                        diff++;
                    }
                    
                }
            }
            if(diff === 1){
                queue.push([word,changeCount+1]);
                visited[index]= 1;
            }
        })
    }
    return 0;
}