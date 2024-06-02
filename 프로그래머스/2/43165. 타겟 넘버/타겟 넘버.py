answer = 0;
def DFS(numbers, current_sum, index, target):
    global answer;
    if index == len(numbers):
        if current_sum == target : 
            answer +=1;
        else :
            return 0;
    
    else:
        DFS(numbers,current_sum + numbers[index], index + 1, target);
        DFS(numbers,current_sum - numbers[index], index + 1, target);
        

def solution(numbers, target):
    global answer;
    DFS(numbers, 0, 0, target);
    return answer;