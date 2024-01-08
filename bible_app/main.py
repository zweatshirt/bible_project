from bible_f_reading.bible_reading import *
from bible_to_dicts.dict_one import DictOne
from mem_mgmt.mem_mgmt import *
from bible_app.defn_api_handling.defn_api_handling import *
import pickle  # will implement eventually


# TODO:
# Complete the implementation of the dictionary. About 5000 words to find definitions for.
# Unfortunately this probably means using a different API.
# Add NLP phrase searching.


def main():
    bible = read_file(BIBLE_FILE)

    # bible lower cased and stripped of most punctuation
    cleaned_bible: [] = clean_bible(bible)  # needs work

    # bible -> book -> chapter -> verse -> words
    # {str: {int: {int: [str]}}}
    b = DictOne(cleaned_bible)
    print(b['Revelation'][22][21])

    # word -> [word occurrence count, {[Strong's: Strong's occurrence count, [book, chapter, verse]]}]
    # # {str: [int, {str: int}]}
    b_two = DictTwo(cleaned_bible)
    print(b_two['Word'])

    # List of JSON of as many words in the bible as possible with definitions
    dictionary_json = read_def_json_f(DEFINITIONS_JSON_FILE)
    unreadable = read_file(LEFTOVER_WORDS_FILE)  # these words can't be understood by the API

    delete_leftover_duplicates(LEFTOVER_WORDS_FILE)  # file cleaner function

    # the elements in this list need to be fed to the API.
    to_append_to_defns = dict_vals_not_in_defns(DEFINITIONS_JSON_FILE, b_two)
    for i in to_append_to_defns:
        pass
    
    # monitor process size. Currently around .4 GB which is a lot.
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
