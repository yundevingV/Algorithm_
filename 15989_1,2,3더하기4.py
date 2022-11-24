import sys

n = int(sys.stdin.readline())

#10개의 결과값
#1 2 3 4 5 7 8 10 12 14

#1로 시작   1 1 1 1 1 1 1 1  1  1
d = [1] * 10001

# #2로 시작   0 1 1 2 2 3 3 4  4  5
for i in range(2,10001):
    d[i] += d[i - 2]
    
#3으로 시작 0 0 1 1 2 3 4 5  7  8    
for i in range(3,10001):
    d[i] += d[i - 3]

#total     1 2 3 4 5 7 8 10 12 14

for i in range(n) :
    m = int(sys.stdin.readline())
    print(d[m])
