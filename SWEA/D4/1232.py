def in_order(t):
    global expression
    if t:
        in_order(left[t])
        in_order(right[t])
        expression.append(nodes[t])

def calculate(postfix):
    stack = []
    for item in postfix:
        if type(item) == int:
            stack.append(item)
        else:
            right = stack.pop()
            left = stack.pop()

            if item == '+':
                stack.append(left+right)
            elif item == '-':
                stack.append(left-right)
            elif item == '*':
                stack.append(left*right)
            elif item =='/':
                stack.append(left/right)

    result = int(stack.pop())
    return result

for tc in range(1,11):
    N = int(input())
    nodes = [0] * (N+1) # 노드 값
    left = [0] * (N+1)
    right = [0] * (N+1)
    
    for _ in range(N):
        inputs = list(input().split())
        node_num = int(inputs[0])
        if len(inputs) == 4:
            nodes[node_num] = inputs[1]
            left[node_num] = int(inputs[2])
            right[node_num] = int(inputs[3])
        else:
            nodes[node_num] = int(inputs[1])

    expression = [] # 후위표기식
    in_order(1)
    answer = calculate(expression)
    print(f'#{tc} {answer}')

'''
# 과정
1. input 받기
- 값 저장 nodes
- 왼쪽, 오른쪽 자식 부모 노드 번호를 인덱스로 저장 left, right

2. 후위표기식으로 변환
3. 계산

# 후위표기식 계산하기
필요한거 -> 스택
1. 앞에서 하나씩 꺼냄
2. 숫자면 push
3. 연산자면
4. 두개 pop으로 꺼냄(왜 두개? 연산할때 두개 필요하니까)
5. 계산한 값 다시 push
...
6. 마지막 결과값 pop
7. 스택 끝
'''
