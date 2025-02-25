T = int(input())
for tc in range(1, T+1):
    N, D = map(int, input().split())
    if N % (1+2*D) == 0:
        answer = N // (1+2*D)
    else:
        answer = (N // (1+2*D)) + 1
    print(f'#{tc} {answer}')


'''
[x-D,x+D] 구간에는 1+2D개만큼의 꽃에 물을 줄 수 있음
(1+2D) 단위로 N개의 꽃에 모두 물을 줘야함
딱 나누어 떨어질 경우는 N//(1+2D)번만큼
나누어 떨어지지 않는 경우에는 N//(1+2D) + 1번
'''
