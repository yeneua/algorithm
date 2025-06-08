nums = list(map(int, input()))
nums.sort(reverse=True)
print(''.join(str(num) for num in nums))
