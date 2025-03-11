# 홀수만 더하기

T = int(input())

for test_case in range(T):
    numbers = list(map(int, input().split()))
    result = 0
    for num in numbers:
        if num % 2:
            result += num
    print(f'#{test_case + 1} {result}')


# 두 번째 풀이
T = int(input())

for tc in range(1, T+1):
    result = [x for x in list(map(int, input().split())) if x % 2 == 1]
    print(f'#{tc}', sum(result))
