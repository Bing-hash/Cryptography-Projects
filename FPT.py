from squaremult import squareNMul
import random
import os

def fermatPrimeTest(p: int, s: int):
    count = 0
    for i in range(s):
        a = random.randint(2,p-2)
        temp = squareNMul(a,p-1,p)
        if temp!=1:
            return count
        count += 1
    return True

if os.name == "nt":
    os.system('cls')
else: os.system('clear')
print("-------------------------------------------\nWelcome to Fermat Primality Test Program: ")
print("Type 'exit' at any prompt to end: ")
while(1):

    p = input('-------------------------------------------\nChoose a prime canidate p: ')
    s = input('Choose a security paramter s: ')

    if p == 'exit' or s == 'exit':
        break

    p = int(p)
    s = int(s)

    verdict = fermatPrimeTest(p,s)
    if verdict == True: print(str(p) + ' is likely prime: ')
    else: print(str(p) + ' is composite: ' + str(verdict))