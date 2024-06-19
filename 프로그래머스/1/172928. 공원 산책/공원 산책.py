# 한칸씩 탐색하다가 이동가능한 피봇 여부
def solution(park, routes):
    answer = []
    x, y = 0, 0
    
    # 시작 지점 저장하기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x, y = i, j

    # 이동하기
    for route in routes: 
        # 방향, 이동 횟수
        direction, moveNumber = route.split(' ')
        moveNumber = int(moveNumber)
        
        
        dx = x;
        dy = y;
        canMove = True;

        for _ in range(moveNumber):
            
            # 이동가능여부
            
            if direction == 'E':
                if dy < len(park[0]) - 1 and park[dx][dy + 1] != 'X':
                    dy += 1
                else :
                    canMove = False
                    break
            elif direction == 'W':
                if dy > 0 and park[dx][dy - 1] != 'X':
                    dy -= 1          
                else :
                    canMove = False
                    break
            elif direction == 'N':
                if dx > 0 and park[dx - 1][dy] != 'X':
                    dx -= 1
                else :
                    canMove = False
                    break
            elif direction == 'S':
                if dx < len(park) - 1 and park[dx + 1][dy] != 'X':
                    dx += 1
                else :
                    canMove = False
                    break
        if canMove :
            x = dx;
            y = dy;


    answer.append(x)
    answer.append(y)
    return answer