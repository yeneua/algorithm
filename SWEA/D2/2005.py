def create_pascal(start, end, before_line): # 1부터 N(end)까지 줄별로 수행
        if start > end: # 마지막줄까지 수행
            return 0
        
        if start == 1: # 첫번째 줄이면 1
            line = [1]
            print(f'#{tc}')
            print(*line)
            create_pascal(start+1, end, line) # 그 다음줄 호출 + 현재 줄 결과값 함께 넘겨줌
        
        if start > 1:
            line = [0] * start # i번째 줄은 i개의 숫자를 가짐 => 길이만큼 0으로 채워진 리스트 만들어줌
            line[0] = line[start-1]= 1 # 첫번째, 마지막 숫자는 1
            for i in range(1, start-2+1): # 첫번째, 마지막을 제외한 숫자들
                line[i] = before_line[i-1] + before_line[i] # 각 숫자는 자신의 왼쪽과 오른쪽 위의 합
            print(*line)
            create_pascal(start+1, end, line) # 그 다음 줄 호출 + 현재 줄 결과값 함께 넘겨줌


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    create_pascal(1, N, 0) # 첫번째 줄은 그 전 줄의 결과값이 없으므로 0을 넘겨줌