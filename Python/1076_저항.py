import sys
result =0
def fs1(a) :
    global result
    if a == 'black' : 
        result +=0
    elif a == 'brown' :
        result +=10
    elif a == 'red' :
        result +=20
    elif a == 'orange' :
        result +=30
    elif a == 'yellow' :
        result +=40
    elif a == 'green' :
        result +=50
    elif a == 'blue' :
        result +=60
    elif a == 'violet' :
        result +=70
    elif a == 'grey' :
        result +=80
    elif a == 'white' :
        result +=90

def fs2(a) :
    global result
    if a == 'black' : 
        result +=0
    elif a == 'brown' :
        result +=1
    elif a == 'red' :
        result +=2
    elif a == 'orange' :
        result +=3
    elif a == 'yellow' :
        result +=4
    elif a == 'green' :
        result +=5
    elif a == 'blue' :
        result +=6
    elif a == 'violet' :
        result +=7
    elif a == 'grey' :
        result +=8
    elif a == 'white' :
        result +=9

def f(a) :
    global result
    if a == 'black' : 
        result *=1
    elif a == 'brown' :
        result *=10
    elif a == 'red' :
        result *=100
    elif a == 'orange' :
        result *=1000
    elif a == 'yellow' :
        result *=10000
    elif a == 'green' :
        result *=100000
    elif a == 'blue' :
        result *=1000000
    elif a == 'violet' :
        result *=10000000
    elif a == 'grey' :
        result *=100000000
    elif a == 'white' :
        result *=1000000000

a1 = input()
a2 = input()
a3 = input()


fs1(a1)
fs2(a2)
f(a3)

print(result)