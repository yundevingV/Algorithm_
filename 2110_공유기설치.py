import sys

n,c = map(int, sys.stdin.readline().split())

#n은 집의개수 , c는 공유기의 개수
lst = []
for _ in range(n) :
    o = int(sys.stdin.readline())
    lst.append(o)

#여기까쥘 입력
lst.sort()

start = min(lst)
end = max(lst)-min(lst)
#왼쪽과 오른쪽을 나눠 start , end로 변수 지정.
#특이점은 end에서 집이 0에 없고 1이나 2부터 있을 수 있으니 -min(lst)를 해줌.

result = []
#결과 담을 배열

while start <= end :
    mid =(start + end) // 2
    #mid 값을 구함. 이 값이 곧 공유기의 설치 거리가 될거임
    cnt=1
    pre = lst[0]

    for i in lst :
        if mid + pre <= i :
            pre=i
            cnt+=1

    if c > cnt :
            end = mid - 1
            
    else :
            start = mid + 1
            result.append(mid) 

print(max(result))


#c >= cnt 공유기가 부족한 경우 혹은 갯수가 딱 맞는 순간
#이 경우에 mid 값을 감소 시키면서 공유기를 세워둠
#mid는 공유기 간의 거리임.

#c < cnt 공유기가 과다한 상황
