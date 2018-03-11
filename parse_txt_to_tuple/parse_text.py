from collections import namedtuple

tup_list = []
LetterData = namedtuple('LetterData', ['input', 'output'])

with open('ocr_train.txt') as f:
    text = list(f)

for line in text:
    elements = list(filter(None, line.strip('_\n').split('\t')))
    if elements:
        tup_list.append(LetterData(input=elements[1].strip('im'), output=elements[2]))
print(*tup_list[:10], sep='\n')
