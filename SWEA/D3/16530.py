operator = '+-*/'

def calculate_postfix(postfix):
    stack = []
    answer = ''
    for i in range(len(postfix)):
        if postfix[i] == '.': # .이면 출력
            if len(stack) == 1:
                answer = int(stack.pop())
                return answer
            else: # 스택에 남아있는게 한개가 아니면 error
                answer = 'error'
                return answer

        if postfix[i] not in operator: # 피연산자면 스택에 push
            stack.append(int(postfix[i]))
        else:
            if stack: # 연산자일 경우 스택에서 피연산자 두개 pop
                right = stack.pop()
                if stack:
                    left = stack.pop()
                else:
                    answer = 'error'
                    return answer
            else:
                answer = 'error'
                return answer
            if postfix[i] == '+':
                temp_cal = left + right
            elif postfix[i] == '-':
                temp_cal = left - right
            elif postfix[i] == '*':
                temp_cal = left * right
            elif postfix[i] == '/':
                temp_cal = left / right
            stack.append(temp_cal)


T = int(input())

for tc in range(1, T+1):
    postfix = input().split()
    print(f'#{tc} {calculate_postfix(postfix)}')