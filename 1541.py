a = input().split('-')

sum = 0

for i in a :
    if a.index(i)==0 :
        
        s = i.split('+')
    for j in s :
        sum-=int(j)

# (15+14+5+8+7)  (15+7)  (14+7)
#    s=[15,14]   j 첫번째 -29
#    s=[15,7] j 2 = -51
#    s=[14,7] j 3 = -72

str = a[0] #   str='15+14'
strnew = str.split('+') # strnew=[15,14]
for n in strnew :
    sum += int(n) *2

print(sum)    