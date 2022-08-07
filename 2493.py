import sys

num = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
r=[0] *num
# 결과 나타내는 리스트
s=[]
# 비교하는 리스트 stack
si=[]
i = num-1
s.append(lst[i])
si.append(i)

while i >0 :  
    while s :
        if s[-1] > lst[i-1] : 
            break      
        else :
            r[si[-1]] = i
            si.pop()
            s.pop()
    i-=1
    s.append(lst[i])
    si.append(i)
    


print(r)