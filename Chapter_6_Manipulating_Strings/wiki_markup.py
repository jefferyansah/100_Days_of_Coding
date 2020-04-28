#!
# wiki_markup.py  A python scripts that add bullet points to a list.


#import Modules
import pyperclip as pcp


#
text = pcp.paste()
print(text)

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pcp.copy(text)
print(text)