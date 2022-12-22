import sys

x = int(sys.stdin.readline())

d = [0] * (x+1)

for i in range(2,x+1) :
    #현재 수에서 1 뺄때
    d[i] = d[i-1] + 1

    #2로 나눠떨어질때
    if i % 2 == 0 :
        d[i] = min(d[i // 2] + 1, d[i])

    #3으로 나눠떨어질때
    if i % 3 == 0 :
        d[i] = min(d[i // 3]+ 1, d[i])

print(d[x])
