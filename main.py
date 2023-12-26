from file_reading.bible_reading import *
from bible_to_dicts.dict_one import DictOne
from bible_to_dicts.dict_two import DictTwo
from mem_mgmt.mem_mgmt import *
from file_reading.vocab_dictionary import append_api_data, read_json_file


def main():
    # read the bible and store as string
    bible = read_bible('data_files/kjv_strongs.txt')

    # list of each word in the bible
    # lower cased and rid of punctuation
    cleaned_words = clean_bible(bible)  # needs work

    # bible -> book -> chapter -> verse -> words
    # {str: {int: {int: [str]}}}
    b = DictOne(cleaned_words)
    print(b['revelation'][22])

    # word -> [word occurrence count, {[Strong's: Strong's occurrence count, [book, chapter, verse]]}]
    # {str: [int, {str: int}]}
    b_two = DictTwo(cleaned_words)
    print(b_two['word'])

    # print(b.num_chapters(book := b['revelation']))

    # List of JSON of as many words in the bible as possible with definitions
    f_name = 'data_files/dictionary.json'
    dictionary_json = read_json_file(f_name)

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
