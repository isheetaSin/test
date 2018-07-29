strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''
count = 0
for i in strings:
    if count == 0:
        sentence = sentence + i
    else:
        sentence = sentence + " " + i
    count = count + 1

print(sentence)

test = ' '.join(strings)
print(' '.join(strings))

if sentence == test:
    print("Test passed")
