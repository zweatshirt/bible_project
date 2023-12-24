from file_reading.bible_reading import *
from bible_to_dicts.dict_one import DictOne
from bible_to_dicts.dict_two import DictTwo
from file_reading.vocab_dictionary import append_api_data, read_json_file

if __name__ == '__main__':
    # read the bible and store as string
    bible = read_bible('kjv_strongs.txt')

    # list of each word in the bible
    # lower cased and rid of punctuation
    cleaned_words = clean_bible(bible)  # needs work

    # bible -> book -> chapter -> verse -> words
    # {str: {int: {int: [str]}}}
    b = DictOne(cleaned_words)

    # word -> [word occurrence count, {Strong's: Strong's occurrence count}]
    # {str: [int, {str: int}]}
    b_two = DictTwo(cleaned_words)

    print(b['genesis'][50])
    print(b.num_chapters(book := b['revelation']))


    # fix
    # print(b_two.get_word_strongs_tuple_for(last))

    # List of JSON of as many words in the bible as possible with definitions
    f_name = '/Users/zachjlinscott/PycharmProjects/bible_parser/dictionary.json'

    # def find_paths(nested_dict, value, prepath=()):
    #     for k, v in nested_dict.items():
    #         path = prepath + (k,)
    #         if v == value: # found value
    #             yield path
    #         elif hasattr(v, 'items'): # v is a dict
    #             yield from find_paths(v, value, path)
    #
    # print(*find_paths(dictionary, 'image/svg+xml'))

    dictionary_json = read_json_file(f_name)
