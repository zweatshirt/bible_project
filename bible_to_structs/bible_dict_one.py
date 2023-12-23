from bible_to_structs.bible_dict_parent import *


# from bible_to_structs.helpers import remove_strongs, get_keys


# bible -> book -> chapter -> verse -> words
class DictOne(BibleDictionary):
    def __init__(self, bible_lst: []):
        super().__init__()
        self.data = self.bible_to_dict(bible_lst)

    def bible_to_dict(self, bible_lst: []):
        bible_dict = {}
        book = None
        chapter = None
        verse_num = None
        verse = []

        len_words = len(bible_lst)

        for i, word in enumerate(bible_lst):

            word, strongs = self.remove_strongs(word)

            if (word == 'chapter' or word == 'psalm') and bible_lst[i + 1].isdigit():

                # reset verse for every new chapter
                verse = []

                # get chapter name
                chapter = int(bible_lst[i + 1])

                # if chapter name is 1, we can grab the book name one index behind
                if chapter == 1:

                    # get book name
                    if bible_lst[i - 2].isdigit():  # in cases where the book name starts with a num e.g. 1 Samuel
                        book = bible_lst[i - 2] + " " + bible_lst[i - 1]
                    else:
                        book = bible_lst[i - 1]

                    # add book to bible_dict
                    if book and book not in bible_dict:
                        bible_dict[book] = {}

                # add chapter to bible_dict[book]
                if book and chapter and chapter not in bible_dict[book]:
                    bible_dict[book][chapter] = {}

            # final word of bible case
            if i == len_words - 1:
                word, strongs = self.remove_strongs(word)
                verse.append(word)
                break

            # look at anything that isn't a chapter, psalm, or book title
            if i != 0 and bible_lst[i - 1] != book:

                if not ((bible_lst[i - 1] == 'chapter' or bible_lst[i - 1] == 'psalm') and bible_lst[i].isdigit()):
                    if not ((word == 'chapter' or word == 'psalm') and bible_lst[i + 1].isdigit()):

                        # if word is a verse num
                        if word.isdigit():
                            verse_num = int(word)
                            # reset verse list for every new verse num
                            verse = []
                        else:
                            # add word to verse list
                            verse.append(word)

                        # get rid of occurrences where book names end up at end of verse
                        if i < len(bible_lst) - 2 and (bible_lst[i + 1] + " " + bible_lst[i + 2] == 'chapter 1' or
                                                       bible_lst[i + 1] + " " + bible_lst[i + 2] == 'psalm 1'):
                            verse.pop()

                        # add verse to to the bible dictionary
                        if verse_num not in bible_dict[book][chapter]:
                            bible_dict[book][chapter][verse_num] = verse

        return bible_dict

    # def __repr__(self):
    #     pp = PrettyPrinter(depth=4)
    #     pp.pprint(self.dict)
