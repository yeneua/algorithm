number, B = input().split()
B = int(B)

result = 0
K = len(number)
for i in range(K):
    if number[i] not in '0123456789':
        num = ord(number[i]) - 55
    else:
        num = int(number[i])
    result += num * (B**(K-1-i))

print(result)
