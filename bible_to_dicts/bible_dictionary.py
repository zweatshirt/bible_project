from collections import UserDict
from re import findall, sub


class BibleDictionary(UserDict):
    def __init__(self):
        super().__init__()

    def bible_to_dict(self, bible_lst: []) -> {}:
        pass

    # removes Strong's from a word and returns the word and Strong's
    @staticmethod
    def separate_strongs(word: str) -> (str, str):
        strongs = ''
        if '{' in word:
            strongs = tuple(findall('\{.*?\}', word))
            word = sub('\{.*?\}', '', word)
        return word, strongs

    # recursive function to get every single key in a nested dictionary
    def yield_all_keys(self, d: {}):
        for key, value in d.items():
            if type(value) is dict:
                yield from self.yield_all_keys(value)
            else:
                yield key, value

    def get_key_list(self):
        return [key for key in self.data.keys()]

    def get_value_list(self):
        return [val for val in self.data.values()]
