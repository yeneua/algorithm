T = int(input())

for tc in range(1, T+1):
    N, text = input().split()

    for s in text:
        print(f'{s * int(N)}', end='')
    print()