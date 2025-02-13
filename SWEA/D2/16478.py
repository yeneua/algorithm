T = int(input())

for tc in range(1, T+1):
    string = input()

    stack =[0] * len(string)
    top = -1
    for text in string:
        top += 1
        stack[top] = text

        if top > 0 and stack[top] == stack[top-1]:
            top -= 2
            
    print(f'#{tc} {top+1}')
