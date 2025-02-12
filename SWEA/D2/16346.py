T = int(input())

for tc in range(1, T+1):
    pattern = input()
    text = input()

    i = 0 # text
    j = 0 # pattern
    result = 0

    while i < len(text):
        if text[i] != pattern[j]:
            i = i - j + 1
            j = 0
        else:
            i += 1
            j += 1
        if j == len(pattern):
            result = 1
            break

    print(f'#{tc} {result}')
