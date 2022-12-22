

str = input()

s1 = []
s2 = []

i = 0
check = 1
for i in str :
    if i == '<' :
        while len(s2) >0 :
            s1.append(s2.pop())
        s1.append(i)
        check = 0 
    
    elif i == '>' :
        s1.append(i)
        check = 1
    
    if i != '<' and i !='>' and check == 0 :
        s1.append(i)
    elif i != '<' and i !='>' and check == 1 :
        if i ==' ' : 
            while len(s2) >0 :
                s1.append(s2.pop())
            s1.append(i)
        else :    
            s2.append(i)    

while len(s2) >0 :
    s1.append(s2.pop())

for i in s1 :
    print(i,end='')
