i = int(input())

for a in range(i) :
    for j in range(i-1,a,-1) :
        print(' ',end='')
    for k in range(0,a+1,1) :
        print('*',end='')
    print('',end='\n')