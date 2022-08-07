import sys

num = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
s=[]
# 스택
sr=[]
r = [-1] *num
#결과값
i = 0
s.append(lst[i])
sr.append(i)
# s는 리스트의 값을 저장해주는 스택
# sr 은 인덱스 번호를 저장하는 스택
# sr[-1] 과 pop를 이용해서 결과값 index를 찾아갈 수 있도록 해줌.

while i < len(lst)-1  :
    while s :
        if lst[i+1] <= s[-1] :
            break
        else :
            r[sr[-1]] = lst[i+1]
            s.pop()
            sr.pop()
            
    i+=1
    s.append(lst[i])
    sr.append(i)


for i in r :
    print(i,end=' ')
