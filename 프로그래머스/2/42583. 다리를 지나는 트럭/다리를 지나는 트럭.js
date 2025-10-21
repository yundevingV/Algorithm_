function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    
    // 다리
    let queue = new Array(bridge_length).fill(0);
    
    // 다리 무게
    let bridge_weight = 0;
    
    while(queue.length) {
        let q = queue.shift();
        bridge_weight -= q;
        let pop = truck_weights[0];
        
        if(truck_weights.length) {
            // 다리 최대 무게보다 가벼우면
            if(bridge_weight + pop <= weight) {
                let truck = truck_weights.shift();
                queue.push(truck);
                bridge_weight += pop;
            }
            // 다리 최대 무게보다 무거우면
            else {
                queue.push(0);
            }
        }
        answer += 1;
    }
    return answer;
}