import sys

num = int(sys.stdin.readline())
lst =[]
s=[]
r=1
rs=[]
for _ in range(num) :
    a = int(sys.stdin.readline())
    while r <= a :
        s.append(r)
        rs.append('+')
        r+=1
    if s[-1] == a :
        s.pop()
        rs.append('-')
    else :
        rs.append('NO')

if 'NO' in rs :
    rs.clear()
    print('NO')
else :
    for i in rs :
        print(i)



