# 최댓값
max_num = 0
max_index = 0

for i in range(9):
    input_num = int(input())
    if max_num < input_num:
        max_num = input_num
        max_index = i+1

print(max_num)
print(max_index)