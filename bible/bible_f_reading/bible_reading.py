import string

BIBLE_FILE = 'bible/data_files/kjv_strongs.txt'


def read_file(f_name: str) -> str:
    with open(f_name, 'r', encoding='utf-8') as file:
        bible_data = file.read()
    return bible_data


def clean_bible(bible: str) -> []:
    punc_to_keep = str.maketrans('', '', '{}-')
    replace_str = string.punctuation.translate(punc_to_keep)
    new = ''
    for i, letter in enumerate(bible):

        if letter in replace_str:
            if bible[i] == '(' and bible[i - 1] != '{':
                new += ' ( '
            elif bible[i] == ')' and bible[i + 1] != '}':
                new += ' ) '
            else:
                if bible[i] == '(' or bible[i] == ')':
                    new += bible[i]
                else:
                    new += ' ' + bible[i] + ' '
        else:
            new += bible[i]
    return new.split()




    # return bible.translate(str.maketrans('', '', replace_str)).lower().split()
