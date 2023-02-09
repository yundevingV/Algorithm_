
def d(x) :
    if x < 10 :
        return x + (x%10)
        
    elif 10 <= x < 100 :
        return x+ (x%10) + (x//10)
        
    elif 100<= x <1000 :
        return x+ (x//100) + (x//10%10) + (x%10) 
        
    elif 1000<= x < 10000 :
        return x + (x%10) + (x//10%10) + (x//10//10%10) +(x//10//10//10)


lst=[0]*10001

for i in range(10001) :
    lst[i] = i
lst.sort()
lst = set(lst)

r =set()

for j in range(10001) :
    r.add(d(j))


for i in lst :
    if i not in r :
        print(i)
