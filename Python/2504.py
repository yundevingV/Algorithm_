import sys

str = input()
ac=0
c=1
s=[]
r=[]
final =0
for i in str :
    if i == '(' :
        s.append('(')
        c= c*2
    elif i == '[' :
        s.append('[')
        c= c*3
    elif i == ')' :
        if not s :
            ac=99
            break
        elif s[-1] == '[' :
            ac=99
            break
        else :
            a=s.pop()
            final +=c
            c=c//2
    elif i == ']' :
        if not s :
            ac=99
            break
        elif s[-1] == '(' :
            ac=99
            break
        else :
            a=s.pop()
            final +=c
            c=c//3


if ac==99 :
    print('0')
else :
    print(final)

