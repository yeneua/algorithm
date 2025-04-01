def calculate(idx, num):
    if idx == 0:
        return num*2
    if idx == 1:
        return num*10+1

def solve(num,count):
    global min_count
    if num > E:
        return
    
    if num == E:
        min_count = min(count, min_count)
        return
    
    for i in range(2):
        next_num = calculate(i, num)
        solve(next_num, count + 1)


S, E = map(int, input().split())
min_count = float('inf')

solve(S, 1)

if min_count == float('inf'):
    print('-1')
else:
    print(min_count)
