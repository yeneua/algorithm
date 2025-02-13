# 첫 번째 풀이
for tc in range(1, 11):
    N = int(input())
    braket_string = list(input())

    def check_braket_pair(N, text):
        stack = [0] * N
        top = -1

        for element in text:
            if element == '(':
                top += 1
                stack[top] = element
            elif element == '[':
                top += 1
                stack[top] = element
            elif element == '{':
                top += 1
                stack[top] = element
            elif element == '<':
                top += 1
                stack[top] = element
            elif element == ')':
                if stack[top] == '(':
                    top -= 1
                else:
                    return 0
            elif element == '}':
                if stack[top] == '{':
                    top -= 1
                else:
                    return 0
            elif element == ']':
                if stack[top] == '[':
                    top -= 1
                else:
                    return 0
            elif element == '>':
                if stack[top] == '<':
                    top -= 1
                else:
                    return 0

        if top == -1:
            return 1
        else:
            return 0

    print(f'#{tc} {check_braket_pair(N, braket_string)}')


# 두 번째 풀이
for tc in range(1, 11):
    N = int(input())
    braket_string = list(input())

    braket_open = ['(', '[', '{', '<']
    braket_closed = [')',']','}','>']

    def check_braket_pair(N, text):
        stack = [0] * N
        top = -1
        idx = -1

        for braket in text:
            if braket in braket_open:
                top += 1
                stack[top] = braket
                idx = braket_open.index(braket)
            elif braket in braket_closed:
                if stack[top] == braket_open[braket_closed.index(braket)]:
                    top -= 1
                else:
                    return 0

        if top == -1:
            return 1
        else:
            return 0


    print(f'#{tc} {check_braket_pair(N, braket_string)}')
