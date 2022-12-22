import sys

num = int(sys.stdin.readline())
for i in range(num) :
    lst =[]

    str = input()
    for j in str :
        if j == '(' :
            lst.append(j)
        elif j == ')' :
            if len(lst) > 0:
                if '(' in lst :
                    lst.pop()
            else :
                lst.append(j)

    if len(lst) == 0 :
        print('YES')
    else :
        print('NO')

                
