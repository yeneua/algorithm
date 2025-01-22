# 최대수 구하기

T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    numbers.sort()
    result = numbers[9]
    print(f'#{i} {result}')
