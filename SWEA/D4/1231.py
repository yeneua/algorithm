for tc in range(1,11):
    N = int(input()) # 정점의 총 수
    left =[0] * (N+1)
    right = [0] * (N + 1)
    words = [0] * (N+1)

    for i in range(1, N+1):
        if i <= N//2:
            inputs = list(input().split()) # 인덱스 0 : 정점 번호, 1 : 문자, 2 : 왼쪽 자식 번호, 3 : 오른쪽 자식 번호
            left[int(inputs[0])] = int(inputs[2])
            if N % 2 == 0 and i < N//2:
                right[int(inputs[0])] = int(inputs[3])
            if N % 2:
                right[int(inputs[0])] = int(inputs[3])
        else:
            inputs = list(input().split())
        words[int(inputs[0])] = inputs[1]

    result = ''
    def in_order(t):
        global result
        if t:
            in_order(left[t])
            result += words[t]
            in_order(right[t])

    in_order(1)
    print(f'#{tc} {result}')

'''
정점 번호별로 문자를 저장
정점번호로 부모 자식 연결
중위순회로 출력

input 받을 때
1. N이 짝수인 경우
- N//2 번째는 right가 없다
2. N이 홀수인 경우
- N//2 번째까지 right 존재
'''
