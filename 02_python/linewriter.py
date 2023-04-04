"""
    lab: 02_python
    author: @lubiku
"""

def writeTextToFile(random_text = ''):
    file_name = 'soubor.txt'
    STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "
 
    with open(file_name, 'w') as file:
        file.write(f'{STATICKY_TEXT}{random_text}')
 
    return file_name
    