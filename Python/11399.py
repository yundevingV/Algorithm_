times=[]

line = int(input(""))

times=map(int, input().split())
times = list(times)
times.sort()

sum=0
for i in range(line) :
    for j in range(i+1) :
        sum+=times[j]
     
print(sum)