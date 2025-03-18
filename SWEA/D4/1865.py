def get_success(row, selected, percent):
    global max_value

    if percent <= max_value: # 확률은 1보다 작으므로 최대값보다 작으면 리턴
        return

    if row == N:
        max_value = max(max_value, percent)
        return

    for j in range(N):
        if selected[j]:
            continue
        else:
            selected[j] = 1
            get_success(row+1, selected, percent * 0.01 * success[row][j])
            selected[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    success = [list(map(int,input().split())) for _ in range(N)]
    max_value = 0
    get_success(0,[0]*N, 1)
    print(f'#{tc} {format(max_value*100,".6f")}') # 소수점 6번째 자리까지 출력
