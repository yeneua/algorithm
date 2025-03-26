from collections import deque

T = int(input())
for tc in range(1, T+1):
    K = int(input()) # 자석 회전 횟수
    magnetics = [list(map(int, input().split())) for _ in range(4)]
    magnetics.insert(0, [0] * 8) # 인덱스를 자석번호 그대로 사용하기위해
    
    magnetic_info = {1:(2,), 2:(1,3), 3:(2,4), 4:(3,)} # 몇번쨰 자석일때 어느 자석을 검사할건지(1일땐 2를 보면 되고, 2일땐 1,3을 봄. 큐에 다음 검사할 자석을 추가하기 때문에 양옆 자석만 검사하면 된다.)
    
    def turn(arr): # 자석 돌리는 함수
        for num, dir in arr:
            if dir == 1: # 시계방향일때
                temp = magnetics[num][-1] # 제일 뒤가 제일 앞으로 온다
                for item in range(7, 0, -1):
                    magnetics[num][item] = magnetics[num][item-1]
                magnetics[num][0] = temp
            else: # 반시계방향일때
                temp = magnetics[num][0] # 제일 앞에가 제일 뒤로 간다
                for item in range(7):
                    magnetics[num][item] = magnetics[num][item+1]
                magnetics[num][-1] = temp
    
    def get_score(arr): # 점수를 구하는 함수
        score = 0
        for i in range(5):
            if i == 0:
                continue
            
            if arr[i][0] == 1:
                score += 2 ** (i-1) # 1,2,4,8을 2의 거듭제곱으로 표현
        return score
    
    for _ in range(K):
        num, dir = map(int, input().split()) # 회전시킬 자석 번호, 방향
        
        command = [] # 회전시킬 자석 정보 저장
        next_visit = deque() # 어느 자석을 볼건지
        visited = [0] * 5 # 인덱스를 자석번호 그대로 사용하기위해
        
        # 시작 노드 처리
        command.append((num,dir)) # 최종적으로 회전시킬 자석번호와 방향 저장
        next_visit.append(num)
        visited[num] = 1
        
        while next_visit:
            current = next_visit.popleft()
            
            for item in magnetic_info[current]:
                if visited[item] == 1:
                    continue
                if current < item: # 어느 자석이 왼쪽, 오른쪽에 있는지 검사
                    if magnetics[current][2] != magnetics[item][6]:
                        if (item % 2) == (num % 2): # 입력으로 받는 기준 자석과 홀/짝이 같으면 동일한 방향
                            item_dir = dir
                        else: # 홀/짝이 다르면 다른 방향
                            item_dir = -dir
                        command.append((item, item_dir))
                        next_visit.append(item)
                        visited[item] = 1
                else:
                    if magnetics[current][6] != magnetics[item][2]:
                        if (item % 2) == (num % 2):
                            item_dir = dir
                        else:
                            item_dir = -dir
                        command.append((item, item_dir))
                        next_visit.append(item)
                        visited[item] = 1
        
        turn(command)        
        result = get_score(magnetics)
            
    print(f'#{tc} {result}')
