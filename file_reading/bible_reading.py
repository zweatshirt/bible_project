import string


def read_bible(f_name: str) -> str:
    with open(f_name, encoding='utf-8') as file:
        bible_data = file.read()
    return bible_data


def clean_bible(bible: str) -> []:
    # strip = string.punctuation.replace('{', '').replace('}', '').replace('(', '').replace(')', '')
    return bible.lower().split()