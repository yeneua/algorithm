# 몫과 나머지 출력하기

T = int(input())

for test_case in range(1, T+1):
    operand1, operand2 = map(int, input().split())
    print(f'#{test_case} {operand1//operand2} {operand1%operand2}')