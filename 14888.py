import sys

a = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
sum=num[0]
p,m,mul,d = map(int, sys.stdin.readline().split())

end= p + m + mul + d
result_min = 1e9
result_max = -1e9

def aa(sum,c,p,m,mul,d) :
    global result_min , result_max, end

    
    if end +1 ==  c  :

        result_max = max(result_max,sum)
        result_min = min(result_min,sum)

        return  
    if p > 0 :
        aa(sum + num[c],c+1,p-1,m,mul,d)
    if m > 0 :
        aa(sum - num[c],c+1,p,m-1,mul,d)
    if mul > 0 :
        aa(sum * num[c],c+1,p,m,mul-1,d)
    if d > 0 :
        aa(int(sum / num[c]),c+1,p,m,mul,d-1)




aa(sum,1,p,m,mul,d)

print(result_max)
print(result_min)

