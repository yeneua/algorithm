def get_code(N, M, inputs):
    code = []
    for i in range(N):
        for j in range(M):
            if inputs[i][j] == 1:
                code = inputs[i][j:j+56] # 1을 만나면 56개 가져오기
                break
    # 암호코드는 0부터 시작 가능
    # but, 암호코드는 1로 끝
    # 끝이 1이 아닌 경우 0을 삭제하고, 그만큼 0번째에 0을 추가함
    count = 0
    for k in range(55,-1,-1):
        if code[k] == 0:
            count += 1
        else:
            break

    for l in range(count):
        del code[-1]
        code.insert(0,0)

    return ''.join(map(str, code))

def decode(code): # 암호코드 숫자로 변환
    decoded = []
    code_info_values = list(code_info.values())
    for i in range(0,56,7):
        item = (code[i:i+7])
        decoded.append(code_info_values.index(item))
    return decoded

def calculate(numbers): # 계산
    result = 0
    odd_sum = 0
    for i in range(8):
        if i % 2: # 짝수
            result += numbers[i]
        else:
            odd_sum += numbers[i]
    result += odd_sum*3

    if result % 10 == 0: # 10의 배수이면
        return result - odd_sum*2
    else:
        return 0


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    inputs = [list(map(int, input())) for _ in range(N)]

    code_info = {0: '0001101', 1: '0011001', 2: '0010011', 3: '0111101', 4: '0100011', 5: '0110001', 6: '0101111',
                 7: '0111011', 8: '0110111', 9: '0001011'}

    code = get_code(N,M,inputs)
    numbers = decode(code)
    answer = calculate(numbers)

    print(f'#{tc} {answer}')

'''
1. input 받기
2. 암호코드 부분만 가져오기
- 코드는 전부 0으로 시작
- 가장 끝자리는 1임
3. 7칸씩 숫자로
4. 계산
'''
