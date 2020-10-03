import pyperclip
text = pyperclip.paste().split('\n')
for i in range(len(text)):
    text[i] = '* ' + text[i] 
print(text[i])
