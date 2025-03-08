T = int(input())

for tc in range(1,T+1):
    N = int(input())

    start = [0]*N # Ai
    end = [0]*N # Bi

    for i in range(N):
        left, right  = map(int, input().split())
        start[i] = left
        end[i] = right
    
    count = 0

    for k in range(N):
        for l in range(k+1, N):
            if (start[k] > start[l] and end[k] < end[l]) or (start[k] < start[l] and end[k] > end[l]):
                count += 1
    print(f'#{tc} {count}')
