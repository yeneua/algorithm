T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    result = ''
    
    for i in range(1,10):
        if N % i ==0: # 나누어 떨어지는 수일때
            remain = N // i # 몫을 remain에 저장
            if 1 <= remain <= 9: # 몫이 1 ~ 9 사이인지?
                result = 'Yes'
                break
    else:
        result = 'No'
        
    print(f'#{tc} {result}')
