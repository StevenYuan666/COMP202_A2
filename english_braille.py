# COMP 202 A2 Part 5
# Author: Ye Yuan
# Student ID: 260921269
from text_to_braille import *

ENG_CAPITAL = '..\n..\n.o'
# You may want to define more global variables here
#define a new global variable include all digits
NUMBER='0123456789'

####################################################
# Here are two helper functions to help you get started

def two_letter_contractions(text):
    '''(str) -> str
    Process English text so that the two-letter contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.
    Provided to students. You should not edit it.

    >>> two_letter_contractions('chat')
    'âat'
    >>> two_letter_contractions('shed')
    'îë'
    >>> two_letter_contractions('shied')
    'îië'
    >>> two_letter_contractions('showed the neighbourhood where')
    'îœë ôe neiêbürhood ûïe'
    >>> two_letter_contractions('SHED')
    'ÎË'
    >>> two_letter_contractions('ShOwEd tHE NEIGHBOURHOOD Where') 
    'ÎŒË tHE NEIÊBÜRHOOD Ûïe'
    '''
    combos = ['ch', 'gh', 'sh', 'th', 'wh', 'ed', 'er', 'ou', 'ow']
    for i, c in enumerate(combos):
        text = text.replace(c, LETTERS[-1][i])
    for i, c in enumerate(combos):
        text = text.replace(c.upper(), LETTERS[-1][i].upper())
    for i, c in enumerate(combos):
        text = text.replace(c.capitalize(), LETTERS[-1][i].upper())

    return text


def whole_word_contractions(text):
    '''(str) -> str
    Process English text so that the full-word contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    If the full-word contraction appears within a word, 
    contract it. (e.g. 'and' in 'sand')

    Provided to students. You should not edit this function.

    >>> whole_word_contractions('with')
    'ù'
    >>> whole_word_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meow'
    >>> whole_word_contractions('With')
    'Ù'
    >>> whole_word_contractions('WITH')
    'Ù'
    >>> whole_word_contractions('wiTH')
    'wiTH'
    >>> whole_word_contractions('FOR thE Cat WITh THE purr And The meow')
    'É thE Cat WITh À purr Ç À meow'
    >>> whole_word_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> whole_word_contractions('wither')
    'ùer'
    '''
    # putting 'with' first so wither becomes with-er not wi-the-r
    words = ['with', 'and', 'for', 'the']
    fr_equivs = ['ù', 'ç', 'é', 'à', ]
    # lower case
    for i, w in enumerate(words):
        text = text.replace(w, fr_equivs[i])
    for i, w in enumerate(words):
        text = text.replace(w.upper(), fr_equivs[i].upper())
    for i, w in enumerate(words):
        text = text.replace(w.capitalize(), fr_equivs[i].upper())
    return text



####################################################
# These two incomplete helper functions are to help you get started

def convert_contractions(text):
    '''(str) -> str
    Convert English text so that both whole-word contractions
    and two-letter contractions are changed to the appropriate
    French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    Refer to the docstrings for whole_word_contractions and 
    two_letter_contractions for more info.

    >>> convert_contractions('with')
    'ù'
    >>> convert_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meœ'
    >>> convert_contractions('chat')
    'âat'
    >>> convert_contractions('wither')
    'ùï'
    >>> convert_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> convert_contractions('Showed The Neighbourhood Where')
    'Îœë À Neiêbürhood Ûïe'
    '''
    # ADD CODE HERE
    #replace the whole word contractions in the text, and store the value
    wholeword=whole_word_contractions(text)
    #replace the two letter contractions in the text, and store the value
    result=two_letter_contractions(wholeword)
    #return the final result
    return result


def convert_quotes(text):
    '''(str) -> str
    Convert the straight quotation mark into open/close quotations.
    >>> convert_quotes('"Hello"')
    '“Hello”'
    >>> convert_quotes('"Hi" and "Hello"')
    '“Hi” and “Hello”'
    >>> convert_quotes('"')
    '“'
    >>> convert_quotes('"""')
    '“”“'
    >>> convert_quotes('" "o" "i" "')
    '“ ”o“ ”i“ ”'
    '''
    # ADD CODE HERE
    #create a new variable to count the occurences of "
    count=0
    #use the for loop to find the "
    for index,char in enumerate(text):
        #check if " should be replaced by open quotation mark
        if (char=='"' and count%2==0):
            #mutate the value of count
            count+=1
            #replace the " by “
            intermediate=text[index]
            text=text[:index]+intermediate.replace('"','“')+text[index+1:]
        #check if " should be replaced by closed quotation mark
        elif(char=='"' and count%2==1):
            #mutate the value of count
            count+=1
            #replace the " by ”
            intermediate=text[index]
            text=text[:index]+intermediate.replace('"','”')+text[index+1:]
    #return the edited text
    return text
        
####################################################
# Put your own helper functions here!
def sub_number_begin(text):
    '''
    (str) -> str
    mark '#' before the number
    >>> sub_number_begin('202')
    '#202'
    >>> sub_number_begin('2')
    '#2'
    >>> sub_number_begin('COMP 202')
    'COMP #202'
    >>> sub_number_begin('COMP 202 AND COMP 250')
    'COMP #202 AND COMP #250'
    >>> sub_number_begin('COMP 202 AND COMP 250 AND COMP 273')
    'COMP #202 AND COMP #250 AND COMP #273'
    >>> sub_number_begin('COMP,202')
    'COMP,#202'
    '''
    #add a space to the input text first
    text=' '+text
    #use the for loop to find every digits
    for index in range(1,len(text)):
        #create a variable to store the condition to add # mark
        condition=text[index] in NUMBER and (text[index-1]==' ' or text[index-1] in PUNCTUATION)
        #check the condition
        if(condition):
            #insert the # in the right position
            remaining=text[index:]
            before_part=text[:index]
            text=before_part+'#'+remaining
    #remove the first space
    text=text[1:]
    #return the edited text
    return text

def sub_number_end(text):
    '''
    (str) -> str
    mark '¥' before the number
    >>> sub_number_end('#202')
    '#202¥'
    >>> sub_number_end('#2')
    '#2¥'
    >>> sub_number_end('COMP #202')
    'COMP #202¥'
    >>> sub_number_end('COMP #202 AND COMP #250')
    'COMP #202¥ AND COMP #250¥'
    >>> sub_number_end('#202 COMP AND #250 COMP')
    '#202¥ COMP AND #250¥ COMP'
    >>> sub_number_end('COMP #202 AND COMP #250 AND COMP #273')
    'COMP #202¥ AND COMP #250¥ AND COMP #273¥'
    >>> sub_number_end('COMP #202,')
    'COMP #202¥,'
    '''
    #if the last character in the text is a digit, add ¥ after it
    if(text[-1] in NUMBER):
        text=text+'¥'
    #use for loop to find every digit
    for index in range(len(text)):
        #create a variable to store the condition to add ¥ mark
        condition=((text[index]==' ' or text[index] in PUNCTUATION) and text[index-1] in NUMBER)
        #check the condition
        if(condition):
            #insert the ¥ in the right position
            remaining=text[index:]
            before_part=text[:index]
            text=before_part+'¥'+remaining
    #return the edited text
    return text
def sub_parentheses(text):
    '''
    (str) -> str
    change the parentheses in the text to quotation marks
    >>> sub_parentheses('(')
    '"'
    >>> sub_parentheses(')')
    '"'
    >>> sub_parentheses('(hi)')
    '"hi"'
    >>> sub_parentheses('(Parenthetical)')
    '"Parenthetical"'
    '''
    #replace the ( by "
    text=text.replace('(','"')
    #replace the ) by "
    text=text.replace(')','"')
    #return the edited text
    return text

def sub_quotation_question(unicode):
    '''
    (str) -> str
    change the french braille mark to english braille mark
    >>> sub_quotation_question('“”')
    '⠦⠴'
    >>> sub_quotation_question('⠢')
    '⠦'
    '''
    #replace the “ by ⠦
    unicode=unicode.replace('“','⠦')
    #replace the “ by ⠴
    unicode=unicode.replace('”','⠴')
    #replace the ⠢ by ⠦
    unicode=unicode.replace('⠢','⠦')
    #return the edited unicode
    return unicode

def sub_numbers(unicode):
    '''
    (str) -> str
    change the special number mark to english braille number mark
    >>> sub_numbers('#')
    '⠼'
    >>> sub_numbers('¥')
    '⠰'
    >>> sub_numbers('⠼')
    ''
    '''
    #replace ¥ by ⠰
    unicode = unicode.replace('¥','⠰')
    #replace ⠼ by ''
    unicode = unicode.replace('⠼','')
    #replace # by ⠼
    unicode = unicode.replace('#','⠼')
    #return the unicode
    return unicode
####################################################

def english_text_to_braille(text):
    '''(str) -> str
    Convert text to English Braille. Text could contain new lines.

    This is a big problem, so think through how you will break it up
    into smaller parts and helper functions.
    Hints:
        - you'll want to call text_to_braille
        - you can alter the text that goes into text_to_braille
        - you can alter the text that comes out of text_to_braille
        - you shouldn't have to manually enter the Braille for 'and', 'ch', etc

    You are expected to write helper functions for this, and provide
    docstrings for them with comprehensive tests.

    >>> english_text_to_braille('202') # numbers
    '⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('2') # single digit
    '⠼⠃⠰'
    >>> english_text_to_braille('COMP') # all caps
    '⠠⠠⠉⠕⠍⠏'
    >>> english_text_to_braille('COMP 202') # combining number + all caps
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('and')
    '⠯'
    >>> english_text_to_braille('and And AND aNd')
    '⠯ ⠠⠯ ⠠⠯ ⠁⠠⠝⠙'
    >>> english_text_to_braille('chat that the with')
    '⠡⠁⠞ ⠹⠁⠞ ⠷ ⠾'
    >>> english_text_to_braille('hi?')
    '⠓⠊⠦'
    >>> english_text_to_braille('(hi)')
    '⠶⠓⠊⠶'
    >>> english_text_to_braille('"hi"')
    '⠦⠓⠊⠴'
    >>> english_text_to_braille('COMP 202 AND COMP 250')
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰ ⠠⠯ ⠠⠠⠉⠕⠍⠏ ⠼⠃⠑⠚⠰'
    >>> english_text_to_braille('For shapes with colour?')
    '⠠⠿ ⠩⠁⠏⠑⠎ ⠾ ⠉⠕⠇⠳⠗⠦'
    >>> english_text_to_braille('(Parenthetical)\\n\\n"Quotation"')
    '⠶⠠⠏⠁⠗⠑⠝⠷⠞⠊⠉⠁⠇⠶\\n\\n⠦⠠⠟⠥⠕⠞⠁⠞⠊⠕⠝⠴'
    >>> english_text_to_braille('... and, word.')
    '⠲⠲⠲ ⠯⠂ ⠺⠕⠗⠙⠲'
    '''
    # Here's a line we're giving you to get started: change text so the
    # contractions become the French accented letter that they correspond to
    text = convert_contractions(text)
    # You may want to put code after this comment. You can also delete this comment.
    #add numbers begin mark
    text = sub_number_begin(text)
    #add numbers end mark
    text = sub_number_end(text)
    #convert "" to “”
    text = convert_quotes(text)
    #convert parentheses to quotation marks
    text = sub_parentheses(text)
    # Run the text through the French Braille translator
    text = text_to_braille(text)
    # You may want to put code after this comment. You can also delete this comment.
    #replace open/closed quotation mark and question mark by right braille unicode
    text = sub_quotation_question(text)
    # replace the French capital with the English capital
    text = text.replace(ostring_to_unicode(CAPITAL), ostring_to_unicode('..\n..\n.o'))
    # You may want to put code after this comment. You can also delete this comment.
    #sub the numbers begin and end mark to right braille unicode
    text=sub_numbers(text)
    #return the final text
    return text


def english_file_to_braille(fname):
    '''(str) -> NoneType
    Given English text in a file with name fname in folder tests/,
    convert it into English Braille in Unicode.
    Save the result to fname + "_eng_braille".
    Provided to students. You shouldn't edit this function.
    >>> english_file_to_braille('test4.txt')
    >>> file_diff('tests/test4_eng_braille.txt', 'tests/expected4.txt')
    True
    >>> english_file_to_braille('test5.txt')
    >>> file_diff('tests/test5_eng_braille.txt', 'tests/expected5.txt')
    True
    >>> english_file_to_braille('test6.txt')
    >>> file_diff('tests/test6_eng_braille.txt', 'tests/expected6.txt')
    True
    '''  
    file_to_braille(fname, english_text_to_braille, "eng_braille")


if __name__ == '__main__':
    doctest.testmod()    # you may want to comment/uncomment along the way
    # and add tests down here
