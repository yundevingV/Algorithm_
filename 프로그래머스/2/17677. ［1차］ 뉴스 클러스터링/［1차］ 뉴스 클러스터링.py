from collections import Counter

def solution(str1, str2):
    answer = 0
    
    # 소문자로 변환
    str1 = str1.lower();
    str2 = str2.lower();
    
    # 문자열 분리하기 위한 배열
    str1_list = [];
    str2_list = [];
    
    # 반복문으로 문자인지 확인 후 문자면 추가하기
    for i in range(len(str1)-1) :
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_list.append(str1[i] + str1[i+1]);
    for i in range(len(str2)-1) :
        if str2[i].isalpha() and str2[i+1].isalpha():
                str2_list.append(str2[i] + str2[i+1]);   
                
    # 다중집합을 세기 위해 Counter
    counter1 = Counter(str1_list);
    counter2 = Counter(str2_list);
    
    a = list((counter1 & counter2).elements());
    b = list((counter1 | counter2).elements());
    
    print(a,b)
    if len(a) == 0 and len(b) == 0 :
        return 65536;
    return int(len(a) / len(b) * 65536)