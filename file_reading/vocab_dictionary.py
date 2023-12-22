from requests import get
from time import sleep

from bible_to_structs.bible_dict_two import DictTwo


def get_api_data(word: str):  # returns JSON
    return get('https://api.dictionaryapi.dev/api/v2/entries/en/' + word)


def write_api_data(file_name: str, d: DictTwo):
    j = 0
    with open(file_name, 'w', encoding='utf-8') as f:
        for val in d.dict.keys():
            json_data = get_api_data(val)
            print(json_data.text)
            f.write("{}\n".format(json_data.text))
            j += 1
            if j % 100 == 0:
                sleep(10)


def extract_file_lines(file_name: str) -> []:
    with open(file_name, 'r', encoding='utf-8') as f:
        lst = [line.strip() for line in f]

    return lst
