T = int(input())

for tc in range(1, T+1):
    H, W, N = map(int, input().split())

    x = (N//H) + 1
    if N % H == 0:
        x = N // H
        y = H
    else:
        y = N % H
    if H == 1:
        x = N // H
        y = N%H + 1
    
    print(f'{y}{"%02d"}' %x)
