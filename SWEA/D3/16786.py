# 첫 번째 풀이 
def hex_to_binary(hex, N):
    result = '' # 최종 결과
    for i in range(N):
        num = int(hex_info.find(hex[i]))  # 16진수 문자열을 인덱스로 사용해서 0~15 숫자를 매칭
        temp = '' # 숫자 각 하나를 2진수로 변환한 결과
        while num > 0: # 2진수로 변환
            temp = str(num%2) + temp
            num //= 2
        if len(temp) != 4: # 4자리가 아니면 4자리 맞춰주기
            for _ in range(4-len(temp)):
                temp = '0' + temp
        result += temp
    return result

T = int(input())

for tc in range(1, T+1):
    N, hex_num = input().split()
    N = int(N)
    hex_info = '0123456789ABCDEF'

    print(f'#{tc} {hex_to_binary(hex_num, N)}')


# 두 번째 풀이 - 이진수 변환 비트 이용
def hex_to_binary(hex, N):
    result = ''
    for i in range(N):
        num = int(hex_info.find(hex[i]))
        for j in range(3, -1, -1):
                if num & (1 << j) == 0:
                    result += '0'
                else:
                    result += '1'
    return result