n = int(input(''))
count =0

while(n!=1) :
    if (n-1) // 3 > (n//2//2):
        n=n//2
        count+=1
        print(n)
    elif (n-1) // 3 < (n//2//2) :
        n=n-1
        count+=1
        print(n)
    elif n%3==0:
        n=n//3
        count+=1
        print(n)
    elif n%2 == 0 :
        n=n//2
        count+=1
        print(n)

    
        
print(count)

    
