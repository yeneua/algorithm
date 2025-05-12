import sys
M = int(sys.stdin.readline()) # input()으로 받는 입력보다 빠름
S = 0

for _ in range(M):
    commands = sys.stdin.readline().rstrip().split()
    if commands[0] == 'all':
        S = (1<<21)-1
    elif commands[0] == 'empty':
            S = 0

    else:
        command, num = commands[0], int(commands[1])

        if command == 'add':
            S = S | (1 << num-1)

        elif command == 'check':
            if S & 1 << (num-1):
                print('1')
            else:
                print('0')

        elif command == 'remove':
            S = S & ~(1<<num-1)

        elif command == 'toggle':
            S = S ^ (1<<num-1)


'''
# 비트마스킹 이용
# 1. 추가 - i번째 비트만 1로 바꾸기
set = set | (1 << i-1)

# 2. 삭제 - i번째 비트만 0으로 바꾸기
set = set & !(1 << i-1)

# 3. 토글 - i번째 비트 뒤집기
set = set ^ (1 << i-1)

# 4. 확인 - i번째 비트 1인지 0인지
set = set & (1 << i-1)
'''
