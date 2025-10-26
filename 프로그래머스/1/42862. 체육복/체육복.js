function solution(n, lost, reserve) {
    var answer = 0;
    
    lost.sort((a, b) => a - b);
    reserve.sort((a, b) => a - b);
    
    let newLost = lost.filter(item => !reserve.includes(item));
    let newResrve = reserve.filter(item => !lost.includes(item));
    
    for(let i=0;i<newResrve.length;i++) {
       
        if(newLost.includes(newResrve[i] - 1)) {
            newLost = newLost.filter(item => item !== newResrve[i] - 1);
            continue;                                  
        }
        else if(newLost.includes(newResrve[i] + 1)) {
            newLost = newLost.filter(item => item !== newResrve[i] + 1);
            continue;
        }
       
    }
    
    return n - newLost.length;
}
    