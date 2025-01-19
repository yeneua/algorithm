# 자릿수 더하기

num = int(input())
result = 0

while num:
    result += num % 10
    num = num // 10
    if num == 0: break

print(result)