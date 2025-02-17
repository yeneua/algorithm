def change_postfix(infix):
    stack = []
    postfix=''

    for i in range(len(infix)):
        if infix[i] != '+':
            postfix += infix[i] # + 연산자 아니면 바로 postfix로
        else:
            while stack:
                postfix += stack.pop() # pop해서 스택에서 꺼내기
            stack.append(infix[i])
    while stack:
        postfix += stack.pop() # 스택이 빌 때까지 출력
    return postfix

def calculate(postfix):
    stack = []
    for i in range(len(postfix)):
        if postfix[i] != '+': # + 연산자가 아니면
            stack.append(int(postfix[i])) # 스택에 push
        else: # 연산자일 경우
            right = stack.pop() # 연산할 숫자 개수만큼 꺼내기 
            left = stack.pop() # 먼저 꺼낸 게 오른쪽에 온다!
            stack.append(left + right) # 연산 결과도 push
    return stack.pop() # 결과

for tc in range(1,11):
    N = int(input())
    expression = input()
    print(f'#{tc} {calculate(change_postfix(expression))}')