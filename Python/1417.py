import sys

num = int(sys.stdin.readline())
lst=[]
cnt =0
for i in range(num) :
    a = int(sys.stdin.readline())
    lst.append(a)
d=lst[0]
del lst[0]
while True :
    
    if len(lst) == 0 :
        print(cnt)
        break
    elif d <= max(lst)  :
        lst.insert(lst.index(max(lst)),lst[(lst.index(max(lst)))] - 1) 
        lst.remove(max(lst))     
        d +=1 
        cnt+=1
    elif d > max(lst) :
        print(cnt)
        break
