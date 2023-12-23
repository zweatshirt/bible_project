# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from file_reading.bible_reading import *
from bible_to_structs.bible_dict_one import DictOne
from bible_to_structs.bible_dict_two import DictTwo
from file_reading.vocab_dictionary import append_api_data, read_json_file

if __name__ == '__main__':
    bible = read_bible('kjv_strongs.txt')

    cleaned_words = clean_bible(bible)
    b = DictOne(cleaned_words)
    # print(bible_dct.dict['zephaniah'][3][20])
    # print(len(bible_dct.dict['zephaniah'][3][21]))
    b_two = DictTwo(cleaned_words)


    json_dct = read_json_file('/Users/zachjlinscott/PycharmProjects/bible_parser/dictionary.json')
    # go through b_two to check if the word is in json_dct
    # if not try to use API for it again

    # lst = [i[0]['word'] for i in json_dct]


