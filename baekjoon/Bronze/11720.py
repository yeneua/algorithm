# 숫자의 합

N = int(input())
numbers = list(input())
result = 0

for i in range(N):
    result += int(numbers[i])

print(result)