T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    
    customer.sort() # 먼저 온 순서대로 정렬
    
    bungeoppang = 0
    idx = 0 # 손님 인덱스
    result = 'Possible'
    
    for i in range(0, customer[-1] + 1): # 0초부터 ~ 마지막에 도착하는 손님 시간까지 검사
        
        if i == 0 and customer[0] == 0: # 0초일때 0초에 도착하는 손님 있으면 Impossible
            result = 'Impossible'
        
        if i == 0: continue # 위 조건 안걸리면 continue
    
        if i % M == 0: # M초마다 K개씩
            bungeoppang +=  K
        
        if customer[idx] <= i: # 도착한 손님이 있을때
            if bungeoppang == 0: # 붕어빵 없으면
                result = 'Impossible' # Impossible
                break
            bungeoppang -= 1 # 붕어빵 있으면 -1개
            idx += 1 # 다음 손님
            
    print(f'#{tc} {result}')
