# Python Program - Nathan Dallmann
def func1(a:int,b:int):
    q = a//b
    r = a%b
    return q,r

def func2(ox:int,oy:int,q:int):
    x = oy
    y = ox-oy*q
    return x,y

def leftside(a: int,b: int,qs):
    while True:
        q,r = func1(a,b)
        qs.append(q)
        a=b
        b=r
        if(b==0):
            break
    return a,b,qs

def rightside(x:int,y:int,qs:list):
        while True:
            x,y = func2(x,y,qs[len(qs)-1])
            qs.pop()
            if(len(qs)==0):
                break
        return x,y

def EEA(a,b):
    x,y,qs = leftside(a,b,[])
    if(x==1):
        x,y = rightside(x,y,qs)
        return x,y
    else: 
        print("The inverse for this set of 'a' and 'b' does not exist: ")
        exit()
    
print("Welcome to the EEA python tool: ")
print("For a mod b: ")
a = input("Select an 'a' value: ")
b = input("Select an 'b' value: ")

a = int(a)
b = int(b)

x,y = EEA(a,b)
ai = x%b
bi = y%a

if(ai<=0 and bi<=0):
    print("The multiplicative inverse of these two numbers is negative: ")
elif(ai<=0):
    print("Multiplicative inverse of 'b' = "+str(bi))
elif(bi<=0):
    print("Multiplicative inverse of 'a' = "+str(ai))
print("Multiplicative inverse of 'a' = "+str(ai)+": \nMultiplicative inverse of 'b' is = "+str(bi)+": ")