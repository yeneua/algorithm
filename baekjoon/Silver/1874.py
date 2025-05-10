N = int(input())
numbers = [] # 만들어야 할 수열
for _ in range(N):
    numbers.append(int(input()))

answer = [] # 내가 만들 수열
stack = []

j = 0 # 들어갈 숫자
for i in range(N):
    while numbers[i] > j: # 만들어야 할 수열의 숫자가 될때까지 push
        j += 1
        stack.append(j)
        answer.append('+')
    
    if numbers[i] == j: # push한 숫자와 j가 같아지면 pop
        stack.pop()
        answer.append('-')
    
    while stack and numbers[i] < j: # 넣을 수 있는 숫자보다 만들어야 할 수열의 숫자가 작으면 pop
        if stack[-1] == numbers[i]:
            stack.pop()
            answer.append('-')
        else: # pop 할 수 있는만큼 하면 멈추고 다음 i로 넘어가기
            break

if stack: # 만들 수 없는 수열이라면 stack이 남아있음
    print('NO')
else:
    for item in answer:
        print(item)
