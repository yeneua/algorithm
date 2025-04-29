X = int(input())

cross = 0 # 대각선 원소 개수
i = 0 # X가 몇번째 대각선에 위치하고 있는지

while True:
    if X <= cross:
        cross -= i
        break    
    i += 1
    cross += i # 대각선의 원소 개수는 1+2+3+... 순으로 늘어남

# 홀수번째 대각선
# - 분자 작아짐
# - 분모 커짐

# 짝수번째 대각선
# - 분자 커짐
# - 분모 작아짐

if i % 2: # 홀수번째 대각선
    # 시작점 : i / 1
    top = i
    bottom = 1
    for j in range(1, i+1):
        cross += 1
        if cross == X:
            break
        top -= 1
        bottom += 1
else:
    # 시작점 : 1 / i
    top = 1
    bottom = i
    for j in range(1,i+1):
        cross += 1
        if cross == X:
            break
        top += 1
        bottom -= 1

print(f'{top}/{bottom}')
