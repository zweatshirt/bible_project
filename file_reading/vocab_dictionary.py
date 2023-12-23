from json import loads
import requests
from time import sleep

from bible_to_dicts.dict_two import DictTwo


def get_api_data(word: str, sleep_time, sleep_count=0) -> str:  # returns JSON
    try:
        res = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/' + word, timeout=5)
        return res.text
    except requests.exceptions.HTTPError:
        sleep_count += 1
        sleep(sleep_time)
        get_api_data(word, sleep_time, sleep_count)


def append_api_data(file_name: str, d: DictTwo or []):
    with open(file_name, 'a', encoding='utf-8') as f:
        for k in d:
            json_data = get_api_data(k, 60)
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
        return [loads(line) for line in f if line.strip()]
