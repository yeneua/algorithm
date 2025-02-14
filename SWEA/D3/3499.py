T = int(input())
for tc in range(1, T+1):
    N = int(input())
    deck = list(input().split())
        
    print(f'#{tc}', end=' ')
    for i in range(N//2):
        print(deck[i], deck[(N//2 + i) + 1*(N%2)], end=' ')
    if N%2: print(deck[N//2], end=' ')
    print()
