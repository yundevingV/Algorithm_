def DFS(numbers, current_sum, index, target):
    if index == len(numbers):
        return 1 if current_sum == target else 0
    else:
        return DFS(numbers, current_sum + numbers[index], index + 1, target) + DFS(numbers, current_sum - numbers[index], index + 1, target)

def solution(numbers, target):
    return DFS(numbers, 0, 0, target)
