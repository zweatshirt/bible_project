import string

BIBLE_FILE = 'bible_app/data_files/kjv_strongs.txt'


def read_file(f_name: str) -> str:
    with open(f_name, encoding='utf-8') as file:
        bible_data = file.read()
    return bible_data


def clean_bible(bible: str) -> []:
    replace_str = string.punctuation\
        .replace('{', '') \
        .replace('}', '') \
        .replace('-', '')\
        .replace('(', '')\
        .replace(')', '')
    # return bible.translate(str.maketrans('', '', replace_str)).lower().split()
    return bible.translate(str.maketrans('', '', replace_str)).lower().split()
