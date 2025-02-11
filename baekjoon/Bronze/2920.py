pitch = list(map(int, input().split()))

pitch_names = {'ascending' : [1,2,3,4,5,6,7,8], 'descending': [8,7,6,5,4,3,2,1]}

if pitch == pitch_names['ascending']:
    print('ascending')
elif pitch == pitch_names['descending']:
    print('descending')
else:
    print('mixed')
