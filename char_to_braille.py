# COMP 202 A2 Part 2
# Author: Ye Yuan
# Student ID: 260921269

from helpers import *

# More constants you'll want to use:
SPACE = '..\n..\n..'
HYPHEN = '..\n..\noo' 
APOSTROPHE = '..\n..\no.' 
QUOTES = '..\noo\noo'


############################ Functions

def convert_irregular(c):
    '''(str) -> str
    Convert the irregular characters to French Braille.
    Recall these are: space, hyphen, apostrophe, guillements
    Apostrophe could be represented by `, ’ or '.
    Hyphen could be represented by - or by –.
    Note the constants such as SPACE and HYPHEN above.

    >>> print(convert_irregular('-'))
    ..
    ..
    oo
    >>> convert_irregular('–')
    '..\\n..\\noo'
    >>> convert_irregular('`')
    '..\\n..\\no.'
    >>> convert_irregular("'")
    '..\\n..\\no.'
    >>> convert_irregular("’")
    '..\\n..\\no.'
    >>> convert_irregular("»")
    '..\\noo\\noo'
    >>> convert_irregular("«")
    '..\\noo\\noo'
    '''
    #check if c is an irregular character first
    if(is_irregular(c)):
        #check which specific pattern c belong to, and return the pattern
        if(c in "`'’"):
            return APOSTROPHE
        elif(c in "-–"):
            return HYPHEN
        elif(c == ' '):
            return SPACE
        elif(c in '«»'):
            return QUOTES
        

def decade_pattern(decade_position):
    '''(int) -> str
    Using position in Braille decade, get associated Braille pattern.
    Provided to students. Do not edit this function.

    >>> decade_pattern(0)
    'o.\\n..'
    >>> decade_pattern(9)
    '.o\\noo'
    '''
    DEC_SEQ = ['o.\n..', 'o.\no.', 'oo\n..', 'oo\n.o',
           'o.\n.o', 'oo\no.', 'oo\noo', 'o.\noo',
           '.o\no.', '.o\noo']
    return DEC_SEQ[decade_position]


def convert_digit(c):
    '''(str) -> str
    Convert string representation of digit
    to Braille. For this, put the decade value in the top two rows,
    and put '..' in the bottow row.
    Hints:
        - Remember: we provided the string DIGITS to you
        - For full credit, this should have fewer than 4 lines of code.

    >>> print(convert_digit('1'))
    o.
    ..
    ..
    >>> print(convert_digit('3'))
    oo
    ..
    ..
    >>> print(convert_digit('0'))
    .o
    oo
    ..
    '''
    #check if c is a number first
    if(is_digit(c)):
        #all numbers have .. in the bottom of their patterns
        pattern=decade_pattern(DIGITS.find(c))+'\n..'
        return pattern
    
def convert_punctuation(c):
    '''(str) -> str
    Convert string representation of common punctuation
    to French Braille. For this put the decade value in the bottom
    two rows, and put '..' in the top row.
    Hints: 
        - Use the string PUNCTUATION we provided to you
        - Recall there are helper functions we gave you
        - For full credit, this should have fewer than 4 lines of code.
        - You should not have to manually enter any Braille strings

    >>> print(convert_punctuation(','))
    ..
    o.
    ..
    >>> print(convert_punctuation(';'))
    ..
    o.
    o.
    >>> print(convert_punctuation(':'))
    ..
    oo
    ..
    >>> print(convert_punctuation('"'))
    ..
    oo
    oo
    '''
    #check if c is a punctuation first
    if(is_punctuation(c)):
        #all punctuations have .. on the top of their patterns
        pattern='..\n'+decade_pattern(PUNCTUATION.find(c))
        return pattern

############################# 


def decade_ending(dec_num):
    '''(int) -> str
    For one of the four decades of standard letters in French Braille,
    return the associated bottom-row (see page 3 of pdf.)

    >>> decade_ending(0)
    '..'
    >>> decade_ending(1)
    'o.'
    >>> decade_ending(2)
    'oo'
    >>> decade_ending(3)
    '.o'
    '''
    #in decade 0, all have .. in the bottom-row
    if(dec_num==0):
        return '..'
    #in decade 1, all have o. in the bottom-row
    elif(dec_num==1):
        return 'o.'
    #in decade 2, all have oo in the bottom-row
    elif(dec_num==2):
        return 'oo'
    #in decade 3, all have .o in the bottom-row
    elif(dec_num==3):
        return '.o'

def letter_row(c):
    '''(str) -> int
    For a standard letter in French Braille, return
    the number of the decade it belongs to. (See table on page 3 of pdf.)
    Provided to students. Do not edit this function.

    >>> letter_row('a')
    0
    >>> letter_row('w')
    3
    >>> letter_row('n')
    1
    >>> letter_row('N')
    1
    '''
    c = c.lower() # convert
    for i, decade in enumerate(LETTERS):
        if c in decade:
            return i


def letter_column(c):
    '''(str) -> int
    For a standard letter in French Braille, return
    its position within its decade. (See table on page 3 of pdf.)
    Provided to students. Do not edit this function.

    >>> letter_column('a')
    0
    >>> letter_column('b')
    1
    >>> letter_column('v')
    1
    >>> letter_column('w')
    9
    >>> letter_column('W')
    9
    '''
    c = c.lower() # convert
    for decade in LETTERS:
        if c in decade:
            return decade.find(c)


def convert_letter(c):
    '''(str) -> str
    For one of the standard letters in French Braille,
    return its Braille representation.

    >>> print(convert_letter('a'))
    o.
    ..
    ..
    >>> print(convert_letter('b'))
    o.
    o.
    ..
    >>> print(convert_letter('p'))
    oo
    o.
    o.
    >>> print(convert_letter('ç'))
    oo
    o.
    oo
    >>> print(convert_letter('ô'))
    oo
    .o
    .o
    >>> print(convert_letter('A'))
    o.
    ..
    ..
    >>> print(convert_letter('Œ'))
    .o
    o.
    .o
    '''
    #check if c is a known letter first
    if (is_letter(c)):
        #find the column and row index
        column_index=letter_column(c)
        row_index=letter_row(c)
        #pattern equal to decade pattern plus new line plus ending pattern
        pattern=decade_pattern(column_index)+'\n'+decade_ending(row_index)
        return pattern

def char_to_braille(c):
    '''(str) -> str
    Convert a character, c, into French Braille.
    If c is a character we don't know how to convert, return 
    the same character as before.

    >>> print(char_to_braille('-'))
    ..
    ..
    oo
    >>> print(char_to_braille('w'))
    .o
    oo
    .o
    >>> print(char_to_braille('1'))
    o.
    ..
    ..
    >>> print(char_to_braille('?'))
    ..
    o.
    .o
    >>> char_to_braille('.')
    '..\\noo\\n.o'
    >>> char_to_braille('a')
    'o.\\n..\\n..'
    >>> char_to_braille('n')
    'oo\\n.o\\no.'
    >>> char_to_braille('Z')
    'o.\\n.o\\noo'
    >>> char_to_braille('Œ')
    '.o\\no.\\n.o'
    >>> char_to_braille(' ')
    '..\\n..\\n..'
    >>> char_to_braille('ß')
    'ß'
    >>> char_to_braille('\\n')
    '\\n'
    '''
    #check if c is a known character first
    if(is_known_character(c)):
        #check which type c belong to, and convert it to braille
        if(is_letter(c)):
            return convert_letter(c)
        elif(is_irregular(c)):
            return convert_irregular(c)
        elif(is_digit(c)):
            return convert_digit(c)
        else:
            return convert_punctuation(c)
    #return the initial value otherwise
    else:
        return c


if __name__ == '__main__':
    doctest.testmod()
