import os

def squareNMul(x: int, h: int, n: int):
    temp = h.bit_length()-1
    num = 1

    # Checks every bit position of H to see if it is equal to 1 by using bitwise and
    # H = ht, ht-1, ... h2, h1, h0
    # For example:  (39)10 = (100111)2
    #               100111
    #             & 100000 (= 32 = 2^5)
    #               100000 = 32
    #                        32 // 32 = 1, so there is a 1 in ht (or h5, t=5)
    #               
    #               100111
    #             &  10000 (= 16 = 2^4)
    #                00000 = 0
    #                        0 // 16 = 0, so there is a 0 in ht-1 (or h4, t=5)
    for i in range(temp, -1, -1):
        hi = (h&(2**i))//2**i
        num = (num**2)%n
        if hi == 1:
            num = (num*x)%n
    return num
        


if os.name == "nt":
    os.system('cls')
else: os.system('clear')

print("-------------------------------------------\nWelcome to Square-and-Multiply Program: ")
print("Type 'exit' at any prompt to end: ")
while(1):
    print("-------------------------------------------\nEnter in the format: x^H mod n: ")
    x = input("-------------------------------------------\nEnter x value: ")
    if(x=="exit"): break
    h = input("Enter H value: ")
    if(h=="exit"): break
    n = input("Enter n value: ")
    if(n=="exit"): break

    x = int(x)
    h = int(h)
    n = int(n)
    
    ans = squareNMul(x,h,n)
    print("\nAnswer is " + str(ans) + " mod " + str(n) + ": ")
    
    