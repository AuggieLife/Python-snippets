Title: Parse a text file into a list of named tuples
Date: 2018-03-10 17:07
Modified: 2018-03-10 17:07
Status: published
Category: This site
Tags: python
Slug: first-post
Series: r/learnpython
Series_index: 1
Author: Dale Appleby
Summary: This was brought up on Reddit in LearnPython.  The question revolved around parsing a large text file that contained lines that represented an image.

### Parse a text file into a list of named tuples

This was brought up on Reddit in LearnPython.  The original post can be found here at this [Reddit Link](https://redd.it/822956).
The question revolved around parsing a large text file that contained lines that represented an image.

To Quote:
>Each line is encoded as such. The Number at the beginning represents the observation value, the 0's and 1's after the "im" represent the bits representing the image and the letter right after represents the output.
> ...
>I want to go through every line in the text file and add it as a list of tuples (input, output). In addition the "_2" (index value) and "im" need to be removed.

The text file can be found here:  [ocr_train.txt](/contents/code/ocr_train.txt)

Lets start by declaring a namedtuple to store the info in and reading the file into a list and checking out what each line looks like.


```python
from collections import namedtuple

tup_list=[]
LetterData = namedtuple('LetterData', ['input', 'output'])

with open('ocr_train.txt') as f:
    text = list(f)
print (text[:1])
```
**Output:**

    ['1\tim00000000000000000000000001110000011111000100011011000011100000011000000110000001100000111000111011111000000000000000000000000000\to\t_\n']


Cool!  So it looks like our 'elements' are separated by a tab.  Lets split each line by the `tab` and see what each line looks like.  For now we will just loop through lines 7-9 lines.  (I chose this to show some normal lines plus one of the "blank" lines that are spread throughout the file.)


```python
for line in text[7:10]:
    elements = line.split('\t')
    print(elements)
```
**Output:**

    ['8', 'im00000000000000000000000000000000000011110011100100100001011000011100000110000001100000011000000100000000000000000000000000000000', 'n', '_\n']
    ['9', 'im01111000110000001000000010000000111111110000000100000001000000010000000100000001000000010000000100000011000001100000010000000100', 'g', '_\n']
    ['', '', '', '\n']


OK.. nice!  Except it looks like we have a "blank line" that only contains a 'new line' character (the last list item shown above) and the other lines all have a `_\n`.  Lets change our loop above to get rid of the `_\n`'s as we don't need them anyway.


```python
for line in text[7:10]:
    elements = line.strip('_\n').split('\t')
    print(elements)
```
**Output:**

    ['8', 'im00000000000000000000000000000000000011110011100100100001011000011100000110000001100000011000000100000000000000000000000000000000', 'n', '']
    ['9', 'im01111000110000001000000010000000111111110000000100000001000000010000000100000001000000010000000100000011000001100000010000000100', 'g', '']
    ['', '', '', '']


We may as well go one step further and filter out the empty elements in the list.  Let's chage our loop one more time.


```python
for line in text[7:10]:
    elements = list(filter(None, line.strip('_\n').split('\t')))
    print(elements)
```
**Output:**

    ['8', 'im00000000000000000000000000000000000011110011100100100001011000011100000110000001100000011000000100000000000000000000000000000000', 'n']
    ['9', 'im01111000110000001000000010000000111111110000000100000001000000010000000100000001000000010000000100000011000001100000010000000100', 'g']
    []


Looks good!  We still have an empty list but we will deal with that in a moment. Now the user wants the `input` which is the 2nd element in our list (index =1) less the `im` at the beginning of it and the `output` which is the third item (index=2).  Lets loop through our text, make sure that our list isn't empty and add our items to our `namedtuple`


```python
for line in text:
    elements = list(filter(None, line.strip('_\n').split('\t')))
    if elements:
        tup_list.append(LetterData(input=elements[1].strip('im'), output=elements[2]))
print (*tup_list[:10], sep='\n')
```
**Output:**

    LetterData(input='im00000000000000000000000000000000000011110011100100100001011000011100000110000001100000011000000100000000000000000000000000000000', output='n')
    LetterData(input='im01111000110000001000000010000000111111110000000100000001000000010000000100000001000000010000000100000011000001100000010000000100', output='g')
    LetterData(input='im00000000000000000000000001110000011111000100011011000011100000011000000110000001100000111000111011111000000000000000000000000000', output='o')
    LetterData(input='im00000000000000000000000000000000000000000000000001111110110110111011000110110001000000000000000000000000000000000000000000000000', output='m')
    LetterData(input='im00000000000000000000000000000000000000000000000011100110101011101011101010010011000000000000000000000000000000000000000000000000', output='m')
    LetterData(input='im00000000000000000000000000000000000000000011000001100000100011001001011011100010000000110000000000000000000000000000000000000000', output='a')
    LetterData(input='im00000000000000000000000000000000000011100001101000110010111000101110001011000010110000101000000110000001000000000000000000000000', output='n')
    LetterData(input='im00000000010000000110000001110000010110000110100000101100001001100011001000010010011100101101011010011100101110011110111100000000', output='d')
    LetterData(input='im00001100000000000000000000000000000000000000000000000000000000000000000000010000000100000001000000010000001100000010000000100000', output='i')
    LetterData(input='im00000000000000000000000000000000000011110011100100100001011000011100000110000001100000011000000100000000000000000000000000000000', output='n')

**After all that our finished script looks like…**

```python
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
```
