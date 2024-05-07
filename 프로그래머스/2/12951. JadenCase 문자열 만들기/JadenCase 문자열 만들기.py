def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        # 첫글자만 대문자로 만들어주는 내장함수
        s[i]=s[i].capitalize();
    answer=' '.join(s)
    return answer
