import sys

n = int(sys.stdin.readline())
c=0
r=0

num_list = list(map(int, input().split()))
for j in num_list :
    c=0
    if j ==1 :
        pass
    else :
        for k in range(2,j+1,1) :
            
            if j % k == 0:
                c+=1

        if c == 1 :
            r +=1
        else :
            r +=0

print(r)


