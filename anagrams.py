#! /usr/bin/env python 
#
import sys
import argparse
import unicodedata
from collections import defaultdict

def get_letters(category='Ll'):
    """
    Shamelessly taken from StackOverflow: https://stackoverflow.com/a/14246025
    """
    unicode_chars = []
    for c in map(chr, range(sys.maxunicode + 1)):
        tmp_category = unicodedata.category(c) 
        if tmp_category == category:
            unicode_chars.append(c)
    return unicode_chars

def get_primes(n):
    """
    Function to get nth prime... I know, a bit lazy. This could be
    an actual function to *compute* primes, but let's just read them from
    a list downloaded from the internet:
    https://www.mathsisfun.com/numbers/prime-number-lists.html
    """
    primes = []
    for line in open('primes-to-100k.txt'):
        primes.append(int(line.strip()))
        if len(primes) == n:
            return primes

# Create a mapping for all lowercase unicode, just in case.
_letters = get_letters()
_letter_dict = {key:p for key,p in zip(_letters,get_primes(len(_letters)))}

def get_int(word):
    """
    Function to map input string, single word, to integer. The int is formed
    from multiplying primes. Returns None if non lower case letter is found.
    """
    prime_int = 1
    for letter in word:
        try:
            prime_int *= _letter_dict[letter]
        except KeyError as e:
            # TODO: create logging error for these
            # print('+++ ',letter)
            return None        
    return prime_int


if __name__ == '__main__':

    # Parse the dictionary and encoding from command line args
    parser = argparse.ArgumentParser(description='Print anagrams.')
    parser.add_argument('-d','--dictionary', type=str, required=False,
                        default='/usr/share/dict/words',
                        help='an integer for the accumulator')
    parser.add_argument('-e','--encoding', type=str, default='utf-8',
                        required=False,
                        help='Some dictionary files use different encodings.')
    parser.add_argument('-w','--min_word_len', type=int, default=4,
                        required=False,
                        help='Minimun length on a word to consider.')

    args = parser.parse_args()

    # Store anagrams in dict
    anagrams = defaultdict(list)
    # Read through dictionary
    try:
        for word in open(args.dictionary, encoding=args.encoding):
            word = word.strip()
            p_int = get_int(word)
            if p_int is not None:
                anagrams[p_int].append(word)
    except UnicodeDecodeError as e:
        print('Problem decoding dictionary. Maybe try option "-e iso-8859-1"')
        sys.exit(1)
    # Now bin anagrams based on word length
    anagram_word_len = defaultdict(list)
    for key, words in anagrams.items():
        word_len = len(words[0])
        anagram_word_len[word_len].append(words)
    # Constrain output to minimum word length and number of anagrams that are
    # greater or equal to the word length.
    for word_len, anagrams in anagram_word_len.items():
        if word_len >= args.min_word_len:
            for words in anagrams:
                if len(words) >= word_len:
                    print(', '.join(words))
