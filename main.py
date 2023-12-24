from file_reading.bible_reading import *
from bible_to_dicts.dict_one import DictOne
from bible_to_dicts.dict_two import DictTwo
from file_reading.vocab_dictionary import append_api_data, read_json_file

# with vocab dictionary, create Strong's Concordance to map to verses


def getpath(nested_dict, value, prepath=()):
    for k, v in nested_dict.items():
        path = prepath + (k,)
        if v == value: # found value
            return path
        elif hasattr(v, 'items'): # v is a dict
            p = getpath(v, value, path) # recursive call
            if p is not None:
                return p


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
    dictionary_json = read_json_file(f_name)



