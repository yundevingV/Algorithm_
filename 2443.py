i = int(input())

for a in range(i) :
    for k in range(0,a,1) :
        print(' ',end='')
    for j in range((2*i)-1,2*a,-1) :
        print('*',end='')

    print('',end="\n")  