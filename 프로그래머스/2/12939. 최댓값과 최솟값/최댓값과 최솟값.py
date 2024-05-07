def solution(s):
    answer = '';
    data_r = list(map(int, s.split()));
    result = str(min(data_r)) + ' ' + str(max(data_r));
    
    return result