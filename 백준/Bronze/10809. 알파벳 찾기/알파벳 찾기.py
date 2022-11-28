import sys

a = input()

compareStr = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(compareStr)) :
    if compareStr[i] in a :
        indexNum = a.find(compareStr[i])
        print(indexNum,end=' ')
    else :
        print(-1,end=' ')

