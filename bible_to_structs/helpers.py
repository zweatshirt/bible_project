from re import findall, sub


def remove_strongs(word: str) -> (str, str):
    strongs = ''
    if '{' or '(' in word:
        strongs = tuple(findall('\{.*?\}', word))
        word = sub('\{.*?\}', '', word)
    return word, strongs


def get_keys(d: {}):
    for key, value in d.items():
        yield key
        if isinstance(value, d):
            yield from get_keys(value)
