N = int(input())

left = [0] * (N+1)
right = [0] * (N+1)

for _ in range(N):
    node, left_c, right_c = input().split()
    if left_c != '.':
        left[ord(node)-64] = ord(left_c)-64
    if right_c != '.':
        right[ord(node)-64] = ord(right_c)-64
        
def pre_order(node):
    if 0 < node <= N:
        print(chr(node+64), end='')
        pre_order(left[node])
        pre_order(right[node])

def in_order(node):
    if 0 < node <= N:
        in_order(left[node])
        print(chr(node+64), end='')
        in_order(right[node])

def post_order(node):
    if 0 < node <= N:
        post_order(left[node])
        post_order(right[node])
        print(chr(node+64), end='')

pre_order(1)
print()
in_order(1)
print()
post_order(1)

'''
알파벳을 아스키코드로 바꿔서 생각
'''