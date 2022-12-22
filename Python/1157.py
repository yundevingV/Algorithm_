import sys

str = input()
dict ={}

str=str.lower()

for i in str :
    dict[i] = dict.get(i,0) +1

maxKey = max(dict,key=dict.get)

a = list(dict.values())
while True :
    a.sort()
    if len(a) > 1 :
        f = a.pop()
        s = a.pop()
        if f == s :
            print('?')
            break
        else :
            print(maxKey.upper())
            break
    else :
            print(maxKey.upper())
            break


