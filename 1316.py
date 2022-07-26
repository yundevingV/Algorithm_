import sys
num = int(sys.stdin.readline())
count = 0
result=0
count = num

for i in range(num) :
    str = input()
    for j in range(len(str)-1) : 
        if str[j] != str[j+1] :
            if str[j] in str[j+1:] :
                count -=1
                break

print(count)

