# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re
from file_reading.bible_reading import *
from bible_to_structs.bible_dict_one import PrimaryBibleDict
from bible_to_structs.bible_dict_two import WordToStrongsDict

# bible -> book -> chapter -> verse

# change this to search a "words to strong dict" and "word counter" dict of the overall bible list


def get_keys(d: {}):
    for key, value in d.items():
        yield key
        if isinstance(value, d):
            yield from get_keys(value)


# map strongs to words
def strongs_dict():
    ...


if __name__ == '__main__':
    bible = read_bible('kjv_strongs.txt')

    cleaned_words = clean_bible(bible)
    bible_dct = PrimaryBibleDict(cleaned_words)
    print(bible_dct.dict['genesis'][1])
    print(bible_dct.dict['revelation'][22])
    # print(bible_dct.dict['zephaniah'][3][20])
    # print(len(bible_dct.dict['zephaniah'][3][21]))
    # Specifically has num of occurences of a word and num of occurences of Strongs
    bible_dct_two = WordToStrongsDict(cleaned_words)


    # print(repr(bible_dct))

