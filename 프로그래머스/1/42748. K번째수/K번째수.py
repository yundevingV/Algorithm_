def solution(array, commands):
    answer = []
    for i in range(len(commands)) :
        
        s = commands[i][0]
        e = commands[i][1]
        p = commands[i][2]
        sliced_array = array[s-1:e]
        sliced_array.sort();
        pick_array = sliced_array[p-1]
        answer.append(pick_array);
        
    return answer