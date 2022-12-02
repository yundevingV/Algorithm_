import sys

n = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))

s = sorted(lst)

dict = {}

a=0

for i in s :
    
    if(dict.get(i) == None) :
        dict[i] = a
        a+=1
    
for i in lst :
    print(dict[i],end=' ')