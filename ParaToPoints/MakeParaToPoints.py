#program which bullets a paragraph for readability

import pyperclip

def newline_split():
    text = pyperclip.paste().split("\n")
    output(text)
    
def fullstop_split():
    text = pyperclip.paste().split(".")
    while '' in text:
        text.remove('')
    output(text)
    
def output(text):
    for i in range(len(text)):
        while text[i][0] == ' ':
            text[i] = text[i][1:]
        text[i] = bullets_choice + ' ' + text[i]
    output = '\n'.join(text)

    print(output)
    pyperclip.copy(output)
    print("\nCopied to clipboard")

bullets_choice = input(f"Which type of bullet point would you like ")
split_type = input("How would you like to split, through fullstop or newline? ")
if split_type.lower() in ['fullstop', 'newline', '.', '\n']:
    if split_type.lower() in ['fullstop', '.']:
        fullstop_split()
    else:
        newline_split()
else:
    print("Unrecognized splitting character, please try again")


