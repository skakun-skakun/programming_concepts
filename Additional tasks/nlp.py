import json
from random import choice

with open('Craig_Martin_A_Critical_Introduction_to_the_Study_of_Religion_Routledge.txt', 'r', encoding='utf8') as f:
    raw_data = ' '.join([line.strip().replace('\n', '') for line in f.readlines() if line != '\n']).split()
# print(raw_data)
data = {}
for word_i in range(len(raw_data)-1):
    if raw_data[word_i] not in data:
        data[raw_data[word_i]] = []
    if raw_data[word_i+1] not in data[raw_data[word_i]]:
        data[raw_data[word_i]].append(raw_data[word_i+1])

# with open('data.json', 'w', encoding='utf8') as f:
#     json.dump(data, f)

word = choice(list(data.keys()))
for i in range(1200):
    print(word, end=' ')
    if '.' in word or '!' in word or '?' in word:
        print()
    word = choice(data[word])
    if not data[word]:
        word = choice(list(data.keys()))
while '.' not in word and '!' not in word and '?' not in word:
    print(word, end=' ')
    word = choice(data[word])
    if not data[word]:
        word = choice(list(data.keys()))
print(word)

