from squaremult import squareNMul
import random
import os
import math
import threading

def fermatPrimeTest(p: int):
    count = 0
    for a in range(p-2,2, -1):
        if math.gcd(a,p) == 1:
            temp = squareNMul(a,p-1,p)
            if temp==1:
                count += 1
            else: 
                print('not '+str(p))
                return 0
        
    return count

def prime(n):
    for i in range(2,n):
        if n%1 == 0:
            return True
    return False

def Threader(p,lock):
    primeTes = prime(p)
    if primeTes == False: return
    if len(temp) == 3:
        return

    count = fermatPrimeTest(p)
    if count >> 0:
        if count != p-4:
            lock.acquire()
            temp.append(p)
            lock.release()

if os.name == "nt":
    os.system('cls')
else: os.system('clear')
print("-------------------------------------------\nWelcome to Fermat Primality Test Program: ")
while(1):
    temp = []
    test = input("Enter the less than number: ")
    test = int(test)

    lock = threading.Lock()
    threads = []

    for p in range(test, 1, -1):
        t = threading.Thread(target=Threader, args=[p, lock])
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    print('Carmichael Numbers: ')
    print(temp)

# print("Type 'exit' at any prompt to end: ")
# while(1):

    # p = input('-------------------------------------------\nChoose a prime canidate p: ')
    # s = input('Choose a security paramter s: ')

    # if p == 'exit': 
    #     break

    # p = int(p)
    # # s = int(s)

    # verdict = fermatPrimeTest(p)
    # if verdict >> 0: 
    #     print(str(p) + ' is likely prime: ')
    #     if verdict == p-3: print(str(p) + ' is prime: ')
    #     else: print(str(p) + ' is a carmichael number: ')
    # else: print(str(p) + ' is composite: ')
    