T = int(input())
for tc in range(1, T+1):
    word = input()
    result = -1

    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            result = 0
            break
    else: result = 1

    print(f'#{tc} {result}')
