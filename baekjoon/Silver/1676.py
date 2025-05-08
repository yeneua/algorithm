N = int(input())

factorial = 1
count = 0

for i in range(1, N+1):
    factorial *= i
    
factorial = str(factorial)

for i in range(len(factorial)-1,-1,-1):
    if factorial[i] == '0':
        count += 1
    else:
        break

print(count)
