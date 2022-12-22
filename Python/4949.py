import sys

def s(str) :
    lst = []
    r='yes'
    for i in str :

        if i == '[' :
            lst.append('[')
            r='no'
        elif i == '(' :
            lst.append('(')
            r='no'
        elif i == ']' :
            if len(lst) >0 and lst[-1] == '['  :
                lst.pop()
                if len(lst) == 0 :
                    r='yes'
                else :
                    r='no'
            else :
                r='no'
                break
        elif i == ')'  :
            if len(lst) > 0 and lst[-1] == '(':
                lst.pop()  
                if len(lst) == 0 :
                    r='yes'
                else :
                    r='no'
            else :
                r='no'
                break

    print(r)

while True :
    str = sys.stdin.readline().rstrip()
    if str == '.' :
        break
    else :
        s(str)
