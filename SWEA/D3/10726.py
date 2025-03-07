# 첫 번째 풀이
def check_is_one(N,M):
    for _ in range(N):
        if M & 1==0:
            return False
        M = M >> 1
    return True

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    if check_is_one(N,M):
        answer = 'ON'
    else:
        answer = 'OFF'
    print(f'#{tc} {answer}')


# 두 번째 풀이 - 비트 마스킹 이용
def check_is_one(N,M):
    mask = (1<<N) - 1 # N번 연속된 1 만들기
    if (M & mask) == mask: # ex. N=4, 1111과 M을 & 연산한 결과가 1111(mask)와 같은지
        return 'ON'
    else:
        return 'OFF'
