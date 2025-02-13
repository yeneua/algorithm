T = int(input())

for tc in range(1, T+1):
    text = input()

    def check_braket_pair(text):
        stack = [0] * len(text)
        top = -1

        for element in text:
            if element == '(':
                top += 1
                stack[top] = element
            elif element == '{':
                top += 1
                stack[top] = element
            elif element ==')':
                if stack[top] == '(':
                    top -= 1
                else:
                    return 0
            elif element == '}':
                if stack[top] == '{':
                    top -= 1
                else:
                    return 0

        if top == -1:
            return 1
        else:
            return 0

    print(f'#{tc} {check_braket_pair(text)}')
