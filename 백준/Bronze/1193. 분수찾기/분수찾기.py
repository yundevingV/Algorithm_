import sys

n = int(sys.stdin.readline())
num =0
c=0
while n > num :
    c+=1
    num +=c

if c % 2 == 0 :
    print(c-(num-n),end='')
    print('/',end='')
    print(num-n+1)
else :
    print(num-n+1,end='')
    print('/',end='')
    print(c-(num-n))

