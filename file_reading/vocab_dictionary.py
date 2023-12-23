from json import loads
from requests import get
from time import sleep

from bible_to_structs.bible_dict_two import DictTwo


# extremely buggy, needs to be rewritten
def get_api_data(word: str) -> str:  # returns JSON
    res = get('https://api.dictionaryapi.dev/api/v2/entries/en/' + word)
    print(res.text)
    if res.status_code == 429 or 'Too many requests' in res.text:
        sleep(90)
        get_api_data(word)
    return res.text


def append_api_data(file_name: str, d: DictTwo or []):
    with open(file_name, 'a', encoding='utf-8') as f:
        for k in d:
            json_data = get_api_data(k)
            if 'No Definitions Found' not in json_data[10:31]:
                print(json_data)
                f.write("{}\n".format(json_data))


def extract_file_lines(file_name: str) -> []:
    with open(file_name, 'r', encoding='utf-8') as f:
        lst = [line.strip() for line in f]

    return lst


def read_json_file(file_name) -> []:
    json_data = []
    with open(file_name, 'r') as f:
        for line in f:
            if line.strip():
                json_data.append(loads(line))
    return json_data
