# 홀수만 더하기

T = int(input())

for test_case in range(T):
    numbers = list(map(int, input().split()))
    result = 0
    for num in numbers:
        if num % 2:
            result += num
    print(f'#{test_case + 1} {result}')