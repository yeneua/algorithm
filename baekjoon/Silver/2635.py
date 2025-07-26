def solution(num):
    global answer_len, answer 

    for i in range(num, 0, -1):
        lst = [num]
        lst.append(i)

        while True:
            next = lst[len(lst)-2] - lst[len(lst)-1]
            if next >= 0:
                lst.append(next)
            else:
                if answer_len < len(lst):
                    answer_len = len(lst)
                    answer = lst
                break

num = int(input())
answer_len = 0
answer = []
solution(num)

print(answer_len)
print(*answer)
