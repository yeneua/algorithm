N = int(input())
numbers = list(map(int, input().split()))

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

count = 0

for i in range(N):
    if numbers[i] == 1: continue
    if is_prime(numbers[i]):
        count += 1

print(count)
