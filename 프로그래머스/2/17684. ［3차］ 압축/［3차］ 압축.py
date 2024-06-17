import string
def solution(msg):
    answer = [];

    alpha_dict = {char: index + 1 for index, char in enumerate(string.ascii_uppercase)}
    print(alpha_dict)
    index = 26;
    
    while msg :
        wc = ""
        for i in range(len(msg)) :
            wc = wc + msg[i];
            if wc not in alpha_dict :
                # 사전에 새로운 단어 추가
                index += 1;
                alpha_dict[wc] = index;
                
                # answer에 추가하기
                wc = wc[:-1]
                answer.append(alpha_dict[wc]);
                break;
        msg = msg[len(wc):]
        if not msg :
            answer.append(alpha_dict[wc])
    return answer