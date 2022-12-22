import sys

n = int(sys.stdin.readline())
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

while True :
    n= int(n)
    if is_prime_number(n):
        n = str(n)
        l = len(n)//2
        if n[0:l] == n[-1:-(l+1):-1] :
                print(n)   
                break 
        else :
            print(n)
            n= int(n)
            n+=1
    else :
        n= int(n)
        n+=1




# 시작 끝 규칙