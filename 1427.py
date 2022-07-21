import sys

num = input()
list=[]

for i in num :
    list.append(i)

list.sort(reverse=True)

for i in list :
    print(i,end='')

