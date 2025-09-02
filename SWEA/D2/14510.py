T = int(input())

for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    answer = 0
    
    max_tree = max(trees)
    
    delta = [0] * N
    for i in range(N):
        delta[i] = max_tree - trees[i]
    
    one = 0
    two = 0

    for i in range(N):
        two += delta[i] // 2
        if delta[i] % 2 == 1:
            one += 1

    while two > one + 1: # 짝수, 홀수 개수 맞추기 -> 홀수 날이 먼저 시작하니까 two > one + 1 조건
        two -= 1
        one += 2

    if two == one:
        answer = two * 2
    elif two > one: # 짝수 날로 끝나는 경우
        answer = two * 2
    elif two < one: # 홀수 날로 끝나는 경우
        answer = one * 2 - 1
              
    print(f'#{tc} {answer}')