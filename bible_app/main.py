from bible_f_reading.bible_reading import *
from bible_to_dicts.dict_one import DictOne
from mem_mgmt.mem_mgmt import *
from bible_app.defn_api_handling.defn_api_handling import *
import kivy  # will implement eventually
import pickle  #  will implement eventually


def main():

    bible = read_bible(BIBLE_FILE)

    # bible lower cased and stripped of most punctuation
    cleaned_bible: [] = clean_bible(bible)  # needs work

    # bible -> book -> chapter -> verse -> words
    # {str: {int: {int: [str]}}}
    b = DictOne(cleaned_bible)
    print(b['revelation'][22])

    # word -> [word occurrence count, {[Strong's: Strong's occurrence count, [book, chapter, verse]]}]
    # {str: [int, {str: int}]}
    b_two = DictTwo(cleaned_bible)
    print(b_two['word'])

    # List of JSON of as many words in the bible as possible with definitions
    dictionary_json = read_def_json_f(DEFINITIONS_JSON_FILE)

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
