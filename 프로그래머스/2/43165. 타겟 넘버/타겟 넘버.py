answer = 0

def dfs (numbers,num,index,target) :
    global answer
    if index == len(numbers) :
        if num == target :
            answer += 1
        else :
            return 0 
    else : 
        dfs(numbers, num + numbers[index], index+1,target)
        dfs(numbers, num - numbers[index], index+1,target)
    
def solution(numbers, target):
    global answer
    dfs(numbers,0,0,target)
    
    return answer