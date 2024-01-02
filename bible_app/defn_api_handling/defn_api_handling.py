from json import loads
import requests
from time import sleep
from bible_app.bible_f_reading.bible_reading import read_file
from bible_app.bible_to_dicts.dict_two import DictTwo

"""
TODO:
    The functions in this file have been modified but need to be properly tested.
"""

DICTIONARY_API = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
DEFINITIONS_JSON_FILE = 'bible_app/data_files/dictionary.json'
LEFTOVER_WORDS_FILE = 'bible_app/data_files/unreadable_by_api.txt'  # words API could not get definitions for


def append_api_data(d: DictTwo or []):
    """gets API data in the form of a json object and appends it to a .json file"""
    with open(DEFINITIONS_JSON_FILE, 'a', encoding='utf-8') as f:
        for k in d:
            json_data = get_api_data(k, 60)
            if json_data:
                print(json_data)
                f.write("{}\n".format(json_data))


def get_api_data(word: str, sleep_time, sleep_count=0) -> str:
    """grabs definition of a given word from the API"""
    word = word.lower()  # hmmmm
    try:
        word = word.lower()
        res = requests.get(DICTIONARY_API + word, timeout=5)
        return res.text if 'title' not in res.text else no_definition_for(word)
    except requests.exceptions.HTTPError:
        if sleep_count == 5:
            no_definition_for(word)
            raise Exception(
                'Unable to access {} for {}'.format(DICTIONARY_API, word)
            )
        sleep_count += 1
        sleep(sleep_time)
        get_api_data(word, sleep_time, sleep_count)


def no_definition_for(word: str):
    """
    if there are no definitions for a word we want to save the word for later attempts.
    should probably be rewritten so it doesn't open the file every time an append is needed.
    """
    f_append(LEFTOVER_WORDS_FILE, word)
    return None


def f_append(f_name, vals):
    """basic file append function"""
    with open(f_name, 'a', encoding='utf-8') as f:
        for v in vals:
            f.write(v)


def read_def_json_f(f_name) -> []:
    """returns list of all json objs from a file"""
    with open(f_name, 'r') as f:
        return [loads(line) for line in f if line.strip()]


def compare_definitions_to_dict(f_name, b_two: {}):
    # dictionary_json = read_def_json_f(DEFINITIONS_JSON_FILE)
    f = read_file(f_name)
    
    # if file == DEFINITIONNS_JSON_FILE:  # implement

    if f_name == LEFTOVER_WORDS_FILE:
        for i in f.split():
        if i not in b_two.keys():
            print(i)
    



def delete_leftover_duplicates():
    with open(LEFTOVER_WORDS_FILE, 'r+', encoding='utf-8') as f:
        no_dupes = set(f.readlines())
        f.seek(0)
        f.truncate()
        [f.write("{}".format(line)) for line in no_dupes]


