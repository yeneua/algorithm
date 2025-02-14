# 첫 번째 풀이
def check_crossword(N, K, puzzle):
    correct_crossword = [1]*K
    count = 0
    # 1. 행 순회
    for i in range(N):
        for j in range(N-K+1):
            if puzzle[i][j:j+K] == correct_crossword:
                if j == 0:
                    if puzzle[i][j+K] == 0:
                        count +=1
                if j + K == N:
                    if puzzle[i][j-1] == 0 :
                        count += 1
                if 0 < j and j+K < N:
                    if puzzle[i][j-1] == 0 and puzzle[i][j+K] ==0:
                        count += 1
    # 2. 열 순회
    for j in range(N):
        for i in range(N-K+1):
            temp = []
            for k in range(i,i+K):
                temp.append(puzzle[k][j])
            if temp == correct_crossword:
                if i == 0:
                    if puzzle[i+K][j] == 0:
                        count +=1
                if i + K == N:
                    if puzzle[i-1][j] == 0 :
                        count += 1
                if 0 < i and i+K < N:
                    if puzzle[i-1][j] == 0 and puzzle[i+K][j] ==0:
                        count += 1
    return count
 
T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {check_crossword(N, K, puzzle)}')


# 두 번째 풀이
def check_crossword(N, K, puzzle):
    result = 0
    for i in range(N):
        count = 0
        for j in range(N):
            if puzzle[i][j]==1:
                count += 1
            else:
                if count == K:
                    result += 1
                    count = 0
                else:
                    count = 0
            if j == N-1 and count == K:
                result += 1
    
    for j in range(N):
        count = 0
        for i in range(N):
            if puzzle[i][j]:
                count += 1
            else:
                if count == K:
                    result += 1
                    count = 0
                else:
                    count = 0
            if i == N-1 and count == K:
                result += 1

    return result

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {check_crossword(N, K, puzzle)}')
