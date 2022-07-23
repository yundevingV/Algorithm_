import sys

num = int(sys.stdin.readline())
result =[]

sum =0
avg = 0
count =0
for i in range(num) :
    num_list = list(map(int, input().split()))
    for i in range(1,len(num_list),1) :
        sum +=num_list[i]
    avg = sum / num_list[0]
    for i in range(1,len(num_list),1) :
        if avg >= num_list[i] :
            count +=1


