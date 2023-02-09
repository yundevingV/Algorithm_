import sys

n = int(sys.stdin.readline())

i = 2

while True :
    if n % i != 0 :
        i+=1
        if n < i :
            break
    else :
        n //=i 
        print(i)
    