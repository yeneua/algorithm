T = int(input())

for tc in range(1, T+1):

    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N-1, -1, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    print(f'#{tc}', end=' ')
    for number in numbers:
        print(number, end=' ')
    print()
    