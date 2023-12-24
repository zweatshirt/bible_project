from bible_to_dicts.bible_dictionary import BibleDictionary


# bible -> book -> chapter -> verse -> words
class DictOne(BibleDictionary):
    def __init__(self, bible_lst: []):
        super().__init__()
        self.data = self.bible_to_dict(bible_lst)

    @staticmethod
    def clean_verse(verse: []):
        return ' '.join([word[0] for word in verse])

    @staticmethod
    def pprint_verse(verse: []):
        print(DictOne.clean_verse(verse))

    # write
    def pprint_chapter(self, chapter: {}):
        for key in self.yield_all_keys(chapter):
            pass

    @staticmethod
    def num_chapters(dct: {}):
        return len(dct)

    def bible_to_dict(self, b_lst: []):
        bible_dict = {}
        book, chapter, verse_num = None, None, None
        verse = []

        for i, word in enumerate(b_lst):
            word, strongs = DictOne.separate_strongs(word)

            if (word == 'chapter' or word == 'psalm') and b_lst[i + 1].isdigit():
                # reset verse for every new chapter
                verse = []
                chapter = int(b_lst[i + 1])
                # if chapter name is 1, we can grab the book name one index behind
                if chapter == 1:
                    book = self.__book_name_helper(b_lst, i)
                    # add book to bible_dict
                self.__add_book_to_dict(bible_dict, book)
                self.__add_ch_to_dict(bible_dict, book, chapter)

            # final word of bible case
            if i == len(b_lst) - 1:
                verse.append((word, strongs))
                break

            # look at any word that isn't a chapter, psalm, or book title
            if not self.__ch_or_book(b_lst, i, book, word):
                if word.isdigit():
                    verse_num = int(word)
                    # reset verse list for every new verse num
                    verse = []
                else:
                    verse.append((word, strongs))

                # get rid of occurrences where book names end up at end of verse
                if self.__b_name_at_end(b_lst, i):
                    verse.pop()

                self.__add_verse_to_dict(bible_dict, book, chapter, verse_num, verse)

        return bible_dict

    ''' helper methods for bible_to_dict() '''

    # in the event that the next book name
    # is appended to the end of the last chapter
    # and verse of the current book
    def __add_book_to_dict(self, bible_dict, book):
        if book and book not in bible_dict:
            bible_dict[book] = {}

    def __add_ch_to_dict(self, bible_dict, book, chapter):
        if book and chapter and chapter not in bible_dict[book]:
            bible_dict[book][chapter] = {}

    def __add_verse_to_dict(self, bible_dict, book, chapter, verse_num, verse):
        if verse_num not in bible_dict[book][chapter]:
            bible_dict[book][chapter][verse_num] = verse

    def __b_name_at_end(self, bible_lst, i):
        if i < len(bible_lst) - 2:
            if (bible_lst[i + 1] + " " + bible_lst[i + 2] == 'chapter 1' or
                    bible_lst[i + 1] + " " + bible_lst[i + 2] == 'psalm 1'):
                return True
        return False

    def __ch_or_book(self, bible_lst, i, book, word):
        if i != 0 and bible_lst[i - 1] != book:
            if not ((bible_lst[i - 1] == 'chapter' or bible_lst[i - 1] == 'psalm') and word.isdigit()):
                if not ((word == 'chapter' or word == 'psalm') and bible_lst[i + 1].isdigit()):
                    return False
        return True

    # grabs book name
    def __book_name_helper(self, bible_lst, i):
        if bible_lst[i - 2].isdigit():  # in cases where the book name starts with a num e.g. 1 Samuel
            return bible_lst[i - 2] + " " + bible_lst[i - 1]
        else:
            return bible_lst[i - 1]

    '''end'''
