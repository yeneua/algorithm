N = int(input())

answer = 1
i = 0
count = 1
while True:
    i += 1
    if N <= count:
        print(i)
        break
    count += i*6

# 벌집 개수는 6의 배수로 늘어남
# 1 - 1번방(1개)
# 2 - 2 ~ 7번방(6개)
# 3 - 8 ~ 19번방(12개)
# 4 - 20 ~ 37번방(18개)
