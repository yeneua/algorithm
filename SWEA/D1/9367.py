T = int(input())

for tc in range(1, T+1):
    N = int(input())
    scales = list(map(int, input().split()))

    count = 1
    result = 0

    for i in range(N-1):
        if scales[i] < scales[i+1]:
            count += 1
        else:
            count = 1
        if result < count:
            result = count

    print(f'#{tc} {result}')
