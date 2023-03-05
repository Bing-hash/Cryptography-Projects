def order(a:int, n:int):
    count = 0
    while 1:
        b = a*a**count
        b = b%n
        count +=1
        if(b==1 or count>n):
            break
    return count

n=""
while 1:
    n = input("Enter a value for n: ")
    if(n=="exit"):
        exit()
    for a in range(int(n)-1):
        ind = int(a)+1
        ord = order(ind, int(n))
        if(ord == int(n)-1):
            print("ord("+str(ind)+") = "+str(ord)+"*")
        elif(ord > int(n)):
            print("ord("+str(ind)+") = infinite")
        else: print("ord("+str(ind)+") = "+str(ord))
                    
        