def decimal_point_to_binary(num):
    result = ''
    pow = -1
    while num > 0.0: # 숫자에서 2^-1 , 2^-2 .. 계속 빼기
        if num >= (2 ** pow):
            result += '1' # 뺄 수 있으면 1
            num -= (2 ** pow)
        else: # 뺄 수 없으면 0 (== 그 자리수는 안들어간다는 말)
            result += '0'
        pow -= 1
        if len(result) == 13:
            result = 'overflow'
            return result
    return result

T = int(input())

for tc in range(1, T+1):
    N = float(input())
    print(f'#{tc} {decimal_point_to_binary(N)}')
