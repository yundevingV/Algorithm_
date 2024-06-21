def solution(dirs):
    answer = set();
    dict = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
    x = 0;
    y = 0;
    
    for i in dirs :
        dx,dy = dict[i];
        nx = x + dx;
        ny = y + dy;
        if -5 <= nx <= 5 and -5 <= ny <= 5 :
            answer.add(((x,y),(nx,ny)));
            answer.add(((nx,ny),(x,y)));
            x = nx;
            y = ny;
    return len(answer) // 2