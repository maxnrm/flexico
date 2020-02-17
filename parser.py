import re

file = open('thetomb.txt', 'r')
content = file.read()
file.close()

text = re.findall(r'\w+', content)

uniq_entries = []

for word in text:
    if len(word) > 1 and word not in uniq_entries:
        uniq_entries.append(word)
uniq_entries = sorted(uniq_entries)
print(len(uniq_entries))

with open('lexi.co', 'a') as file:
    for entry in uniq_entries:
        file.write('%s\n' % entry)