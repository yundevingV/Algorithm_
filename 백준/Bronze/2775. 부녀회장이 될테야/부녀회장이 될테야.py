import sys

t = int(sys.stdin.readline())






for _ in range(t) :
    #층
    k = int(sys.stdin.readline())

    #호수
    n = int(sys.stdin.readline())

    #0층 호수 별 사람 수
    v = [0] * (n)

    for i in range(n) :
        v[i] = i+1

    #1층을 올라가는 포문.
    for _ in range(k) :
        for j in range(1,n) :
            v[j] += v[j-1]
            
            

    print(v[-1])