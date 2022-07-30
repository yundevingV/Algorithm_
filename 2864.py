n,m = input().split()

n1 = int(n.replace('5','6'))
n11 = int(n.replace('6','5'))

n2 = int(m.replace('5','6'))
n21 = int(m.replace('6','5'))

sum1 = n1+n2 
sum2 = n11+n21 

print(sum2,sum1)


