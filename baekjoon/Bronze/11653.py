import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num))):
        if i > 3 and i % 2 == 0:
            continue            
        if num % i == 0:
            return False
    else:
        return True

N = int(input())
i = 2

while N > 1:
    if N % i == 0:
        if isPrime(i):
            print(i)
            N //= i
    else:
        i += 1