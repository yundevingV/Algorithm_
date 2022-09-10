import sys

n = int(sys.stdin.readline())

dict = {}

for _ in range(n) :
    s = sys.stdin.readline().split('.')
    s[1] = s[1].rstrip()
    if s[1] not in dict :
        dict[s[1]] = 1 
    else :
        dict[s[1]] += 1 

sort_dict = sorted(dict.keys())

for i in range(len(dict)) :
    print(sort_dict[i],end=' ')
    print(dict[sort_dict[i]])