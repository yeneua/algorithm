def merge(left, right):
    global count
    l = r = 0
    result = [0] * (len(left) + len(right))
    
    if left[-1] > right[-1]:
        count+=1
    
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l+=1
        else:
            result[l+r] = right[r]
            r+=1
    
    while l < len(left):
        result[l+r] = left[l]
        l+=1
    
    while r<len(right):
        result[l+r] = right[r]
        r+=1
    
    return result

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left_list = merge_sort(left)
    right_list = merge_sort(right)
    
    merged_list = merge(left_list,right_list)
    return merged_list

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    count = 0
    result_num = merge_sort(num)
    print(f'#{tc} {result_num[N//2]} {count}')
