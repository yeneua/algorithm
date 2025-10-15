list1 = list(input())
list2 = []

N = int(input())
for _ in range(N):
    commands = input()
    if commands.startswith('P'):
        command, string = commands.split()
    else:
        command = commands
    
    if command == 'L' and list1:
        list2.append(list1.pop())
    
    elif command == 'D' and list2:
        list1.append(list2.pop())
    
    elif command == 'B' and list1:
        list1.pop()
    
    elif command == 'P':
        list1.append(string)

print(''.join(list1)+''.join(list2[::-1]))

# 커서를 기준으로 왼쪽은 list1, 오른쪽은 list2로 나눔
# list2는 거꾸로


'''
# 처음 풀이 -> 시간 초과
initial_string = [''] + list(input())
current_string = initial_string
pointer = len(current_string) - 1

N = int(input())
for _ in range(N):
    commands = input()
    if commands.startswith('P'):
        command, string = commands.split()
    else:
        command = commands
    if command == 'L':
        if pointer !=-1:
            pointer -= 1
        else:
            pointer = -1
            
    elif command == 'D':
        if pointer != len(current_string)-1:
            pointer += 1
        else:
            pointer = len(current_string) - 1
    
    elif command == 'B':
        if pointer >= 0:
            del current_string[pointer:pointer+1]
            pointer -= 1

    elif command == 'P':
        current_string.insert(pointer+1, string)
        pointer += 1

print(''.join(current_string).strip())

'''

'''
insert(), del은 최악의 경우 시간 복잡도가 O(n)

list.insert(i, x)
- 시간 복잡도 : O(n)
- 삽입 위치 i 뒤의 모든 요소를 한 칸씩 뒤로 이동

del list[i]
- 시간 복잡도 : O(n)
- 삭제 위치 i 뒤의 모든 요소를 한 칸씩 앞으로 이동

list.append(x)
- 시간 복잡도 : O(1)
- 맨 뒤에 추가, 다른 요소 이동 필요x

list.pop()
- 시간 복잡도 : O(1)
- 맨 뒤 요소 삭제, 다른 요소 이동 필요x
'''