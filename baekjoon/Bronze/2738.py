N, M = map(int, input().split())

matrix_A = [list(map(int, input().split())) for _ in range(N)]
matrix_B = [list(map(int, input().split())) for _ in range(N)]

result =[[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        result[i][j] = matrix_A[i][j] + matrix_B[i][j]
        print(result[i][j], end=' ')
    print()
