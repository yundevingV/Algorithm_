answer = 0
found = False

def solution(word):
    global answer, found
    answer = 0
    found = False
    
    alpha = ['A','E','I','O','U']
    
    def dfs(current_word):
        global answer, found
        if len(current_word) > 5:
            return
        if current_word == word:
            found = True
            return
        answer += 1
        for i in alpha:
            if not found:
                dfs(current_word + i)
    
    dfs('')
    return answer