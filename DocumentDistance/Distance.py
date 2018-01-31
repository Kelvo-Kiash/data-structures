import math
import string
import sys


l = []
l.c
def read_file(filename):
    try:
        fp = open(filename)
        L = fp.readlines()

    except IOError:
        print "Error opening the file", filename
        sys.exit()

    return L

def get_words_from_string(line):
    """
    Return a list of the words in the given input string,
    converting each word to lower-case.

    Input:  line (a string)
    Output: a list of strings 
              (each string is a sequence of alphanumeric characters)
    """
    line = line.translate(translation_table)
    word_list = line.split()
    return word_list


def get_words_from_line_list(L):
    """
    
    
    [description]
    
    Arguments:
        L {[type]} -- [description]
    """ 
    word_list = []
    for line in L:
        words_in_line = get_words_from_string(line)
        word_list.extend(words_in_line)
    return word_list

l1 = min(len(string.uppercase), len(string.lowercase))

translation_table = string.maketrans(string.punctuation+string.uppercase[:11],
" "*len(string.punctuation)+string.lowercase[:11])



def count_frequency(word_list):
    """
    Return a list giving pairs of form: (word,frequency)
    """
    D = {}
    for new_word in word_list:
        if D.has_key(new_word):
            D[new_word] = D[new_word]+1
        else:
            D[new_word] = 1
    return D.items()

def merge_sort(A):
    n = len(A)
    if n == 1:
        return A
    mid = n//2
    L = merge_sort(A[:mid])
    R = merge_sort(A[mid:])
    return merge(L, R)





    