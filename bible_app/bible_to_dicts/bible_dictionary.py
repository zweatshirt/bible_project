from collections import UserDict
from re import findall, sub


class BibleDictionary(UserDict):
    def __init__(self):
        super().__init__()

    # refactor: looks awful
    def _is_ch_or_book(self, bible_lst, i, book, word):
        if i != 0 and bible_lst[i - 1] != book:
            if not ((bible_lst[i - 1] == 'chapter' or bible_lst[i - 1] == 'psalm') and word.isdigit()):
                if not ((word == 'chapter' or word == 'psalm') and bible_lst[i + 1].isdigit()):
                    return False
        return True

    def _book_name_helper(self, bible_lst, i):
        if bible_lst[i - 2].isdigit():  # in cases where the book name starts with a num e.g. 1 Samuel
            return bible_lst[i - 2] + " " + bible_lst[i - 1]
        return bible_lst[i - 1]

    def bible_to_dict(self, bible_lst: []) -> {}:
        """
            Method intended to initialize the dictionary.
        """
        pass

    @staticmethod
    def separate_strongs(word: str) -> (str, str):
        """Removes Strong's from a word and returns the word and Strong's"""
        strongs = ''
        if '{' in word:
            strongs = tuple(findall('\{.*?\}', word))
            word = sub('\{.*?\}', '', word)
        return word, strongs

    def yield_all_keys(self, d: {}):
        """recursive function to get every single key in a nested dictionary"""
        for key, value in d.items():
            if type(value) is dict:
                yield from self.yield_all_keys(value)
            else:
                yield key, value

    def get_key_list(self):
        """
            Returns list of keys.
            NOT recursive for nested dictionary cases.
            Slow, but helpful in certain use cases.
        """
        return [key for key in self.data.keys()]

    def get_value_list(self):
        """
            Returns list of values.
            NOT recursive for nested dictionary cases.
            Slow, but helpful in certain use cases.
        """
        return [self.data.values()]
