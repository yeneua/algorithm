T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    
    numbers = list(map(int, input().split()))
    
    answer = 0
    
    def subsum(cnt, cur_sum):
        global answer
        
        if cur_sum == K:
            answer += 1
            return
        
        if cur_sum > K:
            return
        
        if cnt == N:
            return
        
        subsum(cnt + 1, cur_sum+numbers[cnt])
        subsum(cnt+1, cur_sum)
    
    subsum(0,0)
    
    print(f'#{tc} {answer}')
