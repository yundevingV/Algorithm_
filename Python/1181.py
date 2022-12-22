import sys
lst=[]

num = int(sys.stdin.readline())

for i in range(num) :
    a = input()
    lst.append(a)

lst = set(lst)
# 중복제거

lst = list(lst)
# 다시 리스트

lst.sort()
# 알파벳 화
lst.sort(key = len)
# 길이 순으로 함

for i in lst :
    print(i)