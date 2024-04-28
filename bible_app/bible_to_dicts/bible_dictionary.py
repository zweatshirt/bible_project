from collections import UserDict
from re import findall, sub


class BibleDictionary(UserDict):
    def __init__(self):
        super().__init__()

    # refactor: looks awful
    def _is_book(self, book, word, word_after):
        ch = ['Chapter', 'Psalm']
        return True if word == book and word_after in ch else False
        # if ((bible_lst[i - 1] == 'Chapter'.casefold() or bible_lst[i - 1].casefold() == 'Psalm'.casefold()) and word.isdigit()):
        #     return True
    
    def _is_ch(self, word, word_after):
        ch = ['Chapter', 'Psalm']
        return True if word in ch and word_after.isdigit() else False
    

    def _book_name_helper(self, bible_lst, i):
        """Grabs the book name (there are 66 books in the KJV)."""
        if bible_lst[i - 2].isdigit():  # in cases where the book name starts with a num e.g. 1 Samuel
            return bible_lst[i - 2] + " " + bible_lst[i - 1]
        return bible_lst[i - 1]

    def bible_to_dict(self, bible_lst):
        """Initialize the underlying UserDict dictionary."""
        pass

    @staticmethod
    def separate_strongs(word):
        """Removes Strong's from a word and returns the word and Strong's"""
        strongs = ''
        if '{' in word:
            strongs = tuple(findall('\{.*?\}', word))
            word = sub('\{.*?\}', '', word)
        return word, strongs

    def yield_all_keys(self, d):
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
