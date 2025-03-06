T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    result = (0+M) % N
    print(f'#{tc} {numbers[result]}')
