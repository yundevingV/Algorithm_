def solution(n, words):
    answer = [0, 0]
    prev_word = words[0]
    duplication = [prev_word]
    
    for i in range(1, len(words)):
        present_word = words[i]
        if (prev_word[-1] == present_word[0]) and (present_word not in duplication):
            duplication.append(present_word)
            prev_word = present_word
        else:
            answer[0] = (i % n) + 1
            answer[1] = (i // n) + 1
            break

    return answer
