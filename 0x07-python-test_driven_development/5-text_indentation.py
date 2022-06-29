#!/usr/bin/python3
"""Module have a function to do the identation
"""


def text_indentation(text):
    """This is the textIdentation function
    Print the text idented
    Args:
       text (Str): Text to do the identation
    """
    if type(text) != str:
        raise TypeError('text must be a string')
    st = True
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i], end='\n\n')
            st = False
        else:
            if st:
                print(text[i], end='')
            else:
                st = True
