T = int(input())

for tc in range(1, T+1):
    N, limit_cal = map(int, input().split())
    score = [0] * N
    cal = [0] * N
    
    for i in range(N):
        input_score, input_cal = map(int, input().split())
        score[i] = input_score
        cal[i] = input_cal
    
    def calculate_score(arr): # 점수 계산
        result = 0
        for k in range(N):
            result += arr[k] * score[k]
        return result
    
    max_score = float('-inf')
    
    def hamburger(cnt, cur_cal, cur_selected): # 카운트, 현재 칼로리, 재료 선택 여부
        global max_score
        
        if cur_cal > limit_cal:
            return
        
        if cnt == N: # 카운트가 N이 될때까지(level이 N)
            max_score = max(max_score, calculate_score(cur_selected)) # 점수 계산
            return
        
        for i in range(2): # 1 or 0 == 선택 or 선택x
            new_selected = cur_selected + [i] # 선택했는지 안했는지. 1,0 여부
            new_cal = cur_cal + new_selected[-1] * cal[cnt] # 현재 칼로리에 해당 카운트에서 추가한 재료 칼로리 더하기(바로 윗줄에서 고른 1,0 * 칼로리 - 음식 재료의 칼로리 인덱스는 cnt와 같음!)
            hamburger(cnt+1,new_cal, new_selected)
    
    hamburger(0,0,[])
    
    print(f'#{tc} {max_score}')
