T = int(input())
for tc in range(1, T+1):
    target = list(map(int, input()))
    N = len(target)
    count = 0
    
    value = [0] * N
    
    for i in range(N):
        if target[i] != value[i]:
            count += 1
            for j in range(i,N):
                value[j] = target[i]
        else:
            continue
    
    print(f'#{tc} {count}')
