input_word = input().lower()
set_words = set(input_word)
max_count = 0
result = ''

for word in set_words:
    if max_count == input_word.count(word):
        result = '?'
    if max_count < input_word.count(word):
        max_count = input_word.count(word)
        result = word
print(result.upper())
