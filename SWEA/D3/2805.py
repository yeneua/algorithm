T = int(input())
for tc in range(1,T+1):
    N = int(input())

    fields =  [list(map(int, input())) for _ in range(N)]
    
    center = N//2
    total= 0
    
    temp = center
    for i in range(N):
        if i < center: # 행이 center(가운데)보다 작을때 N=5라고 가정하면 2칸 -> 1칸 -> 0칸으로 줄어든다
            temp -= 1
        if i > center:
            temp += 1
        if i == center:
            temp -= 1
            total += sum(fields[i]) # 가운데 행 전체합
            continue
        for j in range(N):
            if j <= temp: continue # j가 temp(선택 안하는 칸 수)보다 작으면 넘어감
            if j > center and (N-1-j) <= temp: continue # j가 center 보다 큰 경우. N-1-j : 대칭되는 인덱스를 뜻함. N=5f라고 가정하면 j가 4일때 0, j가 3일때 1
            total += fields[i][j]
    
    print(f'#{tc} {total}')
