# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from file_reading.bible_reading import *
from bible_to_structs.bible_dict_one import DictOne
from bible_to_structs.bible_dict_two import DictTwo
from file_reading.vocab_dictionary import write_api_data


if __name__ == '__main__':
    bible = read_bible('kjv_strongs.txt')

    cleaned_words = clean_bible(bible)
    b = DictOne(cleaned_words)
    # print(bible_dct.dict['zephaniah'][3][20])
    # print(len(bible_dct.dict['zephaniah'][3][21]))
    b_two = DictTwo(cleaned_words)

    # write_api_data('/Users/zachjlinscott/PycharmProjects/bible_parser/dictionary.json', b_two)

# reads  the processed comments from comments.txt and returns them in a list


# writes the comments and sentiment of the comments to a new file.


# lst = [get('https://api.dictionaryapi.dev/api/v2/entries/en/' + i) for i in b_two.dict.keys()]

# print(lst)
