T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = [0] * (N+1) # 인덱스 번호 사용 -> N+1로 만들기
    
    for i in range(Q):
        left, right = map(int, input().split())
        for k in range(right-left+1): # 끝 번호 - 시작번호 + 1 횟수만큼 반복
            boxes[left+k] = i+1 # left번째 상자부터 right 까지. Q 횟수별로 숫자 1부터 넣기(i)
    del boxes[0] # 인덱스 0 지우기
    print(f'#{tc}', *boxes)
