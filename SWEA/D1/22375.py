T = int(input())

for tc in range(1,T+1):
    N = int(input())
    switch_before = list(map(int, input().split()))
    switch_after = list(map(int, input().split()))

    count = 0

    for i in range(N):
        if switch_before[i] != switch_after[i]:
            count += 1
            for j in range(i,N):
                switch_before[j] = int(not switch_before[j])

    print(f'#{tc} {count}')


'''
인덱스 차례대로 검사
다른값이 나오면 그 인덱스부터 끝까지 모두 반대로
'''
