import sys

num = int(sys.stdin.readline())
lst = []
count = 0
result=0
for i in range(num) :
    str = input()
    lst =[]
    num = len(str)
    for j in str : 
        lst =list(lst)
        lst.append(j)
        lst=set(lst)
        str = str.replace(j,'')
        for k in lst :
            if len(str) > 0 :
                if str[0] == k :
                    count +=1
                    print(count)
                else :
                    count +=0
                    print('012')
    if count >=1  :
        result+=0
    elif count == 0 or num == len(lst) : 
        result+=1
    

print(result)





