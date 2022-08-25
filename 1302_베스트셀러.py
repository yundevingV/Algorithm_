from re import L
import sys

n = int(sys.stdin.readline())
dic = {}
for i in range(n) :
    a = input()
    if a not in dic :
        dic[a] = 1 
    else :
        dic[a] +=1

maxnum = max(dic.values())

lst = []

for i in dic :
    if maxnum == dic[i] :
        lst.append(i)

lst.sort()

print(lst[0])


