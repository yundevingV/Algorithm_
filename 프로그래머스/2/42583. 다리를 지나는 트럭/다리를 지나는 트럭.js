function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    let bridge = new Array(bridge_length).fill(0)
    while (bridge.length){

        bridge.shift()
        if(truck_weights.length){
            const sum = bridge.reduce((acc, currentValue) => acc + currentValue, 0);
        
            if(sum + truck_weights[0] <= weight){
                bridge.push(truck_weights.shift())
            }
            else {
                bridge.push(0)
            }
        }
        answer += 1
    }
        
    return answer;
}