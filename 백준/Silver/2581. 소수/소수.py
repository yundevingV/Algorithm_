import sys

n1 = int(sys.stdin.readline())
n2 = int(sys.stdin.readline())

lst = []

for i in range(n1,n2+1) :
    c=0
    if i == 2 :
        lst.append(i)
    elif i == 1 :
        pass
    else :
        for j in range(2,i) :
            if i % j == 0 :
                c+=1
        
        if c == 0 :
            lst.append(i)
        else : 
            pass
if len(lst) == 0 :
    print('-1')
else :
    print(int(sum(lst)),end='\n')
    print(int(min(lst)))