def calculate(num1, num2, operator):
    if operator == 0 :
        return num1 + num2
    elif operator == 1:
        return num1 - num2
    elif operator== 2:
        return num1 * num2
    elif operator == 3:
        if num1 < 0:
            return -(num1 // (-num2))
        else:
            return num1 // num2

def solve(cnt, cur_value, visited):
    global min_value, max_value
    
    if cnt == N-1:
        min_value = min(min_value, cur_value)
        max_value = max(max_value, cur_value)
        return

    for i in range(4):
        if visited[i] == 0:
            continue
        visited[i] -= 1
        temp = calculate(cur_value, nums[cnt+1], i)
        solve(cnt+1, temp, visited)
        visited[i] += 1


N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

min_value = 1000000000
max_value = -1000000000

solve(0, nums[0], operators)

print(max_value)
print(min_value)

'''
if cur_value >= min_value:
    return
solve 함수 내에 가지치기로 위와 같이 코드를 작성했었음 -> 오답
왜? +, -, *, // 총 4가지 연산이므로 뒤에 연산에서 값이 작아지거나 커질 수 있기 때문
'''