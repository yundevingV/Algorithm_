function solution(n, times) {
    var answer = 0;
    
    // low = left , high = right
    let low = 1;
    let high = Math.max(...times) * n;
    
    while(low <= high){
        let mid = Math.floor((low + high) / 2);
        
        const people = times.reduce((acc,time) => acc + Math.floor(mid / time) , 0)
        if (people < n){
            low = mid + 1;
        } else {
            high = mid -1;
        }
        
    }

    return low;
}