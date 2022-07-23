import sys

n = int(sys.stdin.readline())

num_list = list(map(int, input().split()))

s = int(sys.stdin.readline())

card_list = list(map(int, input().split()))

dict ={}

for i in num_list :
    if i in dict :
        dict[i] +=1
    else :
        dict[i] = 1

for j in card_list :
    if j in dict :
        print(dict[j],end=" ")
    else :
        print(0,end=" ")

