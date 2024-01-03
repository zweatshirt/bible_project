from bible_f_reading.bible_reading import *
from bible_to_dicts.dict_one import DictOne
from mem_mgmt.mem_mgmt import *
from bible_app.defn_api_handling.defn_api_handling import *
import pickle  #  will implement eventually

# TODO:
# Change bible from undercase to normal uppercase
# but in doing so, allow undercase searching
# add the - back into the punctuation
# implement a NLP library for verse searching
# do ignore lowercase for the dictionary?
# lots to do...

# some words are not getting added correctly because of parentheses after the word
# but changing the parentheses to spaces in the text causes a crash


def main():

    bible = read_file(BIBLE_FILE)

    # bible lower cased and stripped of most punctuation
    cleaned_bible: [] = clean_bible(bible)  # needs work

    # bible -> book -> chapter -> verse -> words
    # {str: {int: {int: [str]}}}
    b = DictOne(cleaned_bible)
    # print(b)
    print(b['acts'][4][36])
    #
    # word -> [word occurrence count, {[Strong's: Strong's occurrence count, [book, chapter, verse]]}]
    # # {str: [int, {str: int}]}
    b_two = DictTwo(cleaned_bible)
    print(b_two['word'])

    # List of JSON of as many words in the bible as possible with definitions
    dictionary_json = read_def_json_f(DEFINITIONS_JSON_FILE)
    unreadable = read_file(LEFTOVER_WORDS_FILE)

    delete_leftover_duplicates(LEFTOVER_WORDS_FILE)

    compare_definitions_to_dict(DEFINITIONS_JSON_FILE, b_two)
    compare_definitions_to_dict(LEFTOVER_WORDS_FILE, b_two)

    process = psutil.Process()
    mem_size(process)


if __name__ == '__main__':
    main()

# with vocab dictionary, create Strong's Concordance to map to verses
# not working, I'm not sure why
# def getpath(nested_dict, value, prepath=()):
#     for k, v in nested_dict.items():
#         path = prepath + (k,)
#         if v == value:  # found value
#             return path
#         elif hasattr(v, 'items'):  # v is a dict
#             p = getpath(v, value, path)  # recursive call
#             if p is not None:
#                 return p
