from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    # 대기중인 트럭
    truck_weights = deque(truck_weights)
    # 다리
    b = [0 for _ in range(bridge_length)]
    b = deque(b)

    current_weight = 0 
    
    while truck_weights :
        time += 1
        current_weight -= b.popleft()
        if current_weight + truck_weights[0] <= weight :
            current_weight += truck_weights[0]
            b.append(truck_weights.popleft())
        else :
            b.append(0)
    time += bridge_length
    return time