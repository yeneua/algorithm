def convert(hex): # 16진수 -> 10진수 변환
    hex_info = '0123456789ABCDEF'
    result = 0
    for k in range(round):
        num = hex_info.find(hex[k])
        result += (16 ** (round-1-k) * num)
    return result

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = list(input())

    round = N // 4 # 숫자 개수
    hex_numbers = []

    for i in range(round): # 회전 수만큼
        for j in range(i, i + N, round):
            temp = ''
            if j + round >= N: # 인덱스를 넘어 가는 경우
                temp += ''.join(numbers[j:N]) # j에서 끝까지 더하고
                temp += ''.join(numbers[0:round-len(temp)]) # 모자란 개수만큼 0번 인덱스부터 더해줌
                hex_numbers.append(temp)
            else:
                hex_numbers.append(''.join(numbers[j:j + round]))

    values = set() # 중복 숫자 제거
    for num in hex_numbers:
        values.add(convert(num))

    sorted_values = sorted(list(values),reverse=True) # 리스트로 변환하고 내림차순 정렬

    print(f'#{tc} {sorted_values[K-1]}')
