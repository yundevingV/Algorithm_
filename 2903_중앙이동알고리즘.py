import sys

n = int(sys.stdin.readline())

initialNum = 2
for i in range(n) :
    initialNum +=initialNum
    initialNum -=1


print(initialNum * initialNum)
