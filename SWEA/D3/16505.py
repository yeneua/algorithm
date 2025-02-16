# 첫 번째 풀이
T = int(input())

for tc in range(1, T+1):
    N = int(input())//10
    tape = [0] * (N+1)
    tape[0] = 0
    tape[1] = 1
    tape[2] = 3
    tape[3] = 5
    for i in range(4,N+1):
        tape[i] = tape[i-1] + 2*tape[i-2]
    print(f'#{tc} {tape[N]}')


# 두 번째 풀이 - 재귀
def calculate_tape_cape(N):
    if N == 1:
        return 1
    if N == 2 :
        return 3
    if N > 2:
        return calculate_tape_cape(N-1) + calculate_tape_cape(N-2)*2

T = int(input())

for tc in range(1, T+1):
    N = int(input())//10
    print(f'#{tc} {calculate_tape_cape(N)}')