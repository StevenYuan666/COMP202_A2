# COMP 202 Assignment 2 Part 3
# Author: Ye Yuan
# Student ID: 260921269

import doctest

INCOMPLETE = -1


def ostring_to_raisedpos(s):
    ''' (str) -> str
    Convert a braille letter represented by '##\n##\n##' o-string format
    to raised position format. Provided to students. Do not edit this function.

    Braille cell dot position numbers:
    1 .. 4
    2 .. 5
    3 .. 6
    7 .. 8 (optional)

    >>> ostring_to_raisedpos('..\\n..\\n..')
    ''
    >>> ostring_to_raisedpos('oo\\noo\\noo')
    '142536'
    >>> ostring_to_raisedpos('o.\\noo\\n..')
    '125'
    >>> ostring_to_raisedpos('o.\\noo\\n..\\n.o')
    '1258'
    '''
    res = ''
    inds = [1, 4, 2, 5, 3, 6, 7, 8]
    s = s.replace('\n', '')
    for i, c in enumerate(s):
        if c == 'o':
            res += str(inds[i])
    return res 


def raisedpos_to_binary(s):
    ''' (str) -> str
    Convert a string representing a braille character in raised-position
    representation  into the binary representation.
    TODO: For students to complete.

    >>> raisedpos_to_binary('')
    '00000000'
    >>> raisedpos_to_binary('142536')
    '11111100'
    >>> raisedpos_to_binary('14253678')
    '11111111'
    >>> raisedpos_to_binary('123')
    '11100000'
    >>> raisedpos_to_binary('125')
    '11001000'
    >>> raisedpos_to_binary('278')
    '01000011'
    '''
    #initiate binary with empty first
    binary=''
    #since to all binary expressions have 8 digits
    for i in range(1,9):
        #the digit is 1 if i appears in raisedops expression
        if(str(i) in s):
            binary+='1'
        #the digit is 0 otherwise
        else:
            binary+='0'
    return binary

def binary_to_hex(s):
    '''(str) -> str
    Convert a Braille character represented by an 8-bit binary string
    to a string representing a hexadecimal number.

    TODO: For students to complete.

    The first braille letter has the hex value 2800. Every letter
    therafter comes after it.

    To get the hex number for a braille letter based on binary representation:
    1. reverse the string
    2. convert it from binary to hex
    3. add 2800 (in base 16)

    >>> binary_to_hex('00000000')
    '2800'
    >>> binary_to_hex('11111100')
    '283f'
    >>> binary_to_hex('11111111')
    '28ff'
    >>> binary_to_hex('11001000')
    '2813'
    >>> binary_to_hex('10100000')
    '2805'
    '''
    #reverse the string first
    reverse_binary=s[::-1]
    #change the reverse string to decimal expression
    decimal_reverse_binary=int(reverse_binary,2)
    #when changing to hex expression, add 2800 in base 16
    initial_hex=hex(decimal_reverse_binary+int('2800',16))
    final_hex=initial_hex[2:]
    return final_hex


def hex_to_unicode(n):
    '''(str) -> str
    Convert a braille character represented by a hexadecimal number
    into the appropriate unicode character.
    Provided to students. Do not edit this function.

    >>> hex_to_unicode('2800')
    '⠀'
    >>> hex_to_unicode('2813')
    '⠓'
    >>> hex_to_unicode('2888')
    '⢈'
    '''
    # source: https://stackoverflow.com/questions/49958062/how-to-print-unicode-like-uvariable-in-python-2-7
    return chr(int(str(n),16))


def is_ostring(s):
    '''(str) -> bool
    Is s formatted like an o-string? It can be 6-dot or 8-dot.
    TODO: For students to complete.

    >>> is_ostring('o.\\noo\\n..')
    True
    >>> is_ostring('o.\\noo\\n..\\noo')
    True
    >>> is_ostring('o.\\n00\\n..\\noo')
    False
    >>> is_ostring('o.\\noo')
    False
    >>> is_ostring('o.o\\no\\n..')
    False
    >>> is_ostring('o.\\noo\\n..\\noo\\noo')
    False
    >>> is_ostring('\\n')
    False
    >>> is_ostring('A')
    False
    '''
    #find the amount of dots and newlines
    count_char=s.count('o')+s.count('.')
    count_n=s.count('\n')
    #check the condition for 6-dot
    if(count_char==6 and count_n==2):
        #split the s to two seperate parts, by using two \n
        n1=s[2]
        n2=s[5]
        #check if each \n is on the right position
        result=n1==n2=='\n'
        return result
    #check the condition for 8-dot
    elif(count_char==8 and count_n==3):
        #split the s to three seperate parts, by using three \n
        n1=s[2]
        n2=s[5]
        n3=s[8]
        #check if each \n is on the right position
        result=n1==n2==n3=='\n'
        return result
    #return False otherwise
    else:
        return False
def ostring_to_unicode(s):
    '''
    (str) -> str
    If s is a Braille cell in o-string format, convert it to unicode.
    Else return s.

    Remember from page 4 of the pdf:
    o-string -> raisedpos -> binary -> hex -> Unicode

    TODO: For students to complete.

    >>> ostring_to_unicode('o.\\noo\\n..')
    '⠓'
    >>> ostring_to_unicode('o.\\no.\\no.\\noo')
    '⣇'
    >>> ostring_to_unicode('oo\\noo\\noo\\noo')
    '⣿'
    >>> ostring_to_unicode('oo\\noo\\noo')
    '⠿'
    >>> ostring_to_unicode('..\\n..\\n..')
    '⠀'
    >>> ostring_to_unicode('a')
    'a'
    >>> ostring_to_unicode('\\n')
    '\\n'
    >>> ostring_to_unicode('o.\\no.\\n..\\n..')
    '⠃'
    '''
    #check if s is an ostring first
    if(is_ostring(s)):
        #by calling the functions above to transfer s to unicode step by step
        raisedops=ostring_to_raisedpos(s)
        binary=raisedpos_to_binary(raisedops)
        hex_number=binary_to_hex(binary)
        unicode=hex_to_unicode(hex_number)
        return unicode
    #return the initial value otherwise
    else:
        return s

if __name__ == '__main__':
    doctest.testmod()
