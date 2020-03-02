with open('lexi.co', 'r+') as f:
    words = f.readlines()

with open('known.co', 'r+') as f:
    known_words = f.readlines()

with open('new.co', 'r+') as f:
    new_words = f.readlines()

for word in words:
    if word not in new_words and word not in known_words:
        print('\033c')
        print(word)
        key = input('Do you know this word?')

        if key == 'n':
            new_words.append(word)
        elif key == 'b':
            break
        else: 
            known_words.append(word)

with open('known.co', 'w+') as f:
    for word in known_words:
        f.write(word)

with open('new.co', 'w+') as f:
    for word in new_words:
        f.write(word)
