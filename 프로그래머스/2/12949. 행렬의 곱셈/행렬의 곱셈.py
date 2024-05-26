def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)): 
        row = []
        for j in range(len(arr2[0])): 
            value = 0
            for k in range(len(arr2)): 
                value += arr1[i][k] * arr2[k][j]
            row.append(value)
        answer.append(row)
    return answer