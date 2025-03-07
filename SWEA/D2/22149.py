T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = 0

    # 첫 번째 풀이
    while numbers:
        temp = numbers.pop()
        if temp not in numbers:
            result = temp
            break
        else:
            numbers.remove(temp) # 같은 게 있으면 삭제

    print(f'#{tc} {result}')

'''
# 두 번째 풀이
xor_num = 0

for num in numbers:
    xor_num ^= num

# 숫자 0이랑 id를 xor(^) 연산
# 두번 등장한 id는 원래대로 돌아옴
# 한번 등장한 id는 0 ^ id = id
'''
